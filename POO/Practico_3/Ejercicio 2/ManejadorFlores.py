import csv
import numpy as np
from ClaseFlores import Flor
class ManejaFlores:
    __arreglo: np.array
    def __init__(self):
        self.__arreglo=self.carga_arr()
    def carga_arr(self):
        with open('Flores.csv', 'r', encoding='utf8') as archivo:
            lista_temp=[]
            reader=csv.reader(archivo,delimiter=";")
            for fila in reader:
                F=Flor(fila[0],fila[1],fila[2],fila[3])
                lista_temp.append(F)
            arr=np.array(lista_temp)
            archivo.close()
            return arr
    def get_Ct(self):
        return len(self.__arreglo)
    def mostrar_flores(self):
        print(len(self.__arreglo))
        for i in range(len(self.__arreglo)):
            print(self.__arreglo[i])
    def mostrar_flor(self,pos):
        print("--Nombre: {}, Numero: {}, Color: {}--".format(self.__arreglo[pos].getNom(),self.__arreglo[pos].getNum(),self.__arreglo[pos].getCol()))
    def get_flor(self,pos):
        return self.__arreglo[pos]