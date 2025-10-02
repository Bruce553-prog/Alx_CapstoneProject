from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, null=True)
    email=models.EmailField(unique=True,blank=False)
    address = models.TextField(blank=True, null=True)


