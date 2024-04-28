import numpy as np
class PilaSecuencial:
    __items: np.array
    __top1: int
    __top2: int
    __cantidad: int
    
    def __init__(self,dimension):
        self.__items = np.empty(dimension,dtype=int)
        self.__top1 = 0
        self.__top2 = dimension - 1
        self.__cantidad = dimension
    
    def Vacia(self):
        return self.__top1 == 0 and self.__top2 == self.__cantidad-1
    
    def PilaLlena(self):
        return self.__top1 + 1 < self.__top2
    
    def insertar(self,item):
        pila = int(input("Ingrese el tipo de pila a utilizar: 1 o 2: "))
        if self.PilaLlena():
            if pila == 1:
                self.__items[self.__top1] = item
                self.__top1 += 1
            elif pila == 2:
                self.__items[self.__top2] = item
                self.__top2 -= 1
            else:
                print("No existe la pila ingresada")
        else:
            print("Pila llena")
    
    def suprimir1(self):
        if not self.Vacia():
            self.__top1 -= 1
            np.delete(self.__items,self.__top1)
        else:
            print("Pila vacia")
    
    def suprimir2(self):
        if not self.Vacia():
            self.__top2 += 1
            np.delete(self.__items,self.__top2)
    
    def recorrer(self):
        print("--Elementos de la pila: 1--")
        while self.__top1 > 0:
            #self.suprimir1()
            self.__top1 -= 1
            print(self.__items[self.__top1])
        
        print("--Elementos de la pila: 2--")
        while self.__top2 < self.__cantidad-1:
            #self.suprimir2()
            self.__top2 += 1
            print(self.__items[self.__top2])