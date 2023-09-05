from django.contrib import admin

# models
from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "lastname", "email"]
    
admin.site.register(User, UserAdmin)