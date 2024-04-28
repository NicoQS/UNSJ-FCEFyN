from ClaseNodo import Nodo


class ColaEncadenada:
    __primero: Nodo
    __ultimo: Nodo
    
    def __init__(self):
        self.__primero = None
        self.__ultimo = None
    
    def insertar(self,elemento):
        nuevaNodo = Nodo(elemento)
        if self.Vacia():
            self.__primero = nuevaNodo
        else:
            self.__ultimo.setSiguiente(nuevaNodo)
        self.__ultimo = nuevaNodo

    def Vacia(self):
        return self.__primero == None
    
    def suprimir(self):
        x = None
        if not self.Vacia():
            x = self.__primero.getDato()
            self.__primero = self.__primero.getSiguiente()
        else:
            print("No hay personas en la cola")
        return x
    
    def getCantidad(self):
        return self.__cantidad
    
    def recorrer(self):
        aux=self.__primero
        while aux != None:
            print(aux.getDato())
            aux=aux.getSiguiente()