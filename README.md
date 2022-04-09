# Django REST boilerplate  
  
## Requisitos  
- Python 3.6 o superiror  
- pip  
- virtualenv  

## Datos generales
- Proyecto generado a partir de mi propio boilerplate(Para mas informacion viste el siguiente link)
  - `https://hartas17@bitbucket.org/hartas17/boilerplate.git`

## Proyecto Fibonacci
El poyecto consta de la solucion al problema fibonacci para obtener el valor fibonacci del valor n ingresado
Existen dos posibles soluciones relacionadas a dicho problema, la primera es la que nos enseñan en la escuela,
la forma recursiva y la segunda es via programacion dinamica: En este ejercicio utilizaremos revursividad

## Como instalar  
  
- Crea un entorno virtualenv y actívalo.  
- Clona el repositorio con:   
  - `git clone https://github.com/hartas17/Fibonacci.git`  
- Instala los requerimientos con:   
  - `pip install -r requirements/local.txt`
- Ejecutar migraciones:
    - `python manage.py migrate`
- Crear super usuario para el admin (opcional):
    - `python manage.py createsuperuser`
  
## Como ejecutar
 
    python manage.py runserver --settings controlhub.settings.local  

## Endpoint
- `http://0.0.0.0:8000/api/v1/fibonacci/eval/`
  - `method: POST`
  - `form-data: number`
  - `response: {
    "number": "2",
    "fibonacci": 1
}`
 
## Paqueterias incluidas  
- Django  
- Django rest  
- JWT  
- Rest endpoints para cuentas de usuario con JWT authentication:   
  - Registro con email
  - Activación de cuentas por email (Activado por default)  
  - Inicio de sesión  
  - Restablecimiento de contraseñas con url de un único uso  
  - Cambio de contraseña  
  - Postman Collection  
- Paginación automático con parametro dinámico para tamaño  


## Buenas prácticas:  

### Generales  
- Usar variables de entorno para todo la información sensible, por ejemplo: Contraseñas de servicios, api keys, secret keys, etc.  
- Establecer variables de entorno en los scripts de activar y desactivar del entorno virtual de cada proyecto.  
  
### Django y Django Rest  
- Para usar algún valor del settings utilizar el recomendado por la documentación y no importar el archivo directo.  
- Las validaciones no genéricas, siempre se deben estar en los serializers o forms, nunca en las views o en la sobre escritura del método save() de los modelos.  
  
## Como establecer variables de entorno en Windows  
Para activar y desactivar las variables de entorno de forma automática, es necesario agregar en los archivos que activan y desactivan el entorno virtual de python, en Windows el archivo a editar, si usas PowerShell (recomendado), es el active.ps1 que es el script de para PowerShell:  
  
 

    Set: 
    $env:DJANGO_SETTINGS_MODULE = 'boilerplate.settings.local'     
    
    Delete: 
    Remove-Item env:DJANGO_SETTINGS_MODULE 

 
  
### Como establecer variables de entorno en sistemas Posix en el virtualenv  
  
## Entorno de producción  
- Generar nueva SECRET_KEY siempre, ya que a pesar de que cuando se ejecuta el comando para renombrar el proyecto se genera una nueva secret_key, esta se versiona y puede quedar comprometida.  
```  
from django.core.management.utils import get_random_secret_key  
  
key = get_random_secret_key()  
print(key)  
```
