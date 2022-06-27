from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=255,unique=True)
    password = models.CharField(max_length=255)
    is_admin = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name