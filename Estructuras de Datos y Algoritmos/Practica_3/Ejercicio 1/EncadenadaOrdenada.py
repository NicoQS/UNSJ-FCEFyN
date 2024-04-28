class Nodo:
	__valor: int
	__siguiente: int

	def __init__(self, valor):
		self.__valor = valor
		self.__siguiente = None

	def getValor(self):
		return self.__valor

	def setValor(self, valor):
		self.__valor = valor

	def getSiguiente(self):
		return self.__siguiente

	def setSiguiente(self, siguiente):
		self.__siguiente = siguiente

#--------------------------------------------------------------

class EncadenadaOrdenada:
    __cabeza:Nodo
    __cantidad:int
    
    def __init__(self):
        self.__cabeza = None
        self.__cantidad = 0
        
    def Vacia(self):
        return self.__cabeza == None

    def insert(self, value):
        nuevo = Nodo(value)
        if self.__cabeza is None:
            nuevo.setSiguiente(self.__cabeza)
            self.__cabeza = nuevo
        elif self.__cabeza.getValor() > value:
            nuevo.setSiguiente(self.__cabeza)
            self.__cabeza = nuevo
        else:
            aux = self.__cabeza
            band = True
            while band:
                if aux.getSiguiente() is None:
                    aux.setSiguiente(nuevo)
                    band = False
                elif aux.getSiguiente().getValor() >= value:
                    nuevo.setSiguiente(aux.getSiguiente()) 
                    aux.setSiguiente(nuevo) 
                    band = False
                aux=aux.getSiguiente()
        self.__cantidad += 1
    
    
    def suprimir(self,valor):
        if self.Vacia():
            print("Lista vacia")
        else:
            aux = self.__cabeza
            if aux.getValor() == valor:
                self.__cabeza = aux.getSiguiente()
            else:
                band = True
                while aux.getSiguiente() != None and band is True:
                    if aux.getSiguiente().getValor() == valor:
                        aux.setSiguiente(aux.getSiguiente().getSiguiente())
                        band = False
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
            print(aux.getValor())
            aux = aux.getSiguiente()

if __name__=="__main__":
    lista = EncadenadaOrdenada()
    lista.insert(5)
    lista.insert(4)
    lista.insert(3)
    lista.insert(1)
    lista.insert(2)
    lista.suprimir(3)
    print(lista.getSiguiente(2))
    print(lista.getAnterior(2))
    print("------------------")
    lista.mostrar()