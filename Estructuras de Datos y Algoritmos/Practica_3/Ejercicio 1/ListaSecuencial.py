import numpy as np

class ListaSecuencial:
    __items: np.array
    __tope: int
    __tamTotal: int
    
    def __init__(self,dimension) -> None:
        self.__items = np.full(dimension, None)
        self.__tope = 0
        self.__tamTotal = dimension
    
    def Vacia(self):
        return self.__tope == 0
    
    def llena(self):
        return self.__tope == self.__tamTotal
    
    def posValida(self,pos):
        return pos > 0 and pos-1 <= self.__tope
    
    def insertarPos(self,dato,pos):
        if self.llena():
            print("La lista esta llena")
            raise Exception("La lista esta llena")
        
        elif not self.posValida(pos):
            print("Posicion invalida")
            raise Exception("Posicion invalida")
        pos -= 1
        for i in range(self.__tope, pos,-1):
                self.__items[i] = self.__items[i-1]
        self.__items[pos] = dato
        self.__tope += 1
    
    def suprimirPos(self,pos):
        if not self.posValida(pos):
            print("Posicion invalida")
            raise Exception("Posicion invalida")
        
        for i in range(pos-1, self.__tope-1):
            self.__items[i] = self.__items[i+1]
        
        self.__items[self.__tope-1] = None
        self.__tope -= 1
    
    def buscar (self,dato):
        pos = 0
        while pos < self.__tope and self.__items[pos] != dato:
            pos += 1
        if pos == self.__tope:
            return -1
        else:
            return pos
    
    def recuperar(self,pos):
        if not self.posValida(pos):
            print("Posicion invalida")
        else:
            return self.__items[pos-1]
    
    def mostrar(self):
        for i in range(self.__tope):
            print(self.__items[i])


if __name__ == "__main__":
    Lista = ListaSecuencial(5)
    Lista.insertarPos(1,1)
    Lista.insertarPos(2,2)
    Lista.insertarPos(15,3)
    Lista.insertarPos(4,4)
    Lista.insertarPos(23,5)
    Lista.suprimirPos(5)
    print("El elemento de la pos 3, es: " + str(Lista.recuperar(3)))
    print("El elemento 23 esta en la pos: " + str(Lista.buscar(23)+1))
    print("--LISTADO--")
    Lista.mostrar()