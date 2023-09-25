#se importan las funciones necesarias para la utilizacion de Flask
from flask import Flask, render_template, request, redirect, url_for
#se importa la clase a utilizar
from claseListaActividades import ListaActividades

#se crea una instancia del framework flask, __name__ hace referencia al punto de entrada de la aplicacion y template_folder es la carpeta por defecto 
#donde se buscarán las plantillas HTML
app = Flask(__name__, template_folder='templates')
#instancia de la clase ListaActividades
listaActividades = ListaActividades()

#app.route es un decorador en Flask y se utiliza para asociar una función con una ruta específica en una aplicación web Flask.
#en este caso, se la asocia a la ruta raiz
@app.route('/')
def toDoList():
    actividades = listaActividades.getActividades()
    # Inicializa listas vacías para actividades activas e inactivas
    actividadesActivas, actividadesInactivas, actividadesPendientes = [], [], 0
    # Itera sobre las actividades y clasifícalas en las listas correspondientes
    for actividad in actividades:
        if actividad.getEstado() == 'Active':
            actividadesPendientes+=1
            actividadesActivas.append(actividad)
        elif actividad.getEstado() == 'Inactive':
            actividadesInactivas.append(actividad)
    #render_template es una función proporcionada por Flask que se utiliza para cargar y renderizar una plantilla HTML. 
    # En este caso, se carga la plantilla llamada "index.html" y los parametros necesarios
    return render_template('index.html', actividades=actividades, actividadesActivas=actividadesActivas, actividadesInactivas=actividadesInactivas, actividadesPendientes=actividadesPendientes)

#ruta para agregar una tarea, que utiliza el metodo POST que se encarga de enviar datos a un servidor web para crear o actualizar 
# un recurso en el servidor.
@app.route('/agregar', methods=['POST'])
def toDoListAgregar():
    tarea = request.form.get('tarea')  # Obtiene la tarea del formulario
    estado = "Active" #como predeterminado, se establece en Active el estado de la tarea
    listaActividades.crearActividad(tarea, estado) #se crea la actividad usando la instancia de la clase ListaActividades() y su metodo correspondiente
    print(f"Actividad '{tarea}' creada con éxito.") #se imprime para verificar si se imprimió correctamente.
    #redirect() es una función de Flask que se utiliza para redirigir al usuario a una nueva ubicación dentro de la aplicación web.
    #url_for() es otra función de Flask que se utiliza para generar la URL asociada a una vista o función específica en la aplicación. 
    # En este caso, se está generando la URL para la vista llamada "toDoList".
    return redirect(url_for("toDoList"))

#ruta para editar una tarea, la cual también utiliza el método POST
@app.route('/editar', methods=['POST'])
def editarTarea():
    tarea = request.form['tareaEditar'] # Obtiene la tarea A EDITAR del formulario
    nuevoNombre = request.form['nuevoNombre'] # Obtiene el nuevo nombre ingresado por el usuario
    listaActividades.modificarActividad(tarea, nuevoNombre) #se modifica la actividad usando la instancia de la clase ListaActividades() y su metodo correspondiente
    
    #Este código sirve para depurar y ver si está funcionando correctamente
    #actividades = listaActividades.getActividades()
    #print([actividad.getNombre() for actividad in actividades])
    # se retorna nuevamente utilizando redirect() y url_for()
    return redirect(url_for("toDoList"))

#ruta para eliminar una tarea, la cual también utiliza el método POST
@app.route('/eliminar', methods=['POST'])
def eliminarTarea():
    tareaEliminar = request.form['tareaEliminar'] # Obtiene la tarea a eliminar del formulario
    listaActividades.eliminarActividad(tareaEliminar) #se elimina la actividad usando la instancia de la clase ListaActividades() y su metodo correspondiente
    return redirect(url_for("toDoList")) # se retorna nuevamente utilizando redirect() y url_for()

#ruta para marcar como completada una tarea, la cual también utiliza el método POST
@app.route('/marcarCompletada', methods=['POST'])
def marcarCompletada():
    tarea = request.form['tarea'] # Obtiene la tarea marcada como completada del formulario
    # Encuentra la tarea por su nombre y cambia su estado a "Inactive"
    listaActividades.chequearActividad(tarea)
    return redirect(url_for("toDoList")) # se retorna nuevamente utilizando redirect() y url_for()

#ruta para eliminar las tareas marcadas coomo completadas, la cual también utiliza el método POST
@app.route('/limpiarActividadesCompletadas', methods=['POST'])
def limpiarActividades():
    # Encuentra las tareas con el estado "Inactive" y las elimina de la lista
    listaActividades.limpiarActividadesCompletadas()
    return redirect(url_for("toDoList"))  # se retorna nuevamente utilizando redirect() y url_for()

#e utiliza para iniciar el servidor de desarrollo de Flask. 
if __name__ == '__main__':
    app.run(debug=True)