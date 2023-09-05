from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
from django.views.generic import FormView
from django.views.generic import ListView
from django.views.generic import View
from django.urls import reverse_lazy

# models
from .models import Task
from applications.users.models import User

# forms
from .forms import TaskForm

# permissions
from .permissions import TaskPermisionMixin


# Create your views here.
class TaskIndex(TaskPermisionMixin, ListView, FormView):
    # TaskIndex:
    # muestra la vista del sistema despues de loguearse
    # extrae las tareas de registradas por el usuario
    # procesa el formulario para registrar las tareas del usuario
    template_name = "tasks/index.html"
    form_class = TaskForm
    success_url = reverse_lazy("tasks_app:index")
    paginate_by = 5
    model = None
    context_object_name = "tasks"
    
    def get_context_data(self, **kwargs):
        user_pk =  self.request.user.id
        user = User.objects.get_user(user_pk)
        context = super().get_context_data(**kwargs)
        context["user"] =  user
        return context
    
    def form_valid(self, form):
        user = self.request.user
        task = form.cleaned_data["tasks"]
        Task.objects.add_task(task, user)
        return super().form_valid(form)
    
    def get_queryset(self):
        user_pk =  self.request.user.id
        user = User.objects.get_user(user_pk)
        tasks = Task.objects.all_task(user).order_by("-status")
        return tasks
    

class DeleteTaskView(TaskPermisionMixin, View):
    # DeleteTaskView: 
    # procesa la logica para eliminar dicha tarea por el id 
    # sin importar el estado de la tarea
    login_url = reverse_lazy("users_app:logout")
    
    def get(self, request, *args, **kwargs):
        pk = self.kwargs["pk"]
        Task.objects.delete_task(pk)
        return HttpResponseRedirect(reverse_lazy("tasks_app:index"))
    
    
class UpdateTaskView(TaskPermisionMixin, View):
    # UpdateTaskView:
    # Actualizar el estado de la tarea de Pendiente a Completada
    # mediante el pk
    login_url = reverse_lazy("users_app:logout")
    
    def get(self, request, *args, **kwargs):
        pk = self.kwargs["pk"]
        Task.objects.update_task(pk)
        return HttpResponseRedirect(reverse_lazy("tasks_app:index"))
