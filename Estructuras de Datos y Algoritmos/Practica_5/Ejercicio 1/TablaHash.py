import numpy as np
import random

# Política manejo de colisiones: Direccionamiento abierto

# Función de transformación de claves: Método de la división

# Procesamiento de claves sinónimas: Secuencia de prueba lineal

class TablaHash:
    __dimension: int
    __Tabla: np.array
    __longPrueba: int
    
    def __init__(self,cantidad_claves,usarPrimo=False):
        self.__dimension = cantidad_claves
        
        if usarPrimo:
            self.__dimension = self.__getPrimo(int(self.__dimension/0.7) + 1)
        
        self.__Tabla = np.full(self.__dimension,None)
        self.__longPrueba = 0
    
    def insertar(self,valor):
        index = self.__PruebaLineal(valor)
        
        if index != -1:
            self.__Tabla[index] = valor
        else:
            #Peor caso: recorrer todo el arreglo y no encontrar posición disponible
            print("Tabla llena, no es posible almacenar la clave")
    
    def buscar(self,valor):
        index = self.__PruebaLineal(valor)
        if index != -1:
            return self.__Tabla[index]
        else:
            return None
    
    def calcularFactorCarga(self):
        total = np.count_nonzero(self.__Tabla != None) #Cuenta el número de elementos no nulos
        print(self.__dimension)
        return (total / self.__dimension)
    
    def getLongPrueba(self):
        return self.__longPrueba
    
    #Metodos Auxiliares---------------------------------------------------------
    # FUNCIÓN DE TRANSFORMACIÓN H(K)
    def __metododeDivison(self,valor): #Método de la división (módulo) h(k) = k % m
        return valor % self.__dimension
    
    
    # POLÍTICA DE MANEJO DE COLISIONES
    def __PruebaLineal(self,valor): #Secuencia de prueba lineal - Retorna la posición donde se debe almacenar la clave
        IndexOrigen = index = self.__metododeDivison(valor)
        self.__longPrueba = 0
        
        while self.__Tabla[index] != None and self.__Tabla[index] != valor:
            self.__longPrueba += 1
            index = (index + 1) % self.__dimension
            
            if index == IndexOrigen:
                return -1 #Tabla llena
        
        return index
    
    
    def __getPrimo(self,numero):
        for i in range(2,numero):
            if numero % i == 0:
                return self.__getPrimo(numero+1)
        return numero