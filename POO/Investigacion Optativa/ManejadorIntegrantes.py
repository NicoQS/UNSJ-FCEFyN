import numpy as np
from ClaseIntegrantes import Integrante
import csv
class ManejadorIntegrantes:
    __arreglo: np.ndarray
    def __init__(self):
        self.__arreglo=self.carga_arreglo()
    def carga_arreglo(self):
        lista=[]
        with open('integrantesProyecto.csv', 'r', encoding='utf8') as archivo:
            reader=csv.reader(archivo,delimiter=";")
            next(reader,None)
            for fila in reader:
                I=Integrante(fila[0],fila[1],fila[2],fila[3],fila[4])
                lista.append(I)
            archivo.close()
            arr=np.array(lista)
        return arr
    def mostrar_inte(self):
        for i in range(len(self.__arreglo)):
            print(self.__arreglo[i])
    def Ct_Integrantes(self,id):
        ct=0
        for i in range(len(self.__arreglo)):
            if self.__arreglo[i].get_ID_int() == id and self.__arreglo[i].get_rol() == "integrante":
                ct+=1
        return ct
    def buscaDir_cat(self,id):
        i=0
        band="No-cate"
        while i<len(self.__arreglo) and band=="No-cate":
            cate=self.__arreglo[i].get_cat()
            dire=self.__arreglo[i].get_rol()
            if (self.__arreglo[i].get_ID_int() == id) and (dire == "director"):
                band=cate
            else:
                i+=1
        return band
    def buscaCodir_cat(self,id):
        i=0
        band="No-cate"
        while i<len(self.__arreglo) and band=="No-cate":
            cate=self.__arreglo[i].get_cat()
            dire=self.__arreglo[i].get_rol()
            if (self.__arreglo[i].get_ID_int() == id) and (dire == "codirector"):
                band=cate
            else:
                i+=1
        return band