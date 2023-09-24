from flask import Flask, render_template, request, redirect, url_for
from claseListaActividades import ListaActividades

app = Flask(__name__, template_folder='templates')
listaActividades = ListaActividades()

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
    return render_template('index.html', actividades=actividades, actividadesActivas=actividadesActivas, actividadesInactivas=actividadesInactivas, actividadesPendientes=actividadesPendientes)

@app.route('/agregar', methods=['POST'])
def toDoListAgregar():
    tarea = request.form.get('tarea')  # Obtiene la tarea del formulario
    estado = "Active"
    nombre, estadoAct = listaActividades.crearActividad(tarea, estado)
    print(f"Actividad '{tarea}' creada con éxito.")

    return redirect(url_for("toDoList"))

@app.route('/editar', methods=['POST'])
def editarTarea():
    tarea = request.form['tareaEditar']
    nuevoNombre = request.form['nuevoNombre']
    listaActividades.modificarActividad(tarea, nuevoNombre)
    actividades = listaActividades.getActividades()
    print([actividad.getNombre() for actividad in actividades])
    # Agrega aquí la lógica para editar la tarea con el ID proporcionado.
    return redirect(url_for("toDoList"))

@app.route('/eliminar', methods=['POST'])
def eliminarTarea():
    tareaEliminar = request.form['tareaEliminar']
    listaActividades.eliminarActividad(tareaEliminar)
    return redirect(url_for("toDoList"))

@app.route('/marcarCompletada', methods=['POST'])
def marcarCompletada():
    tarea = request.form['tarea']
    # Encuentra la tarea por su nombre y cambia su estado a "Inactive"
    listaActividades.chequearActividad(tarea)
    return redirect(url_for("toDoList"))


@app.route('/limpiarActividadesCompletadas', methods=['POST'])
def limpiarActividades():
    # Encuentra la tarea por su nombre y cambia su estado a "Inactive"
    listaActividades.limpiarActividadesCompletadas()
    return redirect(url_for("toDoList"))

if __name__ == '__main__':
    app.run(debug=True)