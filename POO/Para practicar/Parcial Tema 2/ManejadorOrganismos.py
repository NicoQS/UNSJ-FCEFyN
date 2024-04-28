import csv
from ClaseOrganos import Organo
class ManejadorOrganismos:
    __lista: list
    def __init__(self):
        self.__lista=[]
    def cargarLista(self):
            with open('Organismos-del-Estado.csv', 'r',encoding='latin-1') as archivo:
                reader=csv.reader(archivo,delimiter=";")
                next(reader,None)
                for  fila in reader:
                    O=Organo(fila[0],fila[1],fila[2],fila[3])
                    self.__lista.append(O)
                archivo.close()
    def nombreOrgas(self):
        lista=[]
        for elemento in self.__lista:
            lista.append(elemento.getNomorg())
        return lista