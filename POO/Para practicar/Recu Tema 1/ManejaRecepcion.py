from ClaseRecibe import Recibe
import numpy as np
import csv
class ManejaRecepcion:
    __arreglo: np.ndarray
    def __init__(self):
        self.__arreglo=self.cargarArreglo()
    def cargarArreglo(self):
        lista_temporal=[]
        with open('recepcion2.csv','r',encoding='utf8') as archivo:
            reader=csv.reader(archivo,delimiter=";")
            next(reader,None)
            for fila in reader:
                R=Recibe(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5])
                lista_temporal.append(R)
            archivo.close()
            arr=np.array(lista_temporal)
            return arr
    def get_Ct(self):
        return len(self.__arreglo)
    def getIDs(self):
        lista=[]
        for i in range(len(self.__arreglo)):
            lista.append(self.__arreglo[i].getID())
        return lista
    def getProd(self,pos):
        return self.__arreglo[pos]
    def buscaMarca(self,mar):
        lista_Id=[]
        for i in range(len(self.__arreglo)):
            if self.__arreglo[i].getMarca() == mar:
                lista_Id.append(self.__arreglo[i].getID())
        if len(lista_Id) != 0:
            return lista_Id
        else:
            return -1
    def apartado3(self,lista):
        lista.sort()
        print("Listado de productos que no fueron reparados ordenados por marca")
        for elemento in lista:
            print(elemento)
    def muestrarecibe(self):
        for i in range(len(self.__arreglo)):
            print(self.__arreglo[i])