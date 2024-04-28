import csv
from ClaseJugador import Jugador
import datetime
class ManejadorJugadores:
    __lista: list

    def __init__(self):
        self.__lista=[]

    def cargarJugadores(self):
        archivo=open("Jugadores.csv")
        reader=csv.reader(archivo,delimiter=";")
        next(reader,None)
        for fila in reader:
            self.__lista.append(Jugador(fila[0],fila[1],fila[2],fila[3],fila[4]))
        archivo.close()
    def mostrarjugadores(self):
        for elemento in self.__lista:
            print(elemento)
    def buscaJugador(self,DNI):
        i=0
        pos=-1
        while i<len(self.__lista) and self.__lista[i].getDNI() != DNI:
            i+=1
        if i<len(self.__lista):
            pos=i
        else:
            print("Jugador de DNI'{}' no encontrado...".format(DNI))
        return pos

    def getJugador(self,pos):
        return self.__lista[pos]