from DigrafoSecuencial import DigrafoSecuencial


personas = {
    'A': 'Ana',
    'B': 'Belén',
    'C': 'Cecilia',
    'D': 'Daniel',
    'E': 'Ezequiel',
    'F': 'Federico'}

def getCamino(graph,vertice1,vertice2):
    caminoMinimo = graph.caminoMinimo(vertice1,vertice2)
    retorna = ""
    for persona in caminoMinimo:
        retorna += personas[persona] + " -> "
    return retorna[:-4]


if __name__=="__main__":
    vertices=['A', 'B', 'C', 'D', 'E', 'F']
    adyacencias = [('A', 'B'), ('A', 'D'), ('B', 'C'), ('B', 'E'), ('B', 'F'), ('C', 'D'), ('D', 'B'), ('E', 'D'), ('E', 'F'), ('F', 'D'), ('F', 'A')]
    pesos = [('A', 'B', 3), ('A', 'D', 6), ('B', 'C', 1), ('B', 'E', 2), ('B', 'F', 1), ('C', 'D', 2), ('D', 'B', 3), ('E', 'D', 3), ('E', 'F', 2), ('F', 'D', 1), ('F', 'A', 5)]

    graph = DigrafoSecuencial(vertices, adyacencias)
    graph.setPesos(pesos)
    for vertice1 in vertices:
        for vertice2 in vertices:
            if vertice1 != vertice2:
                print()
                print("*|* El camino más corto entre", personas[vertice1], "y", personas[vertice2], "es", getCamino(graph, vertice1, vertice2),"*|*")
                print()
    graph.grafico(vertices, adyacencias)