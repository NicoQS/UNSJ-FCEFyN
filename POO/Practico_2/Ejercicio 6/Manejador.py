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

    def funcion1(self):
        maxx = self.__lista[0]
        for elemento in self.__lista:
            if elemento > maxx:
                maxx = elemento.cantidadTotaldeMillas()
        print("APARTADO --1--")
        print("Viajeros con mayor millas acumuladas")
        for elemento in self.__lista:
            if elemento.cantidadTotaldeMillas() == maxx:
                elemento.mostrar()

    def funcion2_3(self):
        print("--APARTADO 2 Y 3--")
        viajero = self.__lista[0]
        viajero.mostrar()
        viajero += 1000
        print("Se acumulan nuevas millas")
        viajero.mostrar()
        print("Se realiza un canje de millas")
        viajero -= 2500
        viajero.mostrar()