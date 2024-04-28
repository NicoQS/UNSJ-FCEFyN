import csv
from ClaseViajero import Viajero
class Manejador:
    __lista : list[Viajero]
    def __init__(self):
        self.__lista=[]
    def cargarobjetos(self):
        archivo=open("Viajeros.csv")
        reader=csv.reader(archivo,delimiter=",")
        next(reader,None)
        for fila in reader:
            obj=Viajero(fila[0],fila[1],fila[2],fila[3],fila[4])
            self.__lista.append(obj)
        archivo.close()
    def funcion_1_2_3(self):
        v = self.__lista[0]
        print("--Por izquierda--")
        print("{} == 2500".format(v))
        print(v == 2500)
        print("--Por derecha--")
        print("2500 == {}".format(v))
        print(2500 == v)
        print("Comparacion entre Objetos")
        print("{} == {}".format(v,self.__lista[1]))
        print(v == self.__lista[1])
        print("Entre otros objetos")
        print("{} == {}".format(v, self.__lista[2]))
        print(v == self.__lista[2])
        print("--APARTADO 2 Y 3--")
        v.mostrar()
        v = 1000 + v
        print("Se acumulan nuevas millas")
        v.mostrar()
        print("Se realiza un canje de millas")
        v = 2500 - v
        v.mostrar()