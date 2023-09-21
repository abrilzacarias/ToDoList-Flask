class Actividad:
    def __init__(self, nombre, estado):
        self.__nombre = nombre
        self.__estado = estado
        self.__listaActividades = []
    
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre = nombre
    
    def getEstado(self):
        return self.__estado
    
    def setEstado(self, estado):
        self.__estado = estado

    def getListaActividades(self):
        return self.__listaActividades
    
    def setListaActividades(self, listaActividades):
        self.__listaActividades = listaActividades

    def crearActividad(self):
        pass

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