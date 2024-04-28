from ClaseABB import ABB

import os


def Menu():
    print("1. Mostrar el nodo padre y el nodo hermano, de un nodo previamente ingresado por teclado")
    print("2. Mostrar la cantidad de nodos del árbol en forma recursiva")
    print("3. Mostrar la altura de un árbol")
    print("4. Mostrar los sucesores de un nodo ingresado previamente por teclado")
    print("5. Salir")
    opcion = int(input("Ingrese una opcion: "))
    os.system('cls')
    return opcion

if __name__ == "__main__":
    ArbolBB = ABB()
    ArbolBB.insertar(ArbolBB.getRaiz(),70)
    raiz = ArbolBB.getRaiz() #Obtiene la raiz del arbol != None
    ArbolBB.insertar(raiz,10)
    ArbolBB.insertar(raiz,20)
    ArbolBB.insertar(raiz,40)
    ArbolBB.insertar(raiz,35)
    ArbolBB.insertar(raiz,100)
    ArbolBB.insertar(raiz,90)
    ArbolBB.insertar(raiz,110)
    
    op = Menu()
    while op != 5:
        if op == 1:
            dato = int(input("Ingrese el dato del nodo: "))
            ArbolBB.mostrarPadreyHerm(raiz,dato)
        elif op == 2:
            print("La cantidad de nodos del arbol es: ",ArbolBB.cantidadNodos(raiz))
        elif op == 3:
            print("La altura del arbol es: ",ArbolBB.Altura(raiz))
        elif op == 4:
            dato = int(input("Ingrese el dato del nodo: "))
            ArbolBB.mostrarSucesores(raiz,dato)
        else:
            print("Opcion incorrecta")
        op = Menu()
    print("Fin del programa")