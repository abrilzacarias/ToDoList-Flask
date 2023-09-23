from claseActividad import Actividad

class ListaActividades:
    def __init__(self):
        self.actividades = []

    def getActividades(self):
        return self.actividades
    
    def crearActividad(self, nombreActividad, estado):
        actividad = Actividad(nombreActividad, estado)
        self.actividades.append(actividad)
        return actividad.getNombre(), actividad.getEstado()

    def modificarActividad(self, actividadActual, nuevaActividad):
        actividades = self.getActividades()
        for actividad in actividades:
            if actividadActual == actividad.getNombre():
                actividad.setNombre(nuevaActividad)
        return actividades  

    def eliminarActividad(self, actividadEliminar):
        actividades = self.getActividades()
        for actividad in actividades:
            if actividadEliminar == actividad.getNombre():
                self.actividades.remove(actividad)
        return actividades  

    def chequearActividad(self):
        pass

    def clasificarActividad(self):
        pass

    def limpiarActividadesCompletadas(self):
        pass
