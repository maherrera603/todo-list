# Todo List App

Sistama de tareas en el cual un usuario podra crear una cuenta para ingresar al sistema y registrar las tareas pendientes que tenga por realizar en su dia.

## Environment Variables

Para correr este proyecto necesita configurar el archivo production.py donde se encuentra en todo/settings las variables para conectarse a la base de datos

`NAME`

`USER`

`PASSWORD`


## Iniciar en local

Crear una carpeta
```bash
mkdir "nombreCarpeta"
```
Ingresar a la carpeta creada
```bash
cd "nombreCarpeta"
```

Instalar entorno virtual
```bash
python -m venv venv
```

Activar entorno virtual
```bash
venv\Scripts\activate
```

Clone el proyecto

```bash
  git clone https://github.com/maherrera603/todo-list.git
```

ir al directorio del proyecto

```bash
  cd todo
```

instalar dependencias

```bash
  pip install -r requirements.txt
```

realizar las migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```

Iniciar el servidor
```bash
  python manage.py runserver
```
