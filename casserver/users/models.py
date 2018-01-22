from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    twitter = models.CharField(max_length=15, blank=True)
    bio = models.TextField(blank=True)
    birth_date = models.DateField(blank=True)
