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
        if not self.Vacia():
            aux = self.__primero
            self.__primero = self.__primero.getSiguiente()
            if self.__primero == None:
                self.__ultimo = None
            del aux
        else:
            print("No hay elementos en la lista")
    
    def recorrer(self):
        aux=self.__primero
        while aux != None:
            print(aux.getDato())
            aux=aux.getSiguiente()


if __name__ == "__main__":
    Pila = ColaEncadenada()
    Pila.insertar(1)
    Pila.insertar(2)
    Pila.insertar(3)
    Pila.insertar(4)
    Pila.suprimir()
    Pila.recorrer()