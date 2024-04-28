class PuzzleSolver:
    """
    Ejecuta las diferentes estrategias para resolver las estrategias y printea la solucion y la performance
    """

    def __init__(self, estrategia):
        """
        :param strategy: Strategy
        """
        self._estrategia = estrategia

    def print_rendimiento(self):
        """
        Numero de nodos expandidos en el arbol de busqueda
        """
        print(f'{self._estrategia} - Nodos expandidos: {self._estrategia.num_nodos_expandidos}')

    def print_solucion(self):
        """
        Explicacion de como resolver el puzzle
        """
        print('Solucion:')
        print("Puzzle Inicial:")
        print(self._estrategia.start)
        print("------------------")
        print("Numero de movimientos: ", len(self._estrategia.solucion)-1)
        for i in range(1, len(self._estrategia.solucion)):
            print(self._estrategia.solucion[i])
        

    def run(self):
        if not self._estrategia.start.es_resoluble():  # Comprobar si el puzzle es resoluble antes de correr el algoritmo
            raise RuntimeError('El puzzle no se puede resolver')

        self._estrategia.resolver_puzzle()