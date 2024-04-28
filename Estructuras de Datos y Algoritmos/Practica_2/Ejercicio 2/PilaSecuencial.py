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
        binario=""
        while not self.Vacia():
            self.suprimir()
            binario+=str(self.__items[self.__top])
        print("El numero binario es: ",binario)

    def conversionBinario(self,decimal):
        binario=0
        while int(decimal/2) > 0:
            binario = decimal%2
            self.insertar(binario)
            decimal=int(decimal/2)
        self.insertar(decimal)
        self.recorrer()