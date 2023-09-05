from django.db.models import Manager
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager, Manager):
    """
        Me permite realizar funciones para consulta, crear, actualizar y de eliminar
        registros del modelo de User
    """
    
    def __create_user(self, name=None, lastname=None, email=None, password= None, is_staff = False, is_superuser = False):
        user = self.model(
            name= name,
            lastname= lastname,
            email = email,
            is_staff = is_staff,
            is_superuser= is_superuser
        )
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_superuser(self,email, password):
        return self.__create_user(email=email, password=password, is_staff=True, is_superuser=True)
    
    def create_user(self, name, lastname,email, password):
        return self.__create_user(name, lastname, email, password, False, False)
    
    def get_user(self, pk):
        try:
            return self.get(pk=pk)
        except:
            return False