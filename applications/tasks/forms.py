from django import forms
from django.forms import Form


class TaskForm(Form):
    """
        Clase para el formulario de tareas
    """
    tasks = forms.CharField(
        label= "Tarea",
        widget=forms.Textarea({"rows":"5"})
    )
    
    def clean_tasks(self):
        task = self.cleaned_data["tasks"]
        if len(task) < 8: 
            self.add_error("tasks", "El campo debe contener mas de 8 caracteres")
        return task