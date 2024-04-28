from puzzle import Puzzle
from algorithms import MenorCosto, FIFO
from solver import PuzzleSolver


def test_generar_ultima_posicion():
    puzzle_4x4 = Puzzle([[0, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 1]])

    assert puzzle_4x4.POSICION_FINAL_PUZZLE == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]], '4x4'

    puzzle_3x3 = Puzzle([[0, 2, 1], [3, 5, 4], [6, 7, 8]])
    assert puzzle_3x3.POSICION_FINAL_PUZZLE == [[1, 2, 3], [4, 5, 6], [7, 8, 0]], '3x3'


def test_intercambio():
    puzzle = Puzzle([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]])
    nueva_posicion = puzzle._intercambio(0, 0, 0, 1)

    assert nueva_posicion == [[2, 1, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]


def test_get_coordenadas():
    puzzle = Puzzle([[1, 2, 6, 3], [4, 9, 5, 7], [8, 13, 11, 15], [12, 14, 0, 10]])
    i, j = puzzle._get_coordenadas(0)

    assert i == 3
    assert j == 2

    i, j = puzzle._get_coordenadas(10)
    assert i == 3
    assert j == 3


def test_generar_posicion_random():
    initial_position = [[1, 2, 6, 3], [4, 9, 5, 7], [8, 13, 11, 15], [12, 14, 0, 10]]
    puzzle = Puzzle(initial_position.copy())
    puzzle.generar_posicion_random()
    new_position = puzzle.posicion

    #assert initial_position != new_position


def test_todos_posibles_movimientos():
    puzzle = Puzzle([[1, 2, 3, 4], [5, 6, 0, 7], [8, 9, 10, 11], [12, 13, 14, 15]])
    output = puzzle.get_movimientos()

    assert output[0].posicion == [[1, 2, 0, 4], [5, 6, 3, 7], [8, 9, 10, 11], [12, 13, 14, 15]], 'up'
    assert output[1].posicion == [[1, 2, 3, 4], [5, 6, 7, 0], [8, 9, 10, 11], [12, 13, 14, 15]], 'right'
    assert output[2].posicion == [[1, 2, 3, 4], [5, 0, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]], 'left'
    assert output[3].posicion == [[1, 2, 3, 4], [5, 6, 10, 7], [8, 9, 0, 11], [12, 13, 14, 15]], 'down'


def testear_heuristico_desposicionado():
    puzzle = Puzzle([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]])
    misplaced = puzzle.Hallar_fuera_de_Lugar()

    assert misplaced == 0

    puzzle = Puzzle([[1, 2, 4, 3], [5, 6, 8, 7], [9, 10, 12, 11], [13, 14, 15, 0]])
    misplaced = puzzle.Hallar_fuera_de_Lugar()
    assert misplaced == 6


def test_hallar_distancia_de_manhattan():
    puzzle = Puzzle([[1, 2, 6, 3], [4, 9, 5, 7], [8, 13, 11, 15], [12, 14, 0, 10]])
    distance = puzzle.hallar_distancia_de_manhattan()

    assert distance == 28


def test_puzzle_sin_solucion():
    puzzle = Puzzle([[1, 8, 2], [0, 4, 3], [7, 6, 5]])
    assert puzzle._get_recuento_de_inversiones() == 10
    assert puzzle.es_resoluble()

    puzzle = Puzzle([[13, 2, 10, 3], [1, 12, 8, 4], [5, 0, 9, 6], [15, 14, 11, 7]])
    assert puzzle._get_recuento_de_inversiones() == 41
    assert puzzle.es_resoluble()

    puzzle = Puzzle([[6, 13, 7, 10], [8, 9, 11, 0], [15, 2, 12, 5], [14, 3, 1, 4]])
    assert puzzle._get_recuento_de_inversiones() == 62
    assert puzzle.es_resoluble()

    puzzle = Puzzle([[3, 9, 1, 15], [14, 11, 4, 6], [13, 0, 10, 12], [2, 7, 8, 5]])
    assert puzzle._get_recuento_de_inversiones() == 56
    assert not puzzle.es_resoluble()

    puzzle = Puzzle([[1, 2, 3, 7], [12, 8, 15, 4], [13, 10, 11, 5], [9, 6, 14, 0]])
    assert puzzle._get_recuento_de_inversiones() == 33
    assert not puzzle.es_resoluble()


def test_rendimiento():
    puzzle_start = Puzzle([[1, 2, 3, 4], [5, 6, 7, 8], [0, 10, 11, 12], [9, 13, 14, 15]])

    s2 = PuzzleSolver(FIFO(puzzle_start))
    s2.run()
    s2.print_rendimiento()
    s2.print_solucion()
    assert s2._estrategia.num_nodos_expandidos == 56

    s1 = PuzzleSolver(MenorCosto(puzzle_start,heuristic='hallar_distancia_de_manhattan'))
    s1.run()
    s1.print_rendimiento()
    s1.print_solucion()
    assert s1._estrategia.num_nodos_expandidos == 4

    s1 = PuzzleSolver(MenorCosto(puzzle_start, heuristic='Hallar_fuera_de_Lugar'))
    s1.run()
    s1.print_rendimiento()
    s1.print_solucion()
    assert s1._estrategia.num_nodos_expandidos == 4

if __name__ == "__main__":
    test_generar_ultima_posicion()
    test_generar_posicion_random()
    test_intercambio()
    test_get_coordenadas()
    test_todos_posibles_movimientos()
    testear_heuristico_desposicionado()
    test_hallar_distancia_de_manhattan()
    test_puzzle_sin_solucion()
    test_rendimiento()