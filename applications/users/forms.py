from django.contrib.auth import authenticate
from django import forms
from django.forms import Form

class LoginForm(Form):
    """
        Formulario  de login
    """
    
    email = forms.CharField(
        label="Correo Electronico",
        widget=forms.TextInput({"type":"email", "placeholder": "Correo electronico"})
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.TextInput({"type":"password", "placeholder": "Contraseña"})
    )
    
    def clean_password(self):
        password = self.cleaned_data["password"];
        if len(password) < 8 or len(password) > 12:
            self.add_error("password", "La contraseña debe ser de 8 a 12 caracteres")
        return password
    
    
    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = self.cleaned_data["email"]
        password = self.cleaned_data["password"]
        if not authenticate(email=email, password=password):
            raise forms.ValidationError("Los datos son incorrectos")
        return cleaned_data


class RegisterForm(Form):
    """
        Formulario de registro
    """
    
    name = forms.CharField(
        label="Nombres",
        widget=forms.TextInput({"type": "text", "placeholder": "Nombres completos"})
    )
    
    lastname = forms.CharField(
        label="Apellidos",
        widget=forms.TextInput({"type": "text", "placeholder": "Apellidos completos"})
    )
    
    email = forms.CharField(
        label="Correo Electronico",
        widget=forms.TextInput({"type":"email", "placeholder": "Correo electronico"})
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.TextInput({"type":"password", "placeholder": "Contraseña"})
    )
    
    pwd = forms.CharField(
        label="Repetir contraseña",
        widget=forms.TextInput({"type":"password", "placeholder": "Repetir contraseña"})
    )
    
    def clean_name(self):
        name = self.cleaned_data["name"]
        if len(name) < 3 or len(name) > 20:
            self.add_error("name", "El campo debe contener de 3 a 20 caracteres")
        return name
    
    def clean_lastname(self):
        lastname = self.cleaned_data["lastname"]
        if len(lastname) < 3 or len(lastname) > 20:
            self.add_error("lastname", "El campo debe contener de 3 a 20 caracteres")
        return lastname
    
    def clean_password(self):
        password = self.cleaned_data["password"];
        if len(password) < 8 or len(password) > 12:
            self.add_error("password", "La contraseña debe ser de 8 a 12 caracteres")
        return password
    
    def clean_pwd(self):
        password = self.cleaned_data["password"]
        pwd = self.cleaned_data["pwd"]

        if len(pwd) < 8 or len(pwd) > 12:
            self.add_error("pwd", "La contraseña debe ser de 8 a 12 caracteres")
        elif password != pwd:
            self.add_error("pwd", "Las contraseñas no coinciden")
            
        return pwd