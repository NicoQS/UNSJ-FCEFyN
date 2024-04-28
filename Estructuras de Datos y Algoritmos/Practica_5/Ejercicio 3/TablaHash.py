# Política manejo de colisiones: Encadenamiento

# Función de transformación de claves: Método de plegado

import numpy as np

from ClaseLista import Lista


class TablaHash:
    __dimension: int
    __Tabla: np.array
    __longPrueba: int
    
    def __init__(self,cantidad_claves,usarPrimo=False):
        self.__dimension = int(cantidad_claves/4)
        if usarPrimo:
            self.__dimension = self.__getPrimo(self.__dimension)
        print("Dimension de la tabla: ",self.__dimension)
        self.__Tabla = np.full(self.__dimension,None)
        self.__longPrueba = 0
    
    def insertar(self,valor):
        index = self.__metodoPlegado(valor)
        if self.__Tabla[index] == None:
            self.__Tabla[index] = Lista()
        self.__Tabla[index].insertar(valor)
        
    
    def buscar(self,valor):
        index = self.__metodoPlegado(valor)
        nodo = self.__Tabla[index].buscar(valor)
        if nodo != None:
            return nodo.getDato()
        else:
            return None
    
    def calcularFactorCarga(self):
        total = np.count_nonzero(self.__Tabla != None) #Cuenta el número de elementos no nulos
        print(self.__dimension)
        return (total / self.__dimension)
    
    def getLongPrueba(self):
        return self.__longPrueba
    
    def mostrar(self):
        for i in range(self.__dimension):
            if self.__Tabla[i] != None:
                print("\n[Posición de la tabla",i,"]")
                print("\--Listado de valores--/")
                self.__Tabla[i].recorrer()
    
    def item1(self):
        for i in range(self.__dimension):
            if self.__Tabla[i] != None and self.__Tabla[i].getCantidad() >= 2:
                print("Posición de la tabla:",i)
                #self.__Tabla[i].recorrer()
                print("Cantidad de elementos en la lista: ",self.__Tabla[i].getCantidad())
    
    def getAverage(self):
        count = 0
        average = 0
        for i in range(self.__dimension):
            if self.__Tabla[i] != None:
                count += self.__Tabla[i].getCantidad()
        average = count / self.__dimension
        print("Promedio de elementos por lista: ",average)
        return average

    def item2(self):
        count = 0
        average = self.getAverage()
        for i in range(self.__dimension):
            if self.__Tabla[i] != None:
                if abs(self.__Tabla[i].getCantidad() - average) >= 3 :
                    count += 1
        return count
    
    #Metodos PRIVADOS---------------------------------------------------------
    # FUNCIÓN DE TRANSFORMACIÓN H(K)
    def __metododeDivison(self,valor): #Método de la división (módulo) h(k) = k % m
        return valor % self.__dimension
    
    def __metodoPlegado(self,valor): #Método de plegado
        valores = str(valor)
        result = 0
        #Tomo los valores de a 2
        
        for i in range(0,len(valores),2):
            if i+2 < len(valores):
                result += int(valores[i:i+2])
            else:
                result += int(valores[i:])
        
        if result >= self.__dimension:
            result = self.__metododeDivison(result)
        return result
    
    def __getPrimo(self,numero):
        for i in range(2,numero):
            if numero % i == 0:
                return self.__getPrimo(numero+1)
        return numero