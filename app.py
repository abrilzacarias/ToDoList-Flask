from flask import Flask, render_template, request, redirect, url_for
from claseListaActividades import ListaActividades

app = Flask(__name__, template_folder='templates')
listaActividades = ListaActividades()

@app.route('/')
def toDoList():
    actividades = listaActividades.getActividades()
    for actividad in actividades:
        print(f"Nombre: {actividad.getNombre()}, Estado: {actividad.getEstado()}")
    return render_template('index.html', actividades=actividades)

@app.route('/agregar', methods=['POST'])
def toDoListAgregar():
    tarea = request.form.get('tarea')  # Obtiene la tarea del formulario
    estado = "active"
    nombre, estadoAct = listaActividades.crearActividad(tarea, estado)
    print(f"Actividad '{tarea}' creada con éxito.")

    return redirect(url_for("toDoList"))

@app.route('/editar', methods=['POST'])
def editarTarea():
    tarea = request.form['tareaEditar']
    nuevoNombre = request.form['nuevoNombre']
    listaActividades.modificarActividad(tarea, nuevoNombre)
    print([actividad.getNombre() for actividad in listaActividades.actividades])
    # Agrega aquí la lógica para editar la tarea con el ID proporcionado.
    return redirect(url_for("toDoList"))

@app.route('/eliminar', methods=['POST'])
def eliminarTarea():
    tareaEliminar = request.form['tareaEliminar']

    print(f"Intentando eliminar la tarea: {tareaEliminar}")

    listaActividades.eliminarActividad(tareaEliminar)

    return redirect(url_for("toDoList"))

if __name__ == '__main__':
    app.run(debug=True)