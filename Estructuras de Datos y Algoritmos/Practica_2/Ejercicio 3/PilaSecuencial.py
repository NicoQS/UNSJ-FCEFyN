import numpy as np
class PilaSecuencial:
    __items: np.array
    __top: int
    __cantidad: int
    
    def __init__(self,dimension):
        self.__items = np.empty(dimension,dtype=int)
        self.__top = 0
        self.__cantidad = dimension
    
    def Vacia(self):
        return self.__top == 0
    
    def insertar(self,item):
        if self.__top < self.__cantidad:
            self.__items[self.__top] = item
            self.__top += 1
        else:
            print("Pila llena")
    
    def suprimir(self):
        if not self.Vacia():
            self.__top -= 1
            np.delete(self.__items,self.__top)
        else:
            print("Pila vacia")

    def recorrer(self):
        fact=1
        while not self.Vacia():
            self.suprimir()
            fact*=self.__items[self.__top] #fact = fact * self.__items[self.__top]
        print("El numero factorial es: ",fact)

    def mostrarFactorial(self,numero):
        while numero > 0:
            self.insertar(numero)
            numero -= 1
        self.recorrer()