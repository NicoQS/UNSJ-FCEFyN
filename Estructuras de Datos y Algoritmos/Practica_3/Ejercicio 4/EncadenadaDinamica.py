import csv
from os import path
from Designaciones import Designacion

class Nodo:
    __valor:int
    __siguiente:object
    
    def __init__(self,valor):
        self.__valor = valor
        self.__siguiente = None
        
    def getValor(self):
        return self.__valor
    
    def getSiguiente(self):
        return self.__siguiente
    
    def setSiguiente(self,siguiente):
        self.__siguiente = siguiente

class ListaEncadenada():
    __cabeza:Nodo

    def __init__(self) -> None:
        self.__cabeza = None
        archivo = open(path.dirname(__file__) + '/Designaciones.csv', 'r')
        reader = csv.reader(archivo,delimiter=",")
        next(reader)
        for fila in reader:
            designacion = Designacion(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6])
            self.insertar(Nodo(designacion))
    
    def Vacia(self):
        return self.__cabeza == None

    def insertar(self,Nodo):
        if self.Vacia():
            Nodo.setSiguiente(self.__cabeza)
            self.__cabeza = Nodo
        else:
            aux = self.__cabeza
            while aux.getSiguiente() != None:
                aux = aux.getSiguiente()
            aux.setSiguiente(Nodo)
    
    def mostrar(self):
        aux = self.__cabeza
        while aux != None:
            print(aux.getValor().getJusticia())
            aux = aux.getSiguiente()
    
    def mostrarMujeresDesignadas(self, tipoCargo):
        aux = self.__cabeza
        cantmujeres = 0
        anio = self.__cabeza.getValor().getAnio()
        while aux != None:
            if aux.getValor().getAnio() != anio:
                print("La cantidad de mujeres designadas en el año:"+ str(anio) +  " es de: " + str(cantmujeres) + " en el cargo: " + tipoCargo)
                anio = aux.getValor().getAnio()
                cantmujeres = aux.getValor().getCtMujeres()
            elif aux.getValor().getCargo().lower() == tipoCargo.lower():
                cantmujeres += aux.getValor().getCtMujeres()
            aux = aux.getSiguiente()
    
    def itemD(self,materia,cargo, anio):
        aux = self.__cabeza
        ctAgentes = 0
        while aux != None:
            if aux.getValor().getAnio() == anio and aux.getValor().getMateria().lower() == materia.lower() and aux.getValor().getCargo().lower() == cargo.lower():
                ctAgentes += (aux.getValor().getCtMujeres() + aux.getValor().getCtVarones())
            aux = aux.getSiguiente()
        print("La cantidad de Agentes Designados en el año: {}, materia: {}, cargo: {}, es de: {}".format(anio,materia,cargo,ctAgentes))