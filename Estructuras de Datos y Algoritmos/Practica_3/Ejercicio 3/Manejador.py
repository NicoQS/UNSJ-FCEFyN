import csv

from os import path

from ListaEncadenadaOrdenada import EncadenadaPosicion, Nodo


class Manejador:
    __lista: EncadenadaPosicion
    
    def __init__(self) -> None:
        self.__lista = EncadenadaPosicion()
        self.procesaCSV()
    
    def procesaCSV(self):
        archivo = open(path.dirname(__file__) +'/SuperficieIncendios.csv')
        reader = csv.reader(archivo, delimiter=';')
        provincia = ""
        hectareas = 0 
        for linea in reader:
            if provincia != linea[3]:
                hectareas = float(linea[6])
                self.__lista.insert(Nodo(linea[3],hectareas))
                provincia = linea[3]
            else:
                hectareas += float(linea[6])

    def itemB(self):
        """b)Mostrar, Nombre de provincia y superficie afectada ordenada de mayor a menor por superficie total afectada. """
        self.__lista.mostrar()