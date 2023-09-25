Aplicación de lista de tareas (To-Do List) desarrollada utilizando el framework Flask de Python. La aplicación de lista de tareas permite a los usuarios gestionar sus tareas pendientes de manera eficaz.

app: Contiene la lógica principal de la aplicación.
claseActividad: plantilla para crear una actividad, con sus correspondientes atributos y métodos.
claseListaActividades: contiene la plantilla para listar las actividades y poder agruparlas para la correspondiente funcionalidad de la aplicación.
templates/: Almacena las plantillas HTML utilizadas para las vistas web.
static/: Contiene archivos estáticos como hojas de estilo (CSS), JavaScript e imágenes.

La aplicación utiliza Flask para crear rutas y vistas web. Se definen rutas para mostrar la lista de tareas, agregar tareas, marcar como completadas, etc. Las plantillas HTML se utilizan para renderizar las páginas web, y se pasan datos desde Flask a las plantillas para mostrar información dinámica.

PARA EJECUTAR LA APLICACIÓN EN FLASK

Paso 1: Instalar Flask.

Se debe tener instalado Python.
Luego, instalar Flask utilizando pip, el administrador de paquetes de Python. Abre una terminal o línea de comandos y ejecuta el siguiente comando:

pip install Flask

Paso 2: Ejecutar la Aplicación
Ejecutar el archivo app.py. 

 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * 
Esto significa que tu aplicación Flask está escuchando en http://127.0.0.1:5000/ (también conocida como http://localhost:5000/).

Paso 3: Acceder a la Aplicación
Acceder a http://localhost:5000/ o http://127.0.0.1:5000/ desde un navegador web.
