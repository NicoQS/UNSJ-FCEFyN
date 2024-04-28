class Nodo:
    __dato = None
    __sigNodo = None
    
    def __init__(self,dat):
        self.__dato = dat
        self.__sigNodo=None

    def  setDato(self,item):
        self.__dato=item
    
    def setSiguiente(self,siguiente):
        self.__sigNodo=siguiente

    def getSiguiente(self):
        return self.__sigNodo

    def getDato(self):
        return self.__dato

class Lista:
    __primero: Nodo
    __ultimo: Nodo
    __cantidad: int
    
    def __init__(self):
        self.__primero = None
        self.__ultimo = None
        self.__cantidad = 0
    
    def insertar(self,elemento):
        nuevaNodo = Nodo(elemento)
        if self.Vacia():
            self.__primero = nuevaNodo
            self.__ultimo = nuevaNodo
        else:
            nodo = self.buscar(elemento)
            if nodo == None:
                self.__ultimo.setSiguiente(nuevaNodo)
                self.__ultimo = nuevaNodo
            else:
                nodo.setDato(elemento)
        self.__cantidad += 1

    def Vacia(self):
        return self.__primero == None
    
    def buscar(self,elemento):
        aux=self.__primero
        while aux != None:
            if aux.getDato() == elemento:
                return aux
            aux=aux.getSiguiente()
        return None
    
    def getCantidad(self):
        return self.__cantidad
    
    def recorrer(self):
        aux=self.__primero
        listado = ""
        while aux != None:
            listado += str(aux.getDato()) + " -> "
            aux=aux.getSiguiente()
        listado += "None"
        print(listado)