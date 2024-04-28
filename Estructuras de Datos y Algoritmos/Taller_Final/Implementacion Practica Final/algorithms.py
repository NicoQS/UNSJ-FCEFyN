from abc import ABC, abstractmethod

from puzzle import Puzzle


class Estrategia(ABC):
    """
    Propiedades de performance de las diferentes estrategias para resolver el puzzle
    """

    num_nodos_expandidos = 0  #cuántos nodos en el árbol de búsqueda necesitan expandirse los algoritmos para resolver el rompecabezas
    solucion = None  # la secuencia de operaciones para resolver el rompecabezas

    @abstractmethod
    def resolver_puzzle(self):
        """
        El algoritmo para resolver el puzzle
        :return: Lista con objetos de puzzle
        """
        raise NotImplemented


"""class FIFO(Estrategia):
    start = None  # Puzzle
    
    def __init__(self, puzzleInicial):
        
        #:param puzzleInicial: Puzzle
        
        self.start = puzzleInicial

    def __str__(self):
        return 'Estrategia FIFO'

    def resolver_puzzle(self):
        cola = [[self.start]]  # Lista de listas con objeto de puzzle. Cada sublista es un camino explorado
        camino = []  # El camino que queremos explorar
        expancion = []  # Posiciones ya exploradas
        num_nodos_expandidos = 0  # contador usado para el analisis de la performance

        while cola:
            camino = cola[0]  # toma el primer camino - lista de objetos puzzle
            cola.pop(0)  # cola (FIFO)
            nodo_final = camino[-1]  # la ultima posicion en el camino explorado

            if nodo_final.posicion in expancion:  # evitar loop infinito
                continue

            for movimiento in nodo_final.get_movimientos():  # loop a traves de todos los posibles movimientos para la posicion actual
                if movimiento.posicion in expancion:  # evitar loop infinito
                    continue
                cola.append(camino + [movimiento])  # agrega el camino con las nuevas posiciones al final de la cola

            expancion.append(nodo_final.posicion)  # todos los movimientos para estas posiciones estan ahora en la cola
            num_nodos_expandidos += 1

            if nodo_final.posicion == nodo_final.POSICION_FINAL_PUZZLE:  # la ultima posicion en nuestro camino es la posicion final
                break

        # setea los valores de la clase base
        self.num_nodos_expandidos = num_nodos_expandidos  # incrementa el contador de performance
        self.solucion = camino"""


class AEstrella(Estrategia):
    HALLAR_DISTANCIA_MANHATTAN, HALLAR_FUERADELUGAR = 'hallar_distancia_de_manhattan', 'Hallar_fuera_de_Lugar'
    CONSTANTES_HEURISTICAS = [HALLAR_DISTANCIA_MANHATTAN, HALLAR_FUERADELUGAR]

    #funciones que se pueden seleccionar para calcular el valor heuristico
    hallar_funciones = {
        HALLAR_DISTANCIA_MANHATTAN: Puzzle.hallar_distancia_de_manhattan.__name__,
        HALLAR_FUERADELUGAR: Puzzle.Hallar_fuera_de_Lugar.__name__
    }

    def __init__(self, puzzle_inicial, heuristic=None):
        """
        :param puzzle_inicial: Puzzle
        :param heuristic: 'distancia de manhattan' (default) or 'fuera de lugar'
        """
        self.start = puzzle_inicial
        self.hallar_funcion = self.hallar_funciones[self.HALLAR_DISTANCIA_MANHATTAN]
        if heuristic:
            if heuristic not in self.CONSTANTES_HEURISTICAS:
                raise RuntimeError(f'Nombre de funcion heuristica invalido. Debe ser {self.CONSTANTES_HEURISTICAS}')
            self.hallar_funcion = self.hallar_funciones[heuristic]

    def __str__(self):
        return 'Estrategia con Algoritmo A*'

    def _calcular_nueva_heuristica(self, movimiento, nodo_final):
        """
        Heuristica que calcula que tan bueno es el movimiento actual
        :param movimiento: Puzzle
        :param nodo_final: Puzzle
        :return: valor heuristico (entero)
        """
        return getattr(movimiento, self.hallar_funcion)() - getattr(nodo_final, self.hallar_funcion)()

    def resolver_puzzle(self):
        # Cada sublista en la cola es un camino a ser explorado y es el primer elemento del camino
        # es el total heuristico (int) para el camino
        cola = [[getattr(self.start, self.hallar_funcion)(), self.start]]
        camino = []  # el camino actual que queremos explorar
        expandido = []  # Posiciones ya exploradas
        num_nodos_expandidos = 0  # contador usado para el analisis de la performance

        while cola:
            # encuentra que camino en la cola tiene el menor valor heuristico
            i = 0
            for j in range(1, len(cola)):
                if cola[i][0] > cola[j][0]:  # minimo coste
                    i = j

            camino = cola[i]  # toma el camino con el menor valor heuristico
            cola = cola[:i] + cola[i + 1:]  # elimina el camino de la cola
            nodo_final = camino[-1]  # La ultima posicion en el camino que estamos explorando

            if nodo_final.posicion == nodo_final.POSICION_FINAL_PUZZLE:  # la ultima posicion de nuestro camino es la ultima posicion
                break
            if nodo_final.posicion in expandido:  # evitar loop infinito
                continue

            for movimiento in nodo_final.get_movimientos():  # loop a traves de todos los movimientos posibles para la posicion actual
                if movimiento.posicion in expandido:
                    continue

                # agrega el camino con la nueva posicion y sus heuristicas al final de la cola
                nuevo_camino = [camino[0] + self._calcular_nueva_heuristica(movimiento, nodo_final)] + camino[1:] + [movimiento]
                cola.append(nuevo_camino)
                expandido.append(nodo_final.posicion)

            num_nodos_expandidos += 1  # incrementa el contador de rendimiento

        # setea los valores de la clase base
        self.num_nodos_expandidos = num_nodos_expandidos
        self.solucion = camino[1:]