import numpy as np
class ColaSecuencial:
    __items: np.array
    __top: int #cantidad de elementos en la cola
    __prim: int
    __ult: int
    __cantidad: int #max
    
    def __init__(self,dimension):
        self.__items = np.empty(dimension,dtype=int)
        self.__top = 0
        self.__prim = 0
        self.__ult = 0
        self.__cantidad = dimension
    
    def Vacia(self):
        return self.__top == 0

    def insertar(self,item):
        if self.__top < self.__cantidad:
            self.__items[self.__ult] = item
            self.__ult = (self.__ult+1)%self.__cantidad
            self.__top += 1
        else:
            print("Pila llena")
        
    def suprimir(self):
        x = None
        if not self.Vacia():
            x = self.__items[self.__prim]
            np.delete(self.__items,self.__prim)
            self.__prim = (self.__prim + 1)%self.__cantidad #elimina el primer elemento de la pila
            self.__top -= 1 
        else:
            print("Pila vacia")
        return x
    
    def recorrer(self):
        while not self.Vacia():
            print(self.suprimir())
        """for _ in range(self.__cantidad):
            if not self.Vacia():
                print(self.suprimir())"""


if __name__ == "__main__":
    ColaSecuencial_ = ColaSecuencial(5)
    ColaSecuencial_.insertar(1)
    ColaSecuencial_.insertar(2)
    ColaSecuencial_.insertar(3)
    ColaSecuencial_.insertar(4)
    ColaSecuencial_.suprimir()
    ColaSecuencial_.insertar(10)
    ColaSecuencial_.recorrer()