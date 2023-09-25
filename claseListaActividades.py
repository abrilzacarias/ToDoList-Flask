#Importa la clase Actividad
from claseActividad import Actividad
#Definición de la clase ListaActividades
class ListaActividades:
    #Constructor de la clase
    def __init__(self):
        self.__actividades = [] #Inicializa lista

    #Método paara establecer la lista de actividades
    def setActividades(self, actividades):
        self.__actividades = actividades

    #Método para obtener la lista de actividades
    def getActividades(self):
        return self.__actividades
    
    #Método para crear una nueva actividad y agregarla a una lista
    def crearActividad(self, nombreActividad, estado):
        actividades = self.getActividades()
        actividad = Actividad(nombreActividad, estado)
        actividades.append(actividad)
        return actividad.getNombre(), actividad.getEstado()

    #Método para modificar una actividad existente
    def modificarActividad(self, actividadActual, nuevaActividad):
        actividades = self.getActividades()
        for actividad in actividades:
            if actividadActual == actividad.getNombre():
                actividad.setNombre(nuevaActividad)
        return actividades  

    #Método para eliminar una actividad
    def eliminarActividad(self, actividadEliminar):
        actividades = self.getActividades()
        for actividad in actividades:
            if actividadEliminar == actividad.getNombre():
                actividades.remove(actividad)
        return actividades  

    #Método para marcar una actividad como inactiva (completada)
    def chequearActividad(self, nombreTarea):
        actividades = self.getActividades()
        for actividad in actividades: #se recorre la lista de actividades
            if actividad.getNombre() == nombreTarea:
                actividad.setEstado("Inactive")
        return actividades 

    #Método para limpiar actividades completadas
    def limpiarActividadesCompletadas(self):
        actividades = self.getActividades() #obtenemos las actividades
        actividadesPorEliminar = [] #lista de las acts por eliminar

        for actividad in actividades:
            if actividad.getEstado() == 'Inactive': #si el estado de la actividad se encuentra inactiva se la agrega a la lista
                #de acts por eliminar 
                actividadesPorEliminar.append(actividad)

        for actividad in actividadesPorEliminar:
            actividades.remove(actividad) #se elimina la actividad

