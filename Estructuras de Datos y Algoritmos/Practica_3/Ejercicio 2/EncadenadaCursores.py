import numpy as np

class Nodo:
    __valor: int
    __siguiente: int

    def __init__(self, valor,siguiente = None):
        self.__valor = valor
        self.__siguiente = siguiente

    def getValor(self):
        return self.__valor

    def setValor(self, valor):
        self.__valor = valor

    def getSiguiente(self):
        return self.__siguiente

    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente

class EncadenadaCursor():
    __inicio:int
    __iniciovacia:int
    __items:Nodo
    __cantidadElem:int
    
    def __init__(self,dimension) -> None:
        self.__items=np.empty(dimension,dtype=Nodo)
        self.__inicio = -1
        self.__iniciovacia = 0
        self.__cantidadElem = 0

        for i in range(dimension - 1):
            self.__items[i] = Nodo(None,i+1)
        self.__items[dimension - 1] = Nodo(None,-1)

    def Vacia(self):
        return self.__inicio == -1
    
    def posValida(self,pos):
        return pos >= 0 and pos-1 < self.__cantidadElem

    def insertar(self, valor, posicion):
        if self.Vacia():
            self.__inicio = posicion
            self.__items[self.__inicio] = Nodo(valor)
            self.__items[self.__inicio].setSiguiente(-1)
            self.__iniciovacia += 1
        else:
            if self.posValida(posicion):
                aux = self.__inicio
                while self.__items[aux].getSiguiente() != -1 and aux != posicion:
                    aux = self.__items[aux].getSiguiente()
                if aux != posicion:
                    self.__items[self.__iniciovacia] = Nodo(valor)
                    self.__items[self.__iniciovacia].setSiguiente(self.__items[aux].getSiguiente()) 
                    self.__items[aux].setSiguiente(self.__iniciovacia) 
                else:
                    self.__items[aux].setValor(valor)
                self.__iniciovacia += 1
            else:
                print("Posicion no valida")
        self.__cantidadElem += 1

    def eliminar(self,posicion):
        if self.Vacia():
            raise Exception("Lista vacia")
        elif not self.posValida(posicion):
            raise Exception("Posicion no valida")
        else:
            if posicion == 0:
                aux = self.__inicio
                self.__inicio = self.__items[aux].getSiguiente()
                self.__items[aux].setSiguiente(self.__iniciovacia)
                self.__iniciovacia = aux
            else:
                aux = self.__inicio
                while self.__items[aux].getSiguiente() != posicion:
                    aux = self.__items[aux].getSiguiente()
                Nodoanterior = self.__items[aux]
                aux = Nodoanterior.getSiguiente()
                Nodoanterior.setSiguiente(self.__items[aux].getSiguiente())
                self.__items[aux].setSiguiente(self.__iniciovacia)
                self.__iniciovacia = aux
    
    def getPrimero(self):
        if self.Vacia():
            return None
        else:
            return self.__items[self.__inicio].getValor()

    def getUltimo(self):
        if self.Vacia():
            return None
        else:
            aux = self.__inicio
            while self.__items[aux].getSiguiente() != -1 :
                aux = self.__items[aux].getSiguiente()
            return self.__items[aux].getValor()

    def recuperarArreglo(self,pos):
        aux = self.__inicio
        while aux != -1 and aux != pos:
            aux=self.__items[aux].getSiguiente()
        if aux == pos:
            return self.__items[aux]
        else:
            return None

    def recuperar(self,posicion):
        aux = self.__inicio
        while aux != -1 and aux != posicion:
            aux=self.__items[aux].getSiguiente()
        if aux == posicion:
            return self.__items[aux].getValor()
        else:
            return None

    def buscar(self,valor):
        aux = self.__inicio
        while aux != -1 and self.__items[aux].getValor() != valor:
            aux=self.__items[aux].getSiguiente()
        return aux

    def mostrar(self):
        aux = self.__inicio
        cadena=""
        while aux != -1:
            cadena += str(self.__items[aux].getValor()) + " "
            print(self.__items[aux].getValor())
            aux = self.__items[aux].getSiguiente()
        print("[ "+cadena+"]")

if __name__=="__main__":
    lista = EncadenadaCursor(4)
    lista.insertar(1,0)
    lista.insertar(2,1)
    lista.insertar(5,2)
    lista.insertar(10,3)
    lista.insertar(6,0)
    lista.eliminar(0)
    lista.eliminar(3)
    lista.mostrar()
    print("El dato es :{}".format(lista.recuperar(1)))
    print("El dato se encuentra en la posicion :{}".format(lista.buscar(2)))