"""

Ejercicio Nº 5   
Diseñe el algoritmo que, apoyado en el TAD Lista, elimine elementos con
valores repetidos de una lista de números naturales.
Entrada  L = ( 10, 5, 7, 5, 2, 10)      ->      Salida  L = ( 10, 5,7, 2)
a) Escriba el código que lo resuelve
b) Considere la lista dada, ordenada por contenido, y en función de esto optimice el código del ítem a. 


"""
import numpy as np

class ListaSecuencialOrdenada:
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
    
    def insertarContenido(self,dato):
        if self.llena():
            print("La lista esta llena")
            raise Exception("La lista esta llena")
        pos = 0
        
        while pos < self.__tope and self.__items[pos] < dato:
            pos += 1
        
        for i in range(self.__tope, pos,-1):
                self.__items[i] = self.__items[i-1]
        self.__items[pos] = dato
        self.__tope += 1
    
    def suprimirPos(self, pos):
        if not self.posValida(pos):
            print("Posicion invalida")
            raise Exception("Posicion invalida")
        
        for i in range(pos-1, self.__tope-1):
            self.__items[i] = self.__items[i+1]
        
        self.__items[self.__tope-1] = None
        self.__tope -= 1
    
    def buscar (self,dato):
        izq = 0
        der = self.__tope - 1
        while izq <= der:
            medio = (izq + der) // 2
            if self.__items[medio] == dato:
                return medio 
            elif self.__items[medio] < dato:
                izq = medio + 1
            else:
                der = medio - 1
        return -1
    
    def primerElemento(self):
        if not self.Vacia():
            return self.__items[0]
        else:
            return None
    
    def ultimoElemento(self):
        if not self.Vacia():
            return self.__items[self.__tope-1]
        else:
            return None
    
    def recuperar(self,pos):
        if not self.posValida(pos):
            print("Posicion invalida")
        else:
            return self.__items[pos-1]
    
    def mostrar(self):
        for i in range(self.__tope):
            print(self.__items[i])
    
    def eliminaRepetidosOptimizado(self):
        elementoPrevio = self.recuperar(1)
        i = 1
        while i < self.__tope:
            elementoActual = self.recuperar(i+1)
            if elementoActual == elementoPrevio:
                self.suprimirPos(i)
            else:
                elementoPrevio = elementoActual
                i += 1


if __name__ == "__main__":
    Lista = ListaSecuencialOrdenada(7)
    Lista.insertarContenido(10)
    Lista.insertarContenido(5)
    Lista.insertarContenido(7)
    Lista.insertarContenido(5)
    Lista.insertarContenido(2)
    Lista.insertarContenido(10)
    print("Lista original")
    Lista.mostrar()
    print("------------------")
    print("Lista sin repetidos")
    Lista.eliminaRepetidosOptimizado()
    Lista.mostrar()