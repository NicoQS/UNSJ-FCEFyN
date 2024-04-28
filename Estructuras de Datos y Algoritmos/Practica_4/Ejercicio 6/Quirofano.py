class Quirofano:
    __tiempoActual: int
    __libre: bool
    __tiempoAtencion: int
    
    
    def __init__(self):
        self.__tiempoActual = 0
        self.__libre = True
        self.__tiempoAtencion = 0
    
    def ocupar(self):
        self.__libre = False
    
    def estaLibre(self):
        return self.__libre
    
    def setTiempoAtencion(self,tiempo):
        self.__tiempoAtencion = tiempo
    
    def actualizar(self):
        self.__tiempoActual += 1
        if self.__tiempoActual == self.__tiempoAtencion:
            self.__libre = True
            self.__tiempoActual = 0
            self.__tiempoAtencion = 0