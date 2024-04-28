"""Dada  la siguiente Narrativa:
La Compañía de Líneas Telefónicas (CLT) está por instalar un cableado telefónico nuevo. Están conectando varios sitios, los
cuales están numerados de 1 a n. Dos sitios nunca comparten un mismo número. Las líneas son bidireccionales, y
cada línea une a dos sitios. En cada sitio, al final de la línea hay un solo teléfono. 
Siempre es posible marcar de un teléfono a otro, aunque no siempre a través de una 
conexión directa (puede pasar por varios sitios). En ocasiones, a un sitio le falla 
el suministro eléctrico y ya no puede conectar. Los directivos de CLT se han dado cuenta 
que puede pasar que no solo ese sitio quede inalcanzable, sino que puede causar que otros 
sitios también los sean. En estos casos, decimos que el sitio (donde ocurrió el fallo) es crítico.
Ahora los directivos quieren contar con un programa que encuentre la cantidad de sitios críticos. 
Se pide:
a) Elija el TAD adecuado
b) Construya un algoritmo que resuelva la problemática planteada 
"""
from GrafoSecuencial import GrafoSecuencial

if __name__ == "__main__":
    vertices = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    adyacencias = [('1', '2'), ('1', '3'), ('1', '4'), ('2', '5'), ('2', '6'), ('3', '7'), ('3', '8'), ('4', '9'), ('4', '10')]

    grafo = GrafoSecuencial(vertices, adyacencias)
    sitios_criticos = []
    
    for vertice in vertices:
        nuevosNodos = vertices.copy()
        nuevosNodos.remove(vertice)
        nuevosAdyacencias = []
        
        for adya in adyacencias:
            if vertice not in adya:
                nuevosAdyacencias.append(adya)

        subGrafo = GrafoSecuencial(nuevosNodos, nuevosAdyacencias)
        if not subGrafo.esConexo():
            sitios_criticos.append(vertice)

    print('Sitios críticos: ')
    print(sitios_criticos)
    print(f'Cantidad de sitios críticos: {len(sitios_criticos)}')

    grafo.grafico(vertices, adyacencias)