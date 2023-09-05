from django.contrib import admin

# models
from .models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display  = ["id", "task", "status","user"]

admin.site.register(Task, TaskAdmin)