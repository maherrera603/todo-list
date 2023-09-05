from django.urls import path

# views 
from .views import SingInView
from .views import RegisterView
from .views import LogoutView

app_name = "users_app"

urlpatterns = [
    path("", SingInView.as_view(), name="login"),
    path("registro/", RegisterView.as_view(), name="register"),
    path("logout/", LogoutView.as_view(), name="logout")
]
