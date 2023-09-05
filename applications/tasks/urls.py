from django.urls import path

# views 
from .views import TaskIndex
from .views import DeleteTaskView
from .views import UpdateTaskView

app_name = "tasks_app"

urlpatterns = [
    path("", TaskIndex.as_view(), name="index"),
    path("delete/<int:pk>", DeleteTaskView.as_view(), name="delete"),
    path("update/<int:pk>", UpdateTaskView.as_view(), name="update")
]