class Nodo:
    __frecuencia: int
    __letra: str
    __izquierdo: None
    __derecho: None
    
    def __init__(self, letra,frecuencia) -> None:
        self.__frecuencia=frecuencia
        self.__letra=letra
        self.__izquierdo = None
        self.__derecho = None
        
    def getFrecuencia(self):
        return self.__frecuencia
    
    def getLetra(self):
        return self.__letra
    
    def setFrecuencia(self,frecuencia):
        self.__frecuencia = frecuencia
    
    def setLetra(self,letra):
        self.__letra = letra
    
    def getIzquierdo(self):
        return self.__izquierdo
    
    def setIzquierdo(self,newizq):
        self.__izquierdo = newizq
    
    def getDerecho(self):
        return self.__derecho

    def setDerecho(self,newder):
        self.__derecho = newder
        
    def tieneDerecho(self):
        return self.__derecho != None
    
    def tieneIzquierdo(self):
        return self.__izquierdo != None

class ABB:
    __raiz: Nodo
    
    def __init__(self,letra,frecuencia) -> None:
        self.__raiz = Nodo(letra,frecuencia)
    
    def EstaVacio(self):
        return self.__raiz == None
    
    def getRaiz(self):
        return self.__raiz
    
    def mostrarRaiz(self):
        return self.__raiz.getDato()
    
    def insertar(self,nodo):
        if self.__raiz.getIzquierdo() is None:
            self.__raiz.setIzquierdo(nodo)
        else:
            self.__raiz.setDerecho(nodo)
    
    
    def generaCodigo(self,raiz,letra):
        if raiz.getLetra() != letra:
            nodoIzq = raiz.getIzquierdo()
            nodoDer = raiz.getDerecho()
            if letra in nodoIzq.getLetra():
                cod = "0" + self.generaCodigo(nodoIzq,letra)
            
            elif letra in nodoDer.getLetra():
                cod = "1" + self.generaCodigo(nodoDer,letra)
            
            else:
                cod = "x" #No se encuentra el caracter
            return cod
        else:
            return ""
    
    def generaLetra(self,raiz,codigo):
        if raiz != None:
            if codigo != "":
                #Leo el primer digito
                primerDigito = codigo[0]
                print(primerDigito)
                print(codigo[1:])
                #Segun el valor del digito me voy por izquierda o derecha
                if primerDigito == '0':
                    letra = self.generaLetra(raiz.getIzquierdo(),codigo[1:])
                if primerDigito == '1':
                    letra = self.generaLetra(raiz.getDerecho(),codigo[1:])
                return letra
            else:
                #Caso base, veo el caracter en el nodo hoja
                letra = raiz.getLetra()
                print(letra)
                return letra
        else:
            #No se encontro una hoja con el codigo ingresado
            return 'Codigo desconocido'
    
    
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
    
    
    def frontera(self,subArbol):
        if subArbol != None:
            if subArbol.tieneIzquierdo() == False and subArbol.tieneDerecho() == False:
                print(subArbol.getLetra())
            else:
                self.frontera(subArbol.getIzquierdo())
                self.frontera(subArbol.getDerecho())
    
    
    def buscar(self,subArbol,dato):
        if subArbol != None:
            if dato == subArbol.getDato():
                return subArbol
            elif dato < subArbol.getDato():
                    return self.buscar(subArbol.getIzquierdo(),dato)
            else:
                return self.buscar(subArbol.getDerecho(),dato)
        else:
            return None
    
    def __gt__(self,arbol):
        return self.__raiz.getFrecuencia() > arbol.getRaiz().getFrecuencia()
    
    def __ge__(self,arbol):
        return self.__raiz.getFrecuencia() >= arbol.getRaiz().getFrecuencia()