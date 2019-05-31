from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    mobile = models.IntegerField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)