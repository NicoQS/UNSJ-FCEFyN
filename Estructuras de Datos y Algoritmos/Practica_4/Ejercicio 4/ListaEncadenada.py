class Nodo:
    __arbol: object
    __siguiente: int

    def __init__(self,arbol):
        self.__arbol = arbol
        self.__siguiente = None

    def getDato(self):
        return self.__arbol
    
    def getSiguiente(self):
        return self.__siguiente

    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente

#--------------------------------------------------------------

class EncadenadaOdenada:
    __cabeza:Nodo
    __cantidad:int
    
    def __init__(self):
        self.__cabeza = None
        self.__cantidad = 0
        
    def Vacia(self):
        return self.__cabeza == None

    def getLen(self):
        return self.__cantidad
    
    def insert(self, arbol):
        nuevo = Nodo(arbol)
        if self.__cabeza is None:
            nuevo.setSiguiente(self.__cabeza)
            self.__cabeza = nuevo
        elif self.__cabeza.getDato() > nuevo.getDato():
            nuevo.setSiguiente(self.__cabeza)
            self.__cabeza = nuevo
        else:
            aux = self.__cabeza
            band = True
            while band:
                if aux.getSiguiente() is None:
                    aux.setSiguiente(nuevo)
                    band = False
                elif aux.getSiguiente().getDato() >= nuevo.getDato():
                    nuevo.setSiguiente(aux.getSiguiente()) 
                    aux.setSiguiente(nuevo)
                    band = False
                aux = aux.getSiguiente()
        self.__cantidad += 1
    
    def suprimir(self,pos):
        if pos >=0 and pos < self.__cantidad: 
            if pos == 0:
                aux = self.__cabeza
                self.__cabeza = aux.getSiguiente()
            else:
                anterior = self.__cabeza
                aux = self.__cabeza
                i = 0
                while i != pos:
                    anterior = aux
                    aux = aux.getSiguiente()
                    i+=1
                anterior.setSiguiente(aux.getSiguiente())
            self.__cantidad -= 1
            return aux

    def recuperar(self,posicion):
        if self.Vacia():
            print("Lista vacia")
        elif not self.posValida(posicion):
            print("Posicion no valida")
        else:
            aux = self.__cabeza
            pos = 1
            while pos < posicion:
                aux = aux.getSiguiente()
                pos += 1
            return aux.getValor()
    
    def buscar(self,valor):
        aux = self.__cabeza
        pos = 1
        while aux != None:
            if aux.getValor() == valor:
                return pos
            aux = aux.getSiguiente()
            pos += 1
        return -1

    def primerElemento(self):
        if self.Vacia():
            print("Lista vacia")
        else:
            return self.__cabeza.getValor()
    
    
    def ultimoElemento(self):
        if self.Vacia():
            print("Lista vacia")
        else:
            aux = self.__cabeza
            while aux.getSiguiente() != None:
                aux = aux.getSiguiente()
            return aux.getValor()
    
    def getSiguiente(self,elemento):
        if self.Vacia():
            print("Lista vacia")
        else:
            aux = self.__cabeza
            while aux != None:
                if aux.getValor() == elemento:
                    return aux.getSiguiente().getValor()
                aux = aux.getSiguiente()

    def getAnterior(self,elemento):
        if self.Vacia():
            print("Lista vacia")
        else:
            aux = self.__cabeza
            while aux.getSiguiente() != None:
                if aux.getSiguiente().getValor() == elemento:
                    return aux.getValor()
                aux = aux.getSiguiente()

    def mostrar(self):
        aux = self.__cabeza
        while aux != None:
            print(aux.getDato().getRaiz().getLetra(),aux.getDato().getRaiz().getFrecuencia())
            aux = aux.getSiguiente()