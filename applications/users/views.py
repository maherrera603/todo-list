from django.http import HttpResponse
from django.views.generic import FormView
from django.views.generic import View
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

# models
from .models import User

# forms
from .forms import LoginForm
from .forms import RegisterForm


# Create your views here.
class SingInView(FormView):
    # clase SingInView: 
    # muestra la vista login de usuario
    # procesa los datos de email y password para conceder acceso al sistema
    __user:None
    template_name = "users/login.html"
    form_class = LoginForm
    success_url = reverse_lazy("tasks_app:index")
    
    def form_valid(self, form):
        email = form.cleaned_data["email"]
        password= form.cleaned_data["password"]
        self.__user = authenticate(email=email, password=password)
        login(self.request, self.__user)
        return super(SingInView, self).form_valid(form)
    
    
class RegisterView(FormView):
    # clase RegisterView: 
    # muestra la vista de registro de usuarios
    # procesa los datos del usuario para registrar al usuario
    template_name = "users/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy("users_app:register")
    
    def form_valid(self, form):
        name = form.cleaned_data["name"]
        lastname = form.cleaned_data["lastname"]
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]
        User.objects.create_user(name, lastname, email, password)
        return super(RegisterView, self).form_valid(form)
    
    
class LogoutView(View):
    # clase LogoutView: 
    # permite al usuario cerrar sesion del sistema y redirecciona al login
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse_lazy("users_app:login"))