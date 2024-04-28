import numpy as np
from ClaseEquipo import Equipo
import csv
class ManejadorEquipos:
    __equipos : np.array

    def __init__(self):
        self.__equipos = np.empty(0,dtype=Equipo)

    def agregarEquipo(self,equipo):
        self.__equipos = np.append(self.__equipos,equipo)

    def mostrarEquipos(self):
        for i in range(len(self.__equipos)):
            print(self.__equipos[i])

    def cargarEquipos(self):
        archivo=open("Equipos.csv")
        reader=csv.reader(archivo,delimiter=";")
        fila=next(reader)
        cantidad=int(fila[0])
        for i in range(cantidad):
            fila=next(reader)
            E=Equipo(fila[0],fila[1])
            self.agregarEquipo(E)
        archivo.close()

    def buscaEquipo(self,nombre):
        i=0
        pos=-1
        band=False
        while i<len(self.__equipos) and not band:
            equipo=self.__equipos[i]
            if equipo.getNombre() == nombre:
                pos=i
                band=True
            i+=1
        if i>len(self.__equipos):
            print("Equipo '{}' no encontrado...".format(nombre))
        return pos

    def getEquipo(self,pos):
        return self.__equipos[pos]
