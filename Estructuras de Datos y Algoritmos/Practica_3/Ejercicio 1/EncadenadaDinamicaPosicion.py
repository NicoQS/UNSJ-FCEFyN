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

class EncadenadaPosicion:
    __cabeza:Nodo
    __cantidad:int
    
    def __init__(self) -> None:
        self.__cabeza = None
        self.__cantidad = 0
        
    def Vacia(self):
        return self.__cabeza == None
    
    def posValida(self,pos):
        return pos > 0 and pos-1 <= self.__cantidad
    
    def insertar(self, valor, posicion):
        if not self.posValida(posicion):
            print("Posicion no valida")
        else:
            nuevo = Nodo(valor)
            if posicion == 1:
                nuevo.setSiguiente(self.__cabeza)
                self.__cabeza = nuevo
            else:
                aux = self.__cabeza
                posActual = 1
                while  posActual < posicion-1:
                    aux = aux.getSiguiente()
                    posActual += 1
                nuevo.setSiguiente(aux.getSiguiente())
                aux.setSiguiente(nuevo)
        self.__cantidad += 1


    def suprimir(self,posicion):
        if self.Vacia():
            print("Lista vacia")
        elif not self.posValida(posicion):
            print("Posicion no valida")
        else:
            aux = self.__cabeza
            pos = 1
            while pos < posicion-1:
                aux = aux.getSiguiente()
                pos += 1
            elimino = aux.getSiguiente()
            aux.setSiguiente(elimino.getSiguiente())
            del elimino
            self.__cantidad -= 1
    
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
    
    def getSiguiente(self,posicion):
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
            return aux.getSiguiente().getValor()
    
    def getAnterior(self,posicion):
        if self.Vacia():
            print("Lista vacia")
        elif not self.posValida(posicion):
            print("Posicion no valida")
        else:
            aux = self.__cabeza
            pos = 1
            while pos < posicion-1:
                aux = aux.getSiguiente()
                pos += 1
            return aux.getValor()

    def mostrar(self):
        aux = self.__cabeza
        while aux != None:
            print(aux.getValor())
            aux = aux.getSiguiente()

if __name__=="__main__":
    lista = EncadenadaPosicion()
    lista.insertar(1,1)
    lista.insertar(2,2)
    lista.insertar(3,3)
    lista.insertar(4,4)
    lista.insertar(5,7)#error
    
    if lista.recuperar(3) == -1:
        print("No se encontro el elemento")
    else:
        print("El elemento es {}".format(lista.recuperar(3)))

    if lista.buscar(3) == -1:
        print("No se encontro el elemento")
    else:
        print("El elemento se encuentra en la posicion {}".format(lista.buscar(3)))
    
    print ("El primer elemento es {}".format(lista.primerElemento()))
    print("El ultimo elemento es {}".format(lista.ultimoElemento()))
    print("El siguiente elemento de 2 es {}".format(lista.getSiguiente(2)))
    print("El anterior elemento de 2 es {}".format(lista.getAnterior(2)))
    
    lista.suprimir(4)
    lista.mostrar()