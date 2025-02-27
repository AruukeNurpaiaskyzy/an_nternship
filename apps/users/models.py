from django.contrib.auth.models import AbstractUser
from django.db import models


import re
from django.core.exceptions import ValidationError


# для фалидации теле
def validate_phone_number(value):
    if not re.match(r'^\+996\d{9}$', value):
        raise ValidationError('Номер телефона должен быть в формате +996XXXXXXXXX')

class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    age = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


# class User(AbstractUser):
#     phone_number = models.CharField(max_length=15, unique=True, validators=[validate_phone_number])
#     ...