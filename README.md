# template
Actividad 1.2 sobre el funcionamiento de Templates en Django

**Cómo Ejecutar el Proyecto**
Requisitos
Python: Tener Python instalado (versión 3.8 o superior).
Entorno Virtual: Usar un entorno virtual para manejar las dependencias.

Pasos para Ejecutar el Proyecto
Clonar el Repositorio:

git clone <URL-del-repositorio>
cd <nombre-del-repositorio>

**Crear y Activar un Entorno Virtual:**
**En Windows:**
python -m venv venv
.\venv\Scripts\activate

**En macOS/Linux:**
python3 -m venv venv
source venv/bin/activate

Instalar Dependencias:
pip install django

Navegar a la Carpeta del Proyecto:
cd myproject

Migrar la Base de Datos:
python manage.py migrate

Ejecutar el Servidor de Desarrollo:
python manage.py runserver
Abrir el Proyecto en el Navegador:

Visita la siguiente URL en tu navegador:
http://127.0.0.1:8000/

**Estructura del Proyecto**
myproject/: Carpeta principal del proyecto Django.

myapp/: Aplicación Django que contiene la lógica del proyecto.

templates/myapp/index.html: Template que muestra los datos dinámicos.

static/myapp/styles.css: Archivo CSS para estilizar el template.


**Detener el Servidor: Presiona Ctrl + C en la terminal donde se está ejecutando el servidor.**
