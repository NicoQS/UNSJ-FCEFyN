import csv
from ClaseEntrega import Entrega
class ManejaEntrega:
    __lista: list
    def __init__(self):
        self.__lista=[]
    def cargarLista(self):
        with open('entrega.csv','r',encoding="utf8") as archivo:
            reader=csv.reader(archivo,delimiter=";")
            next(reader,None)
            for fila in reader:
                E=Entrega(fila[0],fila[1],fila[2],fila[3])
                self.__lista.append(E)
            archivo.close()
    def buscaEntrega(self,ID):
        i=0
        while i<len(self.__lista) and self.__lista[i].getId() != ID:
            i+=1
        if i<len(self.__lista):
            return i
        else:
            return -1
    def apartado4(self,listaID):
        monto=0
        for elemento in self.__lista:
            if elemento.getId() in listaID:
                monto += elemento.getMonto()
        return monto
    def muestraentrega(self):
        for elemento in self.__lista:
            print(elemento)