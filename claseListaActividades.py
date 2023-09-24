from claseActividad import Actividad

class ListaActividades:
    def __init__(self):
        self.__actividades = []

    def setActividades(self, actividades):
        self.__actividades = actividades

    def getActividades(self):
        return self.__actividades
    
    def crearActividad(self, nombreActividad, estado):
        actividades = self.getActividades()
        actividad = Actividad(nombreActividad, estado)
        actividades.append(actividad)
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
                actividades.remove(actividad)
        return actividades  

    def chequearActividad(self, nombreTarea):
        actividades = self.getActividades()
        for actividad in actividades:
            if actividad.getNombre() == nombreTarea:
                actividad.setEstado("Inactive")
        return actividades 
    
    def clasificarActividad(self):
        pass

    def limpiarActividadesCompletadas(self):
        actividades = self.getActividades()
        actividadesPorEliminar = []

        for actividad in actividades:
            if actividad.getEstado() == 'Inactive':
                actividadesPorEliminar.append(actividad)

        for actividad in actividadesPorEliminar:
            actividades.remove(actividad)

