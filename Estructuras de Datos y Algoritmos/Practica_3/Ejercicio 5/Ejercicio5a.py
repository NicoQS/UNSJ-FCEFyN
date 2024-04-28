"""

Ejercicio Nº 5   
Diseñe el algoritmo que, apoyado en el TAD Lista, elimine elementos con
valores repetidos de una lista de números naturales.
Entrada  L = ( 10, 5, 7, 5, 2, 10)      ->      Salida  L = ( 10, 5,7, 2)
a) Escriba el código que lo resuelve
b) Considere la lista dada, ordenada por contenido, y en función de esto optimice el código del ítem a. 


"""
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
    
    def insertarPos(self,dato,pos = -1):
        if pos == -1:
            pos = self.__tope + 1
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

    def eliminarRepetidos(self):
        for i in range(self.__tope):
            for j in range(i+1,self.__tope):
                if self.__items[i] == self.__items[j]:
                    self.suprimirPos(j+1)


if __name__ == "__main__":
    Lista = ListaSecuencial(6)
    Lista.insertarPos(10)
    Lista.insertarPos(5)
    Lista.insertarPos(7)
    Lista.insertarPos(5)
    Lista.insertarPos(2)
    Lista.insertarPos(10)
    print("Lista original")
    Lista.mostrar()
    Lista.eliminarRepetidos()
    print("Lista sin repetidos")
    Lista.mostrar()