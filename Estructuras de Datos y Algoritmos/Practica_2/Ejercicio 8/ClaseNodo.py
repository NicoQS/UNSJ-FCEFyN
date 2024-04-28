class Nodo:
    __paciente = None
    __siguiente = None
    
    def __init__(self,dat):
        self.__paciente = dat
        self.__siguiente=None

    def  setItem(self,item):
        self.__paciente=item
    
    def setSiguiente(self,siguiente):
        self.__siguiente=siguiente

    def getSiguiente(self):
        return self.__siguiente

    def getPaciente(self):
        return self.__paciente