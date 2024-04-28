import random


class Puzzle:
    """
    Rompecabezas genérico con cualquier tamaño de matriz cuadrada (por ejemplo, 3x3, 4x4...)
    """
    posicion: int
    NUM_FILAS_PUZZLE: int 
    NUM_COLUMNAS_PUZZLE: int
    POSICION_FINAL_PUZZLE: list

    def __init__(self, posicion):
        """
        :param posicion: una lista de listas que representan la matriz del rompecabezas
        """
        self.posicion = posicion
        self.NUM_FILAS_PUZZLE = len(posicion)
        self.NUM_COLUMNAS_PUZZLE = len(posicion[0])
        self.POSICION_FINAL_PUZZLE = self._generar_posicion_final()

        if self.NUM_FILAS_PUZZLE != self.NUM_COLUMNAS_PUZZLE:
            raise RuntimeError('Dimension invalida del Puzzle')

    def __str__(self):
        """
        Imprimir en consola como matriz
        """
        long_puzzle = (3 * self.NUM_FILAS_PUZZLE) + 1
        puzzle_string = '—' * long_puzzle + '\n'

        for i in range(self.NUM_FILAS_PUZZLE):
            for j in range(self.NUM_COLUMNAS_PUZZLE):
                puzzle_string += '│{0: >2}'.format(str(self.posicion[i][j]))
                if j == self.NUM_COLUMNAS_PUZZLE - 1:
                    puzzle_string += '│\n'

        puzzle_string += '—' * long_puzzle + '\n'

        return puzzle_string

    def _generar_posicion_final(self):
        """
        Example end position in 4x4 puzzle
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
        """
        posicion_final = []
        nueva_fila = []

        for i in range(1, self.NUM_FILAS_PUZZLE * self.NUM_COLUMNAS_PUZZLE + 1):
            nueva_fila.append(i)
            if len(nueva_fila) == self.NUM_COLUMNAS_PUZZLE:
                posicion_final.append(nueva_fila)
                nueva_fila = []

        posicion_final[-1][-1] = 0  # agrega un espacio en blanco al final

        return posicion_final

    def _intercambio(self, x1, y1, x2, y2):
        """
        Intercambiar posiciones entre dos elementos
        """
        copia_puzzle = [list(row) for row in self.posicion]  #Copia el puzzle
        copia_puzzle[x1][y1], copia_puzzle[x2][y2] = copia_puzzle[x2][y2], copia_puzzle[x1][y1]

        return copia_puzzle

    @staticmethod
    def _es_impar(num):
        return num % 2 != 0

    @staticmethod
    def _es_par(num):
        return num % 2 == 0

    def _get_fila_espacio_blanco_contando_desde_abajo(self):
        fila_cero, _ = self._get_coordenadas(0)  # blank space
        return self.NUM_FILAS_PUZZLE - fila_cero

    def _get_coordenadas(self,pieza, posicion=None):
        """
        Devuelve las coordenadas i, j para un lugar dado
        """
        if not posicion:
            posicion = self.posicion

        for i in range(self.NUM_FILAS_PUZZLE):
            for j in range(self.NUM_COLUMNAS_PUZZLE):
                if posicion[i][j] == pieza:
                    return i, j

        return RuntimeError('Valor de pieza invalido')

    def _get_recuento_de_inversiones(self):
        inv_count = 0
        puzzle_list = [number for row in self.posicion for number in row if number != 0]

        for i in range(len(puzzle_list)):
            for j in range(i + 1, len(puzzle_list)):
                if puzzle_list[i] > puzzle_list[j]:
                    inv_count += 1

        return inv_count

    def get_movimientos(self):
        """
        Retorna la lista de todos los movimientos posibles
        """
        movimientos = []
        i, j = self._get_coordenadas(0)  # espacio en blanco

        if i > 0:
            movimientos.append(Puzzle(self._intercambio(i, j, i - 1, j)))  # move up

        if j < self.NUM_COLUMNAS_PUZZLE - 1:
            movimientos.append(Puzzle(self._intercambio(i, j, i, j + 1)))  # move right

        if j > 0:
            movimientos.append(Puzzle(self._intercambio(i, j, i, j - 1)))  # move left

        if i < self.NUM_FILAS_PUZZLE - 1:
            movimientos.append(Puzzle(self._intercambio(i, j, i + 1, j)))  # move down

        return movimientos

    def Hallar_fuera_de_Lugar(self):
        """
        Cuenta el numero de piezas desposicionadas
        """
        fuera_de_lugar = 0

        for i in range(self.NUM_FILAS_PUZZLE):
            for j in range(self.NUM_COLUMNAS_PUZZLE):
                if self.posicion[i][j] != self.POSICION_FINAL_PUZZLE[i][j]:
                    fuera_de_lugar += 1
        return fuera_de_lugar

    def hallar_distancia_de_manhattan(self):
        """
        Cuenta que tan desposicionada esta la pieza de la posicion original
        """
        distancia = 0

        for i in range(self.NUM_FILAS_PUZZLE):
            for j in range(self.NUM_COLUMNAS_PUZZLE):
                i1, j1 = self._get_coordenadas(self.posicion[i][j], self.POSICION_FINAL_PUZZLE)
                distancia += abs(i - i1) + abs(j - j1)
        return distancia

    def es_resoluble(self):
        """
        1. Si N es impar, entonces el puzzle es resoluble si el numero de inversiones es par en el input
        2. Si N es par, el puzzle es resoluble si:
            - el espacio esta en una fila par contando desde abajo (second-last,fourth-last,etc)
            y el numero de inversiones es par.
            - El espacio esta en una fila impar contando desde abajo (ultima,3er ultima,etc)
            y el numero de inversiones es par.
        3. Para el resto de casos, el puzzle no se puede resolver
        :return: Boolean if the puzzle is solvable or not
        """

        contador_inversiones = self._get_recuento_de_inversiones()
        posicion_vacia = self._get_fila_espacio_blanco_contando_desde_abajo()

        if self._es_impar(self.NUM_FILAS_PUZZLE) and self._es_par(contador_inversiones):
            return True
        elif self._es_par(self.NUM_FILAS_PUZZLE) and self._es_par(posicion_vacia) and self._es_impar(contador_inversiones):
            return True
        elif self._es_par(self.NUM_FILAS_PUZZLE) and self._es_impar(posicion_vacia) and self._es_par(contador_inversiones):
            return True
        else:
            return False

    def generar_posicion_random(self):
        """
        Mezcla el puzzle
        """
        while True:
            random.shuffle(self.posicion)  # mezclar filas
            for row in self.posicion:
                random.shuffle(row)  # mezclar columnas

            if self.es_resoluble():
                break