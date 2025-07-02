# Tareas API

API REST básica para gestionar tareas usando Django y Django REST Framework.

## Instalación
1. Clona el repositorio: `git clone <C:\Users\SUN\tareas_api>`
2. Instala dependencias: `pip install -r requirements.txt`
3. Aplica migraciones: `python manage.py migrate`
4. Inicia el servidor: `python manage.py runserver`

## Uso
- **GET /tareas/**: Lista todas las tareas.
- **POST /tareas/**: Crea una nueva tarea.


## Endpoints
- **POST /tareas/**  
  Ejemplo: `{ "titulo": "Tarea 1", "descripcion": "Descripción", "usuario": 1 }`
- **GET /tareas/**  
  Retorna lista paginada de tareas.