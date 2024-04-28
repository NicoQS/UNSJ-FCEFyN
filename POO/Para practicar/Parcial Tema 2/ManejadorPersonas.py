from ClasePersonal import Persona
import numpy as np
import csv
class ManejadorPersonas:
    __arreglo: np.ndarray
    def __init__(self):
        self.__arreglo=self.cargaArreglo()
    def cargaArreglo(self):
        lista_temporal=[]
        with open('Personal-exceptuado.csv', 'r', encoding='latin-1') as archivo:
            reader=csv.reader(archivo,delimiter=";")
            next(reader,None)
            for fila in reader:
                P=Persona(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7])
                lista_temporal.append(P)
            archivo.close()
            arr=np.array(lista_temporal)
            return arr
    def apartado3(self,nomOrg):
        ct1=0
        ct2=0
        for i in range(len(self.__arreglo)):
            if self.__arreglo[i].getOrga() == nomOrg:
                if self.__arreglo[i].getEdad() < 60 and self.__arreglo[i].getFactor() != "Edad":
                    ct1+=1
                elif self.__arreglo[i].getEdad() > 59 and self.__arreglo[i].getFactor() == "Edad":
                    ct2+=1
        print("Personas menores de 60 anios y con enfermedades pre-existentes: {}".format(ct1))
        print("Personas mayores de 59 anios, factor de riesgo (Edad): {}".format(ct2))
    def apartado4(self,nomOrg):
        listado=[]
        for i in range(len(self.__arreglo)):
            if self.__arreglo[i].getOrga() == nomOrg and self.__arreglo[i].getEdad() < 60 and self.__arreglo[i].getFactor() != "Edad":
                listado.append(self.__arreglo[i])
        listado.sort()
        print("--Organizacion: {}--".format(nomOrg))
        print("--Listado de personas ordenado alfabeticamente--")
        for elemento in listado:
            if elemento.getEdad() < 60:
                print(elemento)