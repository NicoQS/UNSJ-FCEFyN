import csv
from ClaseProyectos import Proyecto
class ManejadorProyectos:
    __lista : list
    def __init__(self):
        self.__lista=[]
    def carga_lista(self):
        with open('proyectos.csv', 'r', encoding='utf8') as archivo:
            reader=csv.reader(archivo,delimiter=";")
            next(reader,None)
            for fila in reader:
                P=Proyecto(fila[0],fila[1],fila[2])
                self.__lista.append(P)
            archivo.close()
    def mostrar_proy(self):
        for elemento in self.__lista:
            print(elemento)
    def puntaje(self,pos,ct):
        self.__lista[pos].puntos(ct)
    def ordenamiento(self):
        self.__lista.sort(reverse=True)
        print("Proyectos ordenados por puntaje de mayor a menor, segun las reglas del negocio")
        self.mostrar_proy()
    def IDs (self):
        lista=[]
        for elemento in self.__lista:
            lista.append(elemento.get_ID())
        return lista
