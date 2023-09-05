
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin


class TaskPermisionMixin(LoginRequiredMixin):
    """
    TaskPermisionMixin:
        verificar si el usuario se encuentra logueado
        si no es asi lo devuelve a la pagina de login    
    """
    login_url = reverse_lazy("users_app:logout")
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            print("entro")
            return self.handle_no_permission()
        print("no entro")
        return super().dispatch(request, *args, **kwargs)