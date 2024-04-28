class Nodo:
    __NombreProv: int
    __hectarea:int
    __siguiente:int
    
    def __init__(self, provincia,hectarea):
        self.__NombreProv = provincia
        self.__hectarea = hectarea
        self.__siguiente = None

    def getNombre(self):
        return self.__NombreProv
    
    def getHectareas(self):
        return self.__hectarea

    def getSiguiente(self):
        return self.__siguiente

    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente
    
#--------------------------------------------------------------

class EncadenadaPosicion:
    __cabeza:Nodo
    __cantidad:int
    
    def __init__(self):
        self.__cabeza = None
        self.__cantidad = 0
        
    def Vacia(self):
        return self.__cabeza == None
    """
        def insert(self, Nodo):
            if self.__cabeza is None:
                Nodo.setSiguiente(self.__cabeza)
                self.__cabeza = Nodo
            elif self.__cabeza.getHectareas() < Nodo.getHectareas():
                Nodo.setSiguiente(self.__cabeza)
                self.__cabeza = Nodo
            else:
                aux = self.__cabeza
                band = True
                while band:
                    if aux.getSiguiente() is None:
                        band = False
                    elif aux.getSiguiente().getHectareas() <= Nodo.getHectareas():
                        band=False
                    aux = aux.getSiguiente()
                if aux is None:
                    aux.setSiguiente(Nodo)
                else:
                    Nodo.setSiguiente(aux.getSiguiente()) 
                    aux.setSiguiente(Nodo) 
            self.__cantidad += 1
    """
    
    def insert(self, Nodo):
        if self.__cabeza is None:
            Nodo.setSiguiente(self.__cabeza)
            self.__cabeza = Nodo
        elif self.__cabeza.getHectareas() < Nodo.getHectareas():
            Nodo.setSiguiente(self.__cabeza)
            self.__cabeza = Nodo
        else:
            aux = self.__cabeza
            band = True
            while band:
                if aux.getSiguiente() is None:
                    aux.setSiguiente(Nodo)
                    band = False
                elif aux.getSiguiente().getHectareas() <= Nodo.getHectareas():
                    Nodo.setSiguiente(aux.getSiguiente())
                    aux.setSiguiente(Nodo)
                    band = False
                aux = aux.getSiguiente()
        self.__cantidad += 1
    
    
    def suprimir(self,valor):
        if self.Vacia():
            print("Lista vacia")
        else:
            aux = self.__cabeza
            if aux.getValor() == valor:
                self.__cabeza = aux.getSiguiente()
            else:
                while aux.getSiguiente() != None:
                    if aux.getSiguiente().getValor() == valor:
                        aux.setSiguiente(aux.getSiguiente().getSiguiente())
                        break
                    aux = aux.getSiguiente()

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
            print("Nombre de la provincia: {}, Hectareas Afectadas: {}".format(aux.getNombre(),aux.getHectareas()))
            aux = aux.getSiguiente()