from EncadenadaDinamica import  ListaEncadenada, Nodo

"""
La secretaria de modernización de presidencia de la Nación, cuenta con conjuntos de datos (Dataset):  Estadística de designaciones de magistrados de la Justicia Federal y Nacional por género. 
Los datos del archivo están ordenados por año.
se pide 
a) Generar la clase designación: con los atributos que posee el archivo.
b)Leer los datos del archivo csv, y generar una lista de designaciones.
c)Leer un tipo de cargo por teclado, y mostrar la cantidad de mujeres designadas en ese cargo por año. 
d)Leer una materia, un cargo y un año y mostrar la cantidad de agentes designados en ese cargo,  esa materia en ese año.
"""

if __name__== "__main__":
    lista=ListaEncadenada()
    tipCargo=input("Ingrese el tipo de cargo: ")
    lista.mostrarMujeresDesignadas(tipCargo)
    tipCargo=input("Ingrese el tipo de cargo: ")
    materia=input("Ingrese la materia: ")
    anio=int(input("Ingrese el año: "))
    lista.itemD(materia,tipCargo,anio)
"""
Defensor
Defensor
Penal
2002
"""