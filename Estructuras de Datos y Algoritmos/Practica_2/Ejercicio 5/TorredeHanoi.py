import numpy as np
import os

class Ficha:
    __valor: int

    def __init__(self,valor=0):
        self.__valor = valor
    
    def getValor(self):
        return self.__valor
    
    def __str__(self) -> str:
        return str(self.__valor)

class Torre:
    __items: np.array
    __top: int

    def __init__(self,dimension):
        self.__items = np.empty(dimension,dtype=Ficha)
        self.__top = 0
    
    def insertar(self,ficha):
        if  self.Vacia():
            self.__items[self.__top] = ficha
        
        elif self.getUltimaFicha() >= ficha.getValor():
            self.__items[self.__top] = ficha
        
        else:
            print("No se puede insertar un disco encima de uno mas pequeño")
            raise Exception ("No se puede insertar un disco encima de uno mas pequeño")
        self.__top += 1
    
    def getUltimaFicha(self):
        return self.__items[self.__top-1].getValor()
    
    def obtenerFicha(self,i):
        if self.__top < i:
            return " "
        else:
            return self.__items[i-1]
    
    def Vacia(self):
        return self.__top == 0
    
    def suprimir(self):
        self.__top -= 1
        x = self.__items[self.__top]
        np.delete(self.__items,self.__top)
        return x


    def cantidadDeDiscos(self):
        return self.__top

class Juego:
    __Torres: list
    __cantidadDisc: int

    def __init__(self,ct):
        self.__Torres = [Torre(ct) for _ in range(3)]
        self.__cantidadDisc = ct
        
        for i in range(ct,0,-1):
            self.__Torres[0].insertar(Ficha(i))
    
    def movimientoDisco(self,desde,hacia):
        if not self.__Torres[desde].Vacia():
            ficha = self.__Torres[desde].suprimir()
            self.__Torres[hacia].insertar(ficha)
        else:
            print("No quedan discos en la torre origen")
    
    def __str__(self) -> str:
        string = ""
        for i in range(ct,0,-1):
            string += ("|{}|      |{}|      |{}|\n".format(self.__Torres[0].obtenerFicha(i),self.__Torres[1].obtenerFicha(i),self.__Torres[2].obtenerFicha(i)))
        return string
    
    def termina(self):
        return self.__cantidadDisc == self.__Torres[2].cantidadDeDiscos()

if __name__ == "__main__":
    ct= int(input("Ingrese la cantidad de fichas: "))
    TorreHanoi = Juego(ct)
    movimientos = 0
    while not TorreHanoi.termina():
        print(TorreHanoi)
        
        desde = int(input("Ingrese la torre de origen: "))
        hacia = int(input("Ingrese la torre de destino: "))
        
        os.system('cls')
        TorreHanoi.movimientoDisco(desde-1,hacia-1)
        movimientos += 1
        print("Movimientos {}".format(movimientos))
    print(TorreHanoi)
    print("Movimientos que se pueden realizar: {}".format(2**ct - 1))