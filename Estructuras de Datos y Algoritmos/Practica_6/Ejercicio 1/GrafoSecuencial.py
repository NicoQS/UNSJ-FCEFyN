import numpy as np

import networkx as nx

import matplotlib.pyplot as plt


class Registro:
    def __init__(self, nodo, conocido, distancia, camino):
        self.nodo = nodo
        self.conocido = conocido
        self.distancia = distancia
        self.camino = camino

class GrafoSecuencial:
    __vertices: np.array
    __matrizAdy: np.array
    __pesos: np.array
    
    def __init__(self,vertices: list, aristas: list):
        self.__vertices = np.array(vertices) #type: ignore
        self.__matrizAdy = np.full((len(vertices),len(vertices)),False) #type: ignore
        self.__pesos = np.full((len(vertices),len(vertices)),1) #type: ignore
        
        for arista in aristas:
            i = self.__posVertice(arista[0])
            j = self.__posVertice(arista[1])
            
            self.__matrizAdy[i][j] = True
            self.__matrizAdy[j][i] = True
    
    def getPeso(self,vertice1,vertice2):
        return self.__matrizAdy[self.__posVertice(vertice1)][self.__posVertice(vertice2)]
    
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
        pos = self.__posVertice(vertice)
        ady = []
        for i in range(len(self.__vertices)):
            if self.__matrizAdy[pos][i]:
                ady.append(self.__vertices[i])
        return ady
    
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
                    pila.append(w)
        return None

    def camino(self,vertice1,vertice2):
        try:
            self.__posVertice(vertice1)
            self.__posVertice(vertice2)
            camino = self.__generarCamino(vertice1,vertice2)
            if camino == None:
                return "No existe camino"
            else:
                return camino
        except:
            print("Algun vertice no existe")

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
        try:
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
        except:
            print("Algun vertice no existe")

    def esConexo(self):
        visitados = self.busquedaProfundidad(self.__vertices[0])
        return len(visitados) == len(self.__vertices)
    
    def busquedaProfundidad(self,vertice):
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
    
    def busquedaAmplitud(self,vertice):
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
        print(self.__matrizAdy)
    
    def Aciclico(self):
        visitados = []
        pila = []
        pila.append(self.__vertices[0])
        while len(pila) > 0:
            v = pila.pop()
            if v not in visitados:
                visitados.append(v)
                ady = self.adyacentes(v)
                for w in ady:
                    if w in visitados:
                        return False
                    pila.append(w)
        return True
    
    def grafico(self,vertices, adyacencia):
        G = nx.Graph()
        G.add_nodes_from(vertices)
        G.add_edges_from(adyacencia)
        nx.draw(G, with_labels=True)
        plt.show()

if __name__ == "__main__":
    vertexs = [1,2,3,4]
    edges = [(1,2),(1,3),(2,4),(3,4)]
    graph = GrafoSecuencial(vertexs,edges)
    graph.mostrar()
    print("Nodos adyacentes a 1 ->",graph.adyacentes(1))
    print("Grado del vertice 1 ->",graph.grado(1))
    print("Recorrido en profundidad desde el vertice 1 ->",graph.busquedaProfundidad(1))
    if graph.camino(1,2): print("Camino de 3 a 4->",graph.camino(3,4)) 
    else: print("No existe camino")
    print("¿Es conexo?",graph.esConexo())
    print("Camino minimo de 3 a 4->",graph.caminoMinimo(3,4))
    graph.grafico(vertexs,edges)