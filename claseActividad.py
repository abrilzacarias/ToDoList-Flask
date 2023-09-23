class Actividad:
    def __init__(self, nombre, estado):
        self.__nombre = nombre
        self.__estado = estado
    
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre = nombre
    
    def getEstado(self):
        return self.__estado
    
    def setEstado(self, estado):
        self.__estado = estado

