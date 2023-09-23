from claseActividad import Actividad

class ListaActividades:
    def __init__(self):
        self.actividades = []

    def crearActividad(self, nombreActividad, estado):
        actividad = Actividad(nombreActividad, estado)
        self.actividades.append(actividad)
        return actividad.getNombre(), actividad.getEstado()

    def getActividades(self):
        return self.actividades

    def modificarActividad(self):
        pass

    def eliminarActividad(self):
        pass

    def chequearActividad(self):
        pass

    def clasificarActividad(self):
        pass

    def limpiarActividadesCompletadas(self):
        pass
