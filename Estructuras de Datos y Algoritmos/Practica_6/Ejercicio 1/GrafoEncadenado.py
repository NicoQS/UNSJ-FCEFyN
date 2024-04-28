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

class GrafoEncadenado:
    __vertices: np.array
    __matrizAdy: np.array
    __pesos: np.array
    
    def __init__(self,vertices: list, aristas: list):
        self.__vertices = np.array(vertices) 
        self.__matrizAdy = np.full(len(vertices),None)
        for i in range(len(self.__matrizAdy)):
            self.__matrizAdy[i] = ListaEnlazada()
        self.__pesos = np.full((len(vertices),len(vertices)),1) 
        for arista in aristas:
            i = self.__posVertice(arista[0])
            j = self.__posVertice(arista[1])
            
            self.__matrizAdy[i].insertar(j)
            self.__matrizAdy[j].insertar(i)
    
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

    def adyacentes(self,vertice):
        posNodo = self.__posVertice(vertice)
        adyacentes = []
        for i in range(len(self.__vertices)):
            if self.__matrizAdy[posNodo].nodoRelacionado(i):
                adyacentes.append(self.__vertices[i])
        return adyacentes

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
        #print("Algun vertice no existe")

    def esConexo(self):
        visitados = self.RecorridoProfundidad(self.__vertices[0])
        return len(visitados) == len(self.__vertices)
    
    def RecorridoProfundidad(self,vertice):
        visitados = []
        pila = []
        pila.append(vertice)
        while len(pila) > 0:
            v = pila.pop()
            if v not in visitados:
                visitados.append(v)
                ady = self.adyacentes(v)
                for w in ady:
                    pila.append(w)
        return visitados
    
    def RecorridoAmplitud(self,vertice):
        visitados = []
        cola = []
        cola.append(vertice)
        while len(cola) > 0:
            v = cola.pop(0)
            if v not in visitados:
                visitados.append(v)
                ady = self.adyacentes(v)
                for w in ady:
                    cola.append(w)
        return visitados
    
    def grado(self,vertice):
        return len(self.adyacentes(vertice))
    
    def mostrar(self):
        for i in range(len(self.__matrizAdy)):
            print(self.__vertices[i], end=": ")
            for j in range(len(self.__matrizAdy)):
                if self.__matrizAdy[i].nodoRelacionado(j):
                    print(self.__vertices[j], end=" ")
            print()
    
    def grafico(self,vertices, adyacencia):
        G = nx.Graph()
        G.add_nodes_from(vertices)
        G.add_edges_from(adyacencia)
        nx.draw(G, with_labels=True)
        plt.show()

if __name__ == "__main__":
    vertices = ["A","B","C","D","E"]
    adyacencia = [("A","B"),("B","C"),("B","E"),("C","D"),("C","E"),("D","E")]
    grafo = GrafoEncadenado(vertices,adyacencia)
    print(grafo.camino("A","E"))
    print("EL recorido en profundidad es: ",grafo.RecorridoProfundidad("A"))
    print("El recorido en amplitud es: ",grafo.RecorridoAmplitud("A"))
    print("¿Es Conexo?",grafo.esConexo())
    if grafo.camino("B","D"): print("Camino de B a D->",grafo.camino("B","D")) 
    else: print("No existe camino")
    print("El grado del vertice A es: ",grafo.grado("A"))
    print("El camino minimo entre B y D es: ",grafo.caminoMinimo("B","D"))
    grafo.grafico(vertices, adyacencia)