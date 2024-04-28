from Nodo import Nodo


class ABB:
    __raiz: Nodo
    
    def __init__(self) -> None:
        self.__raiz = None
    
    def EstaVacio(self):
        return self.__raiz == None
    
    def getRaiz(self):
        return self.__raiz
    
    def mostrarRaiz(self):
        return self.__raiz.getDato()
    
    
    def insertar(self,subArbol: Nodo,dato):
        if subArbol == None:
            self.__raiz = Nodo(dato)
        else:
            if dato < subArbol.getDato():
                if subArbol.tieneIzquierdo():
                    self.insertar(subArbol.getIzquierdo(),dato)
                else:
                    subArbol.setIzquierdo(Nodo(dato))
            else:
                if subArbol.tieneDerecho():
                    self.insertar(subArbol.getDerecho(),dato)
                else:
                    subArbol.setDerecho(Nodo(dato))
    
    
    def suprimir(self,subArbol: Nodo,dato,anterior = None):
        if subArbol != None:
            if dato == subArbol.getDato():
                grado = self.__getGrado(subArbol)
                if grado == 0:
                    if anterior.getIzquierdo() == subArbol:
                        anterior.setIzquierdo(None)
                    else:
                        anterior.setDerecho(None)
                    del subArbol
                elif grado == 1:
                    #Si tiene hijo izquierdo
                    if subArbol.tieneIzquierdo():
                        hijo = subArbol.getIzquierdo()
                        #Si el el derecho del padre es igual al que deseo eliminar
                        if anterior.getDerecho() == subArbol:
                            anterior.setDerecho(hijo)
                        #Sino es el izquierdo
                        else:
                            anterior.setIzquierdo(hijo)
                        del subArbol
                    #Si tiene hijo derecho sucede lo mismo que para el izquierdo
                    elif subArbol.tieneDerecho():
                        hijo = subArbol.getDerecho()
                        if anterior.getDerecho() == subArbol:
                            anterior.setDerecho(hijo)
                        else:
                            anterior.setIzquierdo(hijo)
                        del subArbol
                else:
                    #Buscamos el mayor de los menores
                    mayorMenor = self.__buscarMayorMenores(subArbol.getIzquierdo())
                    #Eliminamos el nodo hoja que contiene el mayor de los menores(nueva raiz del arbol)
                    self.suprimir(self.__raiz,mayorMenor.getDato())
                    #Asignamos el mayor de los menores al nodo que queremos eliminar
                    subArbol.setDato(mayorMenor.getDato())
                    
            elif dato < subArbol.getDato():
                self.suprimir(subArbol.getIzquierdo(),dato,subArbol)
            else:
                self.suprimir(subArbol.getDerecho(),dato,subArbol)
        else:
            print("No se encontro el dato")
    
    
    def __getGrado(self,subArbol):
        grado = 0
        if subArbol.tieneIzquierdo():
            grado += 1
        if subArbol.tieneDerecho():
            grado += 1
        return grado
    

    def __buscarMayorMenores(self,subArbol):
        if subArbol != None:
            if subArbol.tieneDerecho():
                return self.__buscarMayorMenores(subArbol.getDerecho())
            else:
                return subArbol
        else:
            return None
    

    def buscar(self,subArbol,dato):
        if subArbol == None:
            return None
        elif dato == subArbol.getDato():
            return subArbol
        elif dato < subArbol.getDato():
            return self.buscar(subArbol.getIzquierdo(),dato)
        else:
            return self.buscar(subArbol.getDerecho(),dato)
    
    
    def NiveldelNodo(self,subArbol,dato):
        if subArbol != None:
            if dato == subArbol.getDato():
                return 0
            else:
                if dato < subArbol.getDato():
                    return  self.NiveldelNodo(subArbol.getIzquierdo(),dato) + 1
                else:
                    return  self.NiveldelNodo(subArbol.getDerecho(),dato) + 1
        else:
            return -1
    
    def Hoja(self,subArbol,dato):
        if subArbol != None:
            if dato == subArbol.getDato():
                return not subArbol.tieneIzquierdo() and not subArbol.tieneDerecho() #No tiene derecho ni izquierdo (Hoja)
            else:
                if dato < subArbol.getDato():
                    return self.Hoja(subArbol.getIzquierdo(),dato)
                else:
                    return self.Hoja(subArbol.getDerecho(),dato)
        else:
            return False
    
    
    def esHijo(self,subArbol,datoHijo,datoPadre):
        Padre = self.buscar(subArbol,datoPadre)
        if Padre != None:
            if datoHijo < datoPadre:
                return Padre.getIzquierdo().getDato() == datoHijo
            else:
                return Padre.getDerecho().getDato() == datoHijo
        else:
            return False
    
    
    def getPadre(self,subArbol,datoHijo):
        if subArbol != None:
            if subArbol.tieneIzquierdo() and subArbol.getIzquierdo().getDato() == datoHijo:
                return subArbol
            elif subArbol.tieneDerecho() and subArbol.getDerecho().getDato() == datoHijo:
                return subArbol
            else:
                if datoHijo < subArbol.getDato():
                    return self.getPadre(subArbol.getIzquierdo(),datoHijo)
                else:
                    return self.getPadre(subArbol.getDerecho(),datoHijo)
    
    #def Camino(self,subArbol,dato):
    
    def Altura(self,subArbol):
        if subArbol is None:
            return 0
        else:
            #Calcular la altura de cada subarbol
            HIzq = self.Altura(subArbol.getIzquierdo())
            HDer = self.Altura(subArbol.getDerecho())
            return max(HIzq,HDer) + 1
    
    #Recorridos----------------------------------------------------------
    def inOrden(self,subArbol):
        if subArbol != None:
            self.inOrden(subArbol.getIzquierdo())
            print(subArbol.getDato())
            self.inOrden(subArbol.getDerecho())
    
    
    def preOrden(self,subArbol):
        if subArbol != None:
            print(subArbol.getDato())
            self.preOrden(subArbol.getIzquierdo())
            self.preOrden(subArbol.getDerecho())
    
    
    def postOrden(self,subArbol):
        if subArbol != None:
            self.postOrden(subArbol.getIzquierdo())
            self.postOrden(subArbol.getDerecho())
            print(subArbol.getDato())
    
    
    #Frontera del Arbol--------------------------------------------------
    def frontera(self,subArbol):
        if subArbol != None:
            if subArbol.tieneIzquierdo() == False and subArbol.tieneDerecho() == False:
                print(subArbol.getDato())
            else:
                self.frontera(subArbol.getIzquierdo())
                self.frontera(subArbol.getDerecho())
    
    
    #Metodos para el Ejercicio 3-----------------------------------------
    def mostrarPadreyHerm(self,subArbol,dato):
        Padre = self.getPadre(subArbol,dato)
        if Padre != None:
            print("El padre del nodo {} es: {}".format(dato,Padre.getDato()))
            if Padre.tieneIzquierdo() and Padre.getIzquierdo().getDato() == dato:
                if Padre.tieneDerecho():
                    print("El hermano del nodo {} es: {}".format(dato,Padre.getDerecho().getDato()))
            elif Padre.tieneDerecho() and Padre.getDerecho().getDato() == dato:
                if Padre.tieneIzquierdo():
                    print("El hermano del nodo {} es: {}".format(dato,Padre.getDerecho().getDato()))
            else:
                print("No tiene hermano")
        else:
            print("No tiene padre ni hermano")
    
    
    def mostrarPadreyHermano(self,subArbol,dato,anterior=None):
        if subArbol != None:
            if dato == subArbol.getDato():
                if anterior != None:
                    #Busco si tiene hermano
                    if anterior.getDerecho() == subArbol:
                        hermano = anterior.getIzquierdo()
                    else:
                        hermano = anterior.getDerecho()
                    print('Padre: {}'.format(anterior.getDato()))
                    if hermano != None:
                        print('Hermano: {}'.format(hermano.getDato()))
                    else:
                        print('Hermano: No posee')
                else:
                    print("La subArbol del árbol no tiene padre ni hermanos")
                
            elif dato < subArbol.getDato():
                #Buscar en subArbol de subarbol izquierdo
                self.mostrarPadreyHermano(subArbol.getIzquierdo(),dato,subArbol)
            elif dato > subArbol.getDato():
                #Buscar en subArbol de subarbol derecho
                self.mostrarPadreyHermano(subArbol.getDerecho(),dato,subArbol)
        else:
            print("Error: Nodo inexistente")
    
    
    def cantidadNodos(self,subArbol):
        if subArbol is None:
            return 0
        else:
            return self.cantidadNodos(subArbol.getIzquierdo()) + self.cantidadNodos(subArbol.getDerecho()) + 1
    
    def mostrarSucesores(self,subArbol,dato):
        if subArbol != None:
            if dato == subArbol.getDato():
                print("Sucesores del nodo: {}".format(dato))
                if subArbol.tieneIzquierdo():
                    self.inOrden(subArbol.getIzquierdo())
                if subArbol.tieneDerecho():
                    self.inOrden(subArbol.getDerecho())
            elif dato < subArbol.getDato():
                self.mostrarSucesores(subArbol.getIzquierdo(),dato)
            else:
                self.mostrarSucesores(subArbol.getDerecho(),dato)
        else:
            print("Error: Nodo inexistente")