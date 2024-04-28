import numpy as np
from ClaseProducto import Producto
import csv
class ManejaProductos:
    __arreglo: np.ndarray
    def __init__(self):
        self.__arreglo=self.cargarArreglo()
    def cargarArreglo(self):
        lista_temporal=[]
        with open('Productos.csv','r',encoding='latin-1') as archivo:
            reader=csv.reader(archivo,delimiter=";")
            next(reader,None)
            for fila in reader:
                P=Producto(fila[0],fila[1],fila[2])
                lista_temporal.append(P)
            archivo.close()
            arr=np.array(lista_temporal)
            return arr
    def getProd(self,pos):
        return self.__arreglo[pos]
    def getCt(self):
        return len(self.__arreglo)
    def getID(self,pos):
        return self.__arreglo[pos].getCode()
    def ordenaporDescripcion(self):
        self.__arreglo.sort()
    def getDesc(self,pos):
        return self.__arreglo[pos].getDescrip()
    def mostrarDes(self):
        for i in range(len(self.__arreglo)):
            print(self.__arreglo[i].getDescrip())