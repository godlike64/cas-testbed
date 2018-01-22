from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=False, unique=True)
    password = models.CharField(max_length=40, blank=False)
    twitter = models.CharField(max_length=15, blank=True)
    name = models.CharField(max_length=60, blank=True)
    bio = models.TextField()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['username', 'email', 'password']
