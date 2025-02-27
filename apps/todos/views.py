from rest_framework import generics, permissions
from .models import Todo
from .serializers import TodoSerializer
from django_filters import rest_framework as filters
from rest_framework.response import Response
from rest_framework import status

class TodoListCreateView(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TodoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

class TodoDeleteAllView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        self.get_queryset().delete()
        return Response(status=204)





class TodoFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    is_completed = filters.BooleanFilter()

    class Meta:
        model = Todo
        fields = ['title', 'is_completed']

class TodoListCreateView(generics.ListCreateAPIView):
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = TodoFilter
    ...