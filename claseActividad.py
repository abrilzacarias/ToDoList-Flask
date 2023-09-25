#Se define la clase Actividad
class Actividad:
    #Constructor de la clase con sus atributos
    def __init__(self, nombre, estado):
        self.__nombre = nombre
        self.__estado = estado
    
    #Método para obtener el valor del atributo nombre
    def getNombre(self):
        return self.__nombre
    
    #Método para establecer un valor al atributo nombre
    def setNombre(self, nombre):
        self.__nombre = nombre
    
    #Método para obtener el valor del atributo estado
    def getEstado(self):
        return self.__estado
    
    #Método para establecer un valor al atributo estado
    def setEstado(self, estado):
        self.__estado = estado

    #Método para obtener la lista de actividades
    #POLIMORFISMO, ya que en claseListaActividades existe un metodo llamado igual pero con distinto comportamiento
    def getActividades(self):
        return self.getNombre(), self.getEstado()

