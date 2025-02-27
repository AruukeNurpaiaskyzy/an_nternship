from django.db import models
from apps.users.models import User
from ckeditor.fields import RichTextField

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='todo_images/', null=True, blank=True)
    content = RichTextField()

    def __str__(self):
        return self.title