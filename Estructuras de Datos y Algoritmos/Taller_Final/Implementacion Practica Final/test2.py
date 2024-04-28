from puzzle import Puzzle
from algorithms import AEstrella
from solver import PuzzleSolver

def test_rendimiento():
    puzzle_start = Puzzle([[1, 2, 3],[5, 6, 0],[4, 7, 8 ]])
    s1 = PuzzleSolver(AEstrella(puzzle_start,heuristic='hallar_distancia_de_manhattan'))
    s1.run()
    s1.print_rendimiento()
    print("Estrategia con heuristica de distancia de manhattan")
    s1.print_solucion()

    s1 = PuzzleSolver(AEstrella(puzzle_start, heuristic='Hallar_fuera_de_Lugar'))
    s1.run()
    s1.print_rendimiento()
    print("Estrategia con heuristica de fuera de lugar")
    s1.print_solucion()


if __name__ == "__main__":
    test_rendimiento()