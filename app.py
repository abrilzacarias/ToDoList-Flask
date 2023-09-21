from flask import Flask, render_template, request
from claseListaActividades import ListaActividades

app = Flask(__name__, template_folder='templates')
listaActividades = ListaActividades()

@app.route('/', methods=['GET', 'POST'])
def toDoListAgregar():

    tarea = request.form.get('tarea')  # Obtiene la tarea del formulario
    estado = "active"
    nombre, estadoAct = listaActividades.crearActividad(tarea, estado)
    print(f"Actividad '{tarea}' creada con éxito.")

    actividades = listaActividades.getActividades()
    return render_template('index.html', nombre=nombre, estadoAct=estadoAct)
'''@app.route('/')
def toDoList():
    return render_template('index.html')'''

if __name__ == '__main__':
    app.run(debug=True)