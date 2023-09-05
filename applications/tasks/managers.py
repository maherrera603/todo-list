from django.db.models import Manager

class TaskManager(Manager):
    """
        Me permite realizar funciones para consulta, crear, actualizar y de eliminar
        registros del modelo de Task
    """
    def add_task(self, tasks, user):
        task = self.model(
            user=user,
            task=tasks,
            status="Pendiente"
        )
        task.save()

    def all_task(self, user):
        tasks = self.filter(user__id = user.id)
        return tasks

    def delete_task(self, pk):
        try:
            task = self.get(pk=pk)
            return task.delete()
        except:
            return False
        
    def update_task(self, pk):
        try:
            task = self.get(pk=pk)
            task.status = "Completada"
            return task.save()
        except:
            return False
