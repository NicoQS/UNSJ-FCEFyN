class Nodo:
    __dato: int
    __izquierdo: None 
    __derecho: None
    
    def __init__(self, dato) -> None:
        self.__dato = dato
        self.__izquierdo = None
        self.__derecho = None
        
    def getDato(self):
        return self.__dato
    
    def setDato(self,newdato):
        self.__dato = newdato
    
    def getIzquierdo(self):
        return self.__izquierdo
    
    def setIzquierdo(self,newizq):
        self.__izquierdo = newizq
    
    def getDerecho(self):
        return self.__derecho

    def setDerecho(self,newder):
        self.__derecho = newder
        
    def tieneDerecho(self):
        return self.__derecho != None
    
    def tieneIzquierdo(self):
        return self.__izquierdo != None