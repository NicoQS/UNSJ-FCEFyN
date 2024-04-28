import csv
from ClaseLugar import Lugar
class ManejaLugares:
    __lista: list
    def __init__(self):
        self.__lista=[]
    def cargarLista(self):
        with open('lugaresVac.csv','r',encoding='utf8') as archivo:
            reader=csv.reader(archivo,delimiter=";")
            next(reader,None)
            for fila in reader:
                L=Lugar(fila[0],fila[1])
                self.__lista.append(L)
            archivo.close()