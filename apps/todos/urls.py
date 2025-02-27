from django.urls import path
from .views import TodoListCreateView, TodoRetrieveUpdateDestroyView, TodoDeleteAllView

urlpatterns = [
    path('todos/', TodoListCreateView.as_view()),
    path('todos/<int:pk>/', TodoRetrieveUpdateDestroyView.as_view()),
    path('todos/delete-all/', TodoDeleteAllView.as_view()),
]