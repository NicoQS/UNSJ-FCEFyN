import csv
import numpy as np
from numpy import array
from ClaseCamas import cama
class ManejadorCamas:
    __arreglo : array
    def __init__(self):
        self.__arreglo=self.cargar_objetos()
    def cargar_objetos(self):
        lista=[]
        archivo=open("camas.csv")
        reader=csv.reader(archivo,delimiter=";")
        next(reader,None)
        for fila in reader:
            c=cama(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5])
            lista.append(c)
        archivo.close()
        arr=np.array(lista)
        return arr
    def mostrar(self):
        for i in range(len(self.__arreglo)):
            print(self.__arreglo[i])
    def busca(self,nombreap):
        i=0
        while i<len(self.__arreglo) and self.__arreglo[i].get_nom() != nombreap:
            i+=1
        if i < len(self.__arreglo):
            return i
        else:
            return -1
    def alta(self,fecha,pos):
        self.__arreglo[pos].set_alta(fecha)
    def get_id(self,pos):
        return self.__arreglo[pos].get_cama()
    def muestra_paciente(self,pos):
        print("\nPaciente: {}\t\t Cama: {}\t\t Habitacion: {}".format(self.__arreglo[pos].get_nom(),self.__arreglo[pos].get_cama(),self.__arreglo[pos].get_habitacion()))
        print("Diagnostico: {}\t\t Fecha de internacion: {}".format(self.__arreglo[pos].get_diag(),self.__arreglo[pos].get_internacion()))
        print("Fecha de alta: {}".format(self.__arreglo[pos].get_fecha_alt()))
    def listado_internados(self):
        diag=input("Ingrese un diagnostico: ")
        print("Pacientes internados con el diagnostico ingresado")
        for i in range(len(self.__arreglo)):
            if self.__arreglo[i].get_diag() == diag and self.__arreglo[i].get_estado() == True:
                print(self.__arreglo[i])
            else:
                print("El paciente {} no posee el diagnostico ingresado o esta dado de alta...".format(self.__arreglo[i].get_nom()))