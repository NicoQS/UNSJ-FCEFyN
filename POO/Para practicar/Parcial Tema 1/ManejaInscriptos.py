import csv
from ClaseInscripto import Inscripto
import numpy as np
class ManejaInscripto:
    __arreglo: np.ndarray
    def __init__(self):
        self.__arreglo=self.cargaArreglo()
    def cargaArreglo(self):
        lista_temporal=[]
        with open('inscriptos20210503.csv','r',encoding='utf8') as archivo:
            reader=csv.reader(archivo,delimiter=";")
            next(reader,None)
            for fila in reader:
                I=Inscripto(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6])
                lista_temporal.append(I)
            archivo.close()
            arr=np.array(lista_temporal)
            return arr
    def apartado3(self):
        lista_edades=[]
        for i in range(len(self.__arreglo)):
            if self.__arreglo[i].getEdad() not in lista_edades:
                lista_edades.append(self.__arreglo[i].getEdad())
        for i in range(len(lista_edades)):
            ctRiesgo=0
            ctSinRiesgo=0
            for j in range(len(self.__arreglo)):
                if self.__arreglo[j].getEdad() == lista_edades[i]:
                    if self.__arreglo[j].getFactor() != "Ninguno":
                        ctRiesgo+=1
                    else:
                        ctSinRiesgo+=1
            print("Para la edad {}, la cantidad de personas con factores de riesgo es {} y sin factor de riesgo es {}".format(lista_edades[i],ctRiesgo,ctSinRiesgo))
    def calcula_priori(self):
        for i in range(len(self.__arreglo)):
            priori=0
            factor=self.__arreglo[i].getFactor()
            if factor == "Diabetes" or factor == "Obesidad":
                priori+=50
            elif factor == "Cardiovascular" or factor == "Renal"  or factor == "Respiratoria":
                priori+=50
            elif factor == "Cirrosis" or factor == "HIV":
                priori+=30
            self.__arreglo[i].prioridad(priori)
    def apartado4(self):
        self.calcula_priori()
        Z=input("Ingrese el nombre de una Zona: ")
        lista_por_zona=[]
        for i in range(len(self.__arreglo)):
            if self.__arreglo[i].getZona() == Z:
                lista_por_zona.append(self.__arreglo[i])
        lista_por_zona.sort(reverse=True)
        print("--Personas ordenadas por factor de prioridad--")
        for elemento in lista_por_zona:
            print(elemento)