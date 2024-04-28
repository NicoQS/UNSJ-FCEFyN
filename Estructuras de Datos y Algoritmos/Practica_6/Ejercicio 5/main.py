from DigrafoSecuencial import DigrafoSecuencial

"""Los vértices del siguiente Dígrafo representan ciudades (Almafuerte, Belén, Córdoba,
Dar-el-Salam, Estambul y Finisterre) y las aristas indican si existe una ruta aérea entre ellas.
Implemente un algoritmo para averiguar cuál sería la forma en la que una persona podría viajar de 
una a otra pasando por la menor cantdad de ciudades intermedias posibles.
"""
ciudades = {
    'A': 'Almafuerte',
    'B': 'Belen',
    'C': 'Cordoba',
    'D': 'Dar-el-Salam',
    'E': 'Estambul',
    'F': 'Finisterre'}

def buscarCiudad(ciudad):
    for vertice in ciudades:
        if ciudades[vertice].lower() == ciudad.lower():
            return vertice
    return None

def getCamino(graph,vertice1,vertice2):
    caminoMinimo = graph.caminoMinimo(vertice1,vertice2)
    retorna = ""
    for ciudad in caminoMinimo:
        retorna += ciudades[ciudad] + " -> "
    return retorna[:-4]

if __name__ == "__main__":
    vertices = ['A', 'B', 'C', 'D', 'E', 'F']
    adyacencias = [('A', 'B'), ('A', 'D'), ('B', 'C'), ('B', 'E'), ('B', 'F'), ('C', 'D'), ('D', 'B'), ('E', 'D'), ('E', 'F'), ('F', 'D'), ('F', 'A')]
    ciudad_inicio = buscarCiudad(input("Ingrese ciudad de inicio(Almafuerte, Belen, Cordoba,Dar-el-Salam, Estambul y Finisterre): "))
    ciudad_destino = buscarCiudad(input("Ingrese ciudad de destino(Almafuerte, Belen, Cordoba,Dar-el-Salam, Estambul y Finisterre): "))
    digrafo = DigrafoSecuencial(vertices, adyacencias)
    print("El camino más corto entre", ciudades[ciudad_inicio], "y", ciudades[ciudad_destino], "es", getCamino(digrafo, ciudad_inicio, ciudad_destino))
    digrafo.grafico(vertices, adyacencias)