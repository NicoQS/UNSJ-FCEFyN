import numpy as np

class ColadePrioridad:
    __array: np.array
    __cantidad: int
    
    def __init__(self,dimension):
        self.__array = np.full(dimension,None)
        self.__cantidad = 0
        self.__array[0] = -1
    
    def vacio(self):
        return self.__cantidad == 0
    
    def lleno(self):
        return self.__cantidad == len(self.__array)
    
    def padre(self,posicion):
        return posicion // 2
    
    def hijo_izquierdo(self,posicion):
        return posicion * 2
    
    def hijo_derecho(self,posicion):
        return (posicion*2) + 1
    
    def esHoja(self,posicion):
        return posicion > self.__cantidad
    
    def intercambiar(self,pos1,pos2):
        self.__array[pos1],self.__array[pos2] = self.__array[pos2],self.__array[pos1]
    
    def insertar(self, element):
        if self.lleno():
            return print("No hay espacio en la cola")
        else:
            #Propiedad de estructura
            self.__cantidad += 1
            self.__array[self.__cantidad] = element
            actual = self.__cantidad
            #Propiedad de orden
            Padre = self.padre(actual)
            while self.__array[actual] < self.__array[Padre]:
                self.intercambiar(actual, Padre)
                actual = Padre
                Padre = self.padre(actual)
    
    def minimo_a_eliminar(self,pos):
        Padre = pos
        Hizq = self.hijo_izquierdo(pos)
        Hder = self.hijo_derecho(pos) 
        #Mientras no sea hoja y el padre sea mayor que alguno de sus hijos
        while  not self.esHoja(Hder) and (self.__array[Padre] > self.__array[Hizq] or self.__array[Hder]):
            if self.__array[Hizq] <= self.__array[Hder]: #Compara los hijos para ver cual es el menor
                self.intercambiar(Padre,Hizq)
                Padre = Hizq
            else:
                self.intercambiar(Padre,Hder)
                Padre = Hder
            #Actualiza los hijos
            Hizq = self.hijo_izquierdo(Padre) 
            Hder = self.hijo_derecho(Padre)
    
    def eliminar(self):
        #Propiedad de estructura
        eliminado = self.__array[1]
        self.__array[1] = self.__array[self.__cantidad]
        self.__array[self.__cantidad] = None
        self.__cantidad -= 1
        #Propiedad de orden
        self.minimo_a_eliminar(1)
        return eliminado
    
    def mostrar(self):
        for i in range(1,(self.__cantidad // 2+1)):
            print(" PADRE : "+ str(self.__array[i])+" HIJO IZQUIERDO : "+ 
                                str(self.__array[2 * i])+" HIJO DERECHO: "+
                                str(self.__array[(2 * i) + 1]))