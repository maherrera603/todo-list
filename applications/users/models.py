from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

# managers
from .managers import UserManager

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=100)
    objects = UserManager()
    USERNAME_FIELD = "email"
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)