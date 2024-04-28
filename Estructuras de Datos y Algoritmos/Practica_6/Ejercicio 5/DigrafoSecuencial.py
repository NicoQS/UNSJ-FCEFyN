import numpy as np

import networkx as nx

import matplotlib.pyplot as plt



"""Defina TAD Digrafo e implemente todas las operaciones vistas en teoría y determine la complejidad de cada una de ellas.
a.	Representación secuencial. 
b.	Representación encadenada.
"""

class Registro:
    def __init__(self, nodo, conocido, distancia, camino):
        self.nodo = nodo
        self.conocido = conocido
        self.distancia = distancia
        self.camino = camino

class DigrafoSecuencial:
    __array:np.array
    __cantvertices:int
    __pesos:np.array

    def __init__(self,vertices,aristas) -> None:
        self.__vertices = vertices
        self.__array = np.full((len(self.__vertices),len(self.__vertices)),False)
        self.__pesos = np.full((len(self.__vertices),len(self.__vertices)),1)
        for arista in aristas:
            self.__array[self.__posVertice(arista[0])][self.__posVertice(arista[1])] = True

    def getPeso(self,vertice1,vertice2):
        return self.__pesos[self.__posVertice(vertice1)][self.__posVertice(vertice2)]
    
    def setPesos(self,pesos: list):
        for peso in pesos:
            self.__pesos[self.__posVertice(peso[0])][self.__posVertice(peso[1])] = peso[2]
            self.__pesos[self.__posVertice(peso[1])][self.__posVertice(peso[0])] = peso[2]
    

    def __posVertice(self,vertice):
        for i in range(len(self.__vertices)):
            if self.__vertices[i] == vertice:
                return i
        raise Exception("Vertice inexistente")

    def RecorridoProfundidad(self,vertice):
        visitados = []
        pila = []
        pila.append(vertice)
        while len(pila) > 0:
            v = pila.pop()
            if v not in visitados:
                visitados.append(v)
                for ady in self.adyacentes(v):
                    pila.append(ady)
        return visitados
    
    def RecorridoAnchura(self,vertice):
        visitados = []
        cola = []
        cola.append(vertice)
        while len(cola) > 0:
            v = cola.pop(0)
            if v not in visitados:
                visitados.append(v)
                for ady in self.adyacentes(v):
                    cola.append(ady)
        return visitados

    def camino(self,nodo_inicial,nodo_final):
        visitados = []
        pila = []
        pila.append(nodo_inicial)
        while len(pila) > 0:
            v = pila.pop()
            if v not in visitados:
                visitados.append(v)
                if v == nodo_final:
                    return visitados
                for ady in self.adyacentes(v):
                    pila.append(ady)
        return None

    def adyacentes(self,vertice):
        pos = self.__posVertice(vertice)
        ady = []
        for i in range(len(self.__vertices)):
            if self.__array[pos][i]:
                ady.append(self.__vertices[i])
        return ady

    def grado(self,vertice):
        return len(self.adyacentes(vertice))

    def esConexo(self):
        esConexo = True
        i = 0
        while i < len(self.__vertices) and esConexo:
            if len(self.RecorridoProfundidad(self.__vertices[i])) < len(self.__vertices):
                esConexo = False
            i += 1
        return esConexo

    def mostrar(self):
        print(self.__array)


    def dijkstra(self,verticeOrigen):
        Tabla = {}
        for vertice in self.__vertices:
            Tabla[vertice] = Registro(vertice,False,999999999,None)
        Tabla[verticeOrigen].distancia = 0
        
        for i in range(len(self.__vertices)):
            #Buscar el vertice con menor distancia y que no haya sido visitado
            v = None
            for vertice in self.__vertices:
                if not Tabla[vertice].conocido:
                    if v == None or Tabla[vertice].distancia < Tabla[v].distancia:
                        v = vertice
            Tabla[v].conocido = True
            #Actualizar los registros de los adyacentes
            for w in self.adyacentes(v):
                if Tabla[v].distancia + self.getPeso(v,w) < Tabla[w].distancia:
                    Tabla[w].distancia = Tabla[v].distancia + self.getPeso(v,w)
                    Tabla[w].camino = v
        return Tabla
    
    def caminoMinimo(self,verticeOrigen,verticeDestino):
        Tabla = self.dijkstra(verticeOrigen)
        camino = []
        v = verticeDestino
        while v != None:
            camino.append(v)
            v = Tabla[v].camino
        camino.reverse()
        return camino

    def grafico(self,vertices, adyacencia):
        G = nx.DiGraph()
        G.add_nodes_from(vertices)
        G.add_edges_from(adyacencia)
        nx.draw(G, with_labels=True)
        plt.show()