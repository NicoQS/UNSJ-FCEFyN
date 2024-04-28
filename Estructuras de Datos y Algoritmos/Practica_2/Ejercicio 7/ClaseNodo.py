class Nodo:
    __dato = None
    __sigNodo = None
    
    def __init__(self,dat):
        self.__dato = dat
        self.__sigNodo=None

    def  setItem(self,item):
        self.__dato=item
    
    def setSiguiente(self,siguiente):
        self.__sigNodo=siguiente

    def getSiguiente(self):
        return self.__sigNodo

    def getDato(self):
        return self.__dato