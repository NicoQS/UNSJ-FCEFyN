from ClaseCalefactorGas import CalefactorGas
from ClaseCalefactorElectrico import CalefactorElectrico
from ClaseCalefactor import Calefactor
import csv
import numpy as np
class ManejadorCalefactores:
    __calefactores: np.array

    def __init__(self):
        self.__calefactores=np.empty(0,dtype=Calefactor)

    def agregarCalefactor(self,calefactor):
        self.__calefactores = np.append(self.__calefactores,calefactor)

    def cargaElectricos(self):
        with open('calefactor-electrico.csv','r',encoding="utf8") as archivo:
            reader=csv.reader(archivo,delimiter=";")
            next(reader, None)
            for fila in reader:
                C=CalefactorElectrico(fila[0],fila[1],fila[2])
                self.agregarCalefactor(C)
            archivo.close()

    def cargaGas(self):
        with open('calefactor-a-gas.csv','r',encoding="utf8") as archivo:
            reader=csv.reader(archivo,delimiter=";")
            next(reader,None)
            for fila in reader:
                C=CalefactorGas(fila[0],fila[1],fila[2],fila[3])
                self.agregarCalefactor(C)
            archivo.close()

    def item_1(self,c,h):
        pos=-1
        min=99999999
        for i in range(len(self.__calefactores)):
            if type(self.__calefactores[i]) is CalefactorGas:
                costo=(self.__calefactores[i].getCalorias()/1000)*c*h
                if costo < min:
                    min=costo
                    pos=i
        return pos
    def item_2(self,c,h):
        pos=-1
        min=99999999
        for i in range(len(self.__calefactores)):
            if type(self.__calefactores[i]) is CalefactorElectrico:
                costo=(self.__calefactores[i].getPotencia()/1000)*c*h
                if costo < min:
                    min=costo
                    pos=i
        return pos
    def item_3(self,c,h):
        pos1=-1
        pos2=-1
        min1=9999999
        min2=9999999
        costo1=None
        costo2=None
        for i in range(len(self.__calefactores)):
            if type(self.__calefactores[i]) is CalefactorElectrico:
                costo1=(self.__calefactores[i].getPotencia()/1000)*c*h
                if costo1 < min1:
                    min1=costo1
                    pos1=i
            elif type(self.__calefactores[i]) is CalefactorGas:
                costo2 = (self.__calefactores[i].getCalorias() / 1000) * c * h
                if costo2 < min2:
                    min2 = costo2
                    pos2 = i
        if costo1 < costo2:
            print("Tipo: {}, Calefactor: {}".format(self.__calefactores[pos1].getTipoE(),self.__calefactores[pos1]))
        else:
            print("Tipo: {}, Calefactor: {}".format(self.__calefactores[pos2].getTipoG(), self.__calefactores[pos2]))
    def opciones(self,op,c,h):
        if op == 1:
            posgas=self.item_1(c,h)
            print("El calefactor a gas de menor consumo es el de marca {} y modelo {}.".format(self.__calefactores[posgas].getMarca(),self.__calefactores[posgas].getModelo()))

        elif op == 2:
            poselec=self.item_2(c,h)
            print("El calefactor electrico de menor consumo es el de marca {} y modelo {}.".format(self.__calefactores[poselec].getMarca(), self.__calefactores[poselec].getModelo()))

        elif op == 3:
            self.item_3(c,h)