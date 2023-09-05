from django.db import models
from django.db.models import Model

# models
from applications.users.models import User

# managers
from .managers import TaskManager

# Create your models here.
class Task(Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.TextField(max_length=255, null=False, blank=False)
    status = models.CharField(max_length=30, null=False, blank=False)
    objects = TaskManager()
