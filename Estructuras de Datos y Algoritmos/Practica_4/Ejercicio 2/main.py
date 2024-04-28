from ClaseABB import ABB

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
    print("Frontera del Arbol")
    ArbolBB.frontera(raiz)