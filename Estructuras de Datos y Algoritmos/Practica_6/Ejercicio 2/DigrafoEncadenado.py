from ListaEnlazada import ListaEnlazada

import numpy as np

import networkx as nx

import matplotlib.pyplot as plt


class Registro:
    def __init__(self, nodo, conocido, distancia, camino):
        self.nodo = nodo
        self.conocido = conocido
        self.distancia = distancia
        self.camino = camino

class DigrafoEncadenado:
    __vertices:np.array
    __matrizAdy:np.array
    __pesos:np.array

    def __init__(self,vertices,aristas) -> None:
        self.__vertices = np.array(vertices)
        self.__matrizAdy = np.full(len(vertices),None)
        for i in range(len(self.__matrizAdy)):
            self.__matrizAdy[i] = ListaEnlazada()
        self.__pesos = np.full((len(vertices),len(vertices)),1)
        for arista in aristas:
            i = self.__posVertice(arista[0])
            j = self.__posVertice(arista[1])
            self.__matrizAdy[i].insertar(j)

    
    def getPeso(self,vertice1,vertice2):
        return self.__pesos[self.__posVertice(vertice1)][self.__posVertice(vertice2)]
    
    def setPesos(self,pesos: list):
        for peso in pesos:
            self.__pesos[self.__posVertice(peso[0])][self.__posVertice(peso[1])] = peso[2]
    
    def __posVertice(self,vertice):
        for i in range(len(self.__vertices)):
            if self.__vertices[i] == vertice:
                return i
        raise Exception("Vertice inexistente")

    def mostrar(self):
        for i in range(len(self.__matrizAdy)):
            print(self.__vertices[i], end=": ")
            for j in range(len(self.__matrizAdy)):
                if self.__matrizAdy[i].nodoRelacionado(j):
                    print(self.__vertices[j], end=" ")
            print()

    def adyacentes(self,vertice):
        adyacentes = []
        i = self.__posVertice(vertice)
        for j in range(len(self.__matrizAdy)):
            if self.__matrizAdy[i].nodoRelacionado(j):
                adyacentes.append(self.__vertices[j])
        return adyacentes

    def grado(self,vertice):
        return len(self.adyacentes(vertice))

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

    def __generarCamino(self,vertice1,vertice2):
        visitados = []
        pila = []
        pila.append(vertice1)
        while len(pila) > 0:
            v = pila.pop()
            if v not in visitados:
                visitados.append(v)
                if v == vertice2:
                    return visitados
                ady = self.adyacentes(v)
                for w in ady:
                    if w not in visitados:
                        pila.append(w)
        return None

    def camino(self,vertice1,vertice2):
        self.__posVertice(vertice1)
        self.__posVertice(vertice2)
        camino = self.__generarCamino(vertice1,vertice2)
        if camino == None:
            return "No existe camino"
        else:
            return camino

    def esConexo(self):
        visitados = []
        pila = []
        pila.append(self.__vertices[0])
        while len(pila) > 0:
            v = pila.pop()
            if v not in visitados:
                visitados.append(v)
                for ady in self.adyacentes(v):
                    pila.append(ady)
        return len(visitados) == len(self.__vertices)

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
    
    def caminoMinimo(self,vertice1,vertice2):
        self.__posVertice(vertice1)
        self.__posVertice(vertice2)
        camino = self.dijkstra(vertice1)
        if camino[vertice2] == None:
            return "No existe camino"
        else:
            v = vertice2
            caminoMinimo = []
            while v != None:
                caminoMinimo.append(v)
                v = camino[v].camino
            caminoMinimo.reverse()
            return caminoMinimo

    def verticeSumidero(self,vertice):
        esSumidero = False
        i = 0
        while i < len(self.__vertices) and not esSumidero:
            if vertice in self.adyacentes(self.__vertices[i]):
                esSumidero = True
            i += 1
        return len(self.adyacentes(vertice)) == 0 and esSumidero
    
    def verticeFuente(self,vertice):
        esFuente = True
        i = 0
        while i < len(self.__vertices) and esFuente:
            if vertice in self.adyacentes(self.__vertices[i]):
                esFuente = False
            i += 1
        return len(self.adyacentes(vertice)) > 0 and esFuente
    
    def grafico(self,vertices, adyacencia):
        G = nx.DiGraph()
        G.add_nodes_from(vertices)
        G.add_edges_from(adyacencia)
        nx.draw(G, with_labels=True)
        plt.show()

if __name__ == "__main__":
    vertexs = ["A","B","C","D","E"]
    edges = [("A","B"),("A","C"),("B","D"),("C","D"),("D","E")]
    graph = DigrafoEncadenado(vertexs,edges)
    graph.mostrar()
    print("Nodos adyacentes a A ->",graph.adyacentes("A"))
    print("Grado del vertice A ->",graph.grado("A"))
    print("Recorrido en profundidad desde el vertice A ->",graph.RecorridoProfundidad("A"))
    print("Recorrido en anchura desde el vertice A ->",graph.RecorridoAnchura("A"))
    if graph.camino("A","D"): print("Camino de A a D->",graph.camino("A","D")) 
    else: print("No existe camino")
    print("¿Es conexo?: ",graph.esConexo())
    print("Camino minimo de A a D->",graph.caminoMinimo("A","D"))
    print("¿Es sumidero el vertice E?:",graph.verticeSumidero("E"))
    print("¿Es fuente el vertice A?:",graph.verticeFuente("A"))
    graph.grafico(vertexs,edges)