from hashlib import new
import imp
from os import path
from ListaEncadenada import EncadenadaOdenada
from ABB import ABB

class CodificadorDecodificador():
    __letras = []
    __frecuencia = []
    __ListaEnlazada = EncadenadaOdenada()
    __arbolHuffman = None
    __archivo: str
    def __init__(self) -> None:
        self.__archivo = ""
        self.__letras=[]
        self.__frecuencia=[]
        self.__ListaEnlazada=EncadenadaOdenada()
        self.__arbolHuffman= None

    def Leerarchivo(self,nombre):
        try:
            newname = path.dirname(__file__) +"/" + str(nombre)+".txt"
            archivo = open(newname, 'r')
            self.__archivo = newname
            for line in archivo:
                for letra in line:
                    if letra != "\n" and letra != " ":
                        if letra in self.__letras:
                            self.__frecuencia[self.__letras.index(letra)] += 1
                        else:
                            self.__letras.append(letra)
                            self.__frecuencia.append(1)
            archivo.close()
            print("Archivo leido con exito")
            for i in range(len(self.__letras)):
                print(self.__letras[i], self.__frecuencia[i])
            print("Total de letras: ", len(self.__letras))
            print("----------------------------------")
        except:
            print("Error al abrir el archivo")
            return False
    
    
    
    def crearArbol(self):
            #Genera una lista enlazada de arboles ordenados por frecuencia de cada caracter
        for i in range(len(self.__letras)):
            newArbol = ABB(self.__letras[i],self.__frecuencia[i])
            self.__ListaEnlazada.insert(newArbol)
        while self.__ListaEnlazada.getLen() > 1:
            #Tomo de a pares, desde las frecuencias menores y creo un nuevo arbol
            #Tendra como raiz la suma de las frec y los dos chars juntos

            #Suprimo de la lista los de menor frec, obtengo los nodos
            primero = self.__ListaEnlazada.suprimir(0)
            segundo = self.__ListaEnlazada.suprimir(0)

            #De cada nodo obtengo el dato, es el arbol en sí
            arbol1 = primero.getDato()
            arbol2 = segundo.getDato()

            #De cada árbol obtengo su raiz, es el nodo con caracter y frec
            raiz1 = arbol1.getRaiz()
            raiz2 = arbol2.getRaiz()

            #Concateno los caracteres y sumo las frecuencias
            newChar = raiz1.getLetra() + raiz2.getLetra()
            newFrec = raiz1.getFrecuencia() + raiz2.getFrecuencia()

            #Creo el nuevo arbol
            newArbol = ABB(newChar,newFrec)
            
            #Coloco los hijos izquierdo y derecho
            #Tendra como hijo izq al de menor frec, y como hijo der al de mayor frec
            newArbol.insertar(raiz1)
            newArbol.insertar(raiz2)
            
            #Vuelvo a insertar en la lista
            self.__ListaEnlazada.insert(newArbol)
    
        #Obtengo el árbol generador de codigos de huffman
        elemento = self.__ListaEnlazada.suprimir(0)
        self.__arbolHuffman = elemento.getDato()
        print('\nÁrbol binario generado')
        self.__arbolHuffman.frontera(self.__arbolHuffman.getRaiz())
    
    def comprimirArchivo(self):
        if self.__archivo == "":
            print("No se ha cargado un archivo")
            return False
        else:
            raiz = self.__arbolHuffman.getRaiz()
            archivo = open(self.__archivo, 'r')
            comprimido = ""
            for linea in archivo:
                for letra in linea:
                    if letra == "\n":
                        comprimido += "\n"
                    elif letra == " ":
                        comprimido += " "
                    else:
                        comprimido += self.__arbolHuffman.generaCodigo(raiz,letra)
            
            archivo.close()
            print("Generando archivo comprimido...")
            newname = path.dirname(__file__) +"/" + "comprimido.txt"
            archivo = open(newname, 'w')
            archivo.write(comprimido)
            archivo.close()
            print("Archivo generado correctamente")
    
    def descomprimirArchivo(self,texto):
        if texto == "":
            print("No se ha cargado un archivo")
            return False
        else:
            raiz = self.__arbolHuffman.getRaiz()
            newname = path.dirname(__file__) +"/" + str(texto)+".txt"
            archivo = open(newname, 'r')
            descomprimido = ""
            for lineaAr in archivo:
                linea = lineaAr.replace("\n"," ")
                codigos = linea.split(" ")
                #print(codigos)
                for codigo in codigos:
                    descomprimido += self.__arbolHuffman.generaLetra(raiz,codigo)
            archivo.close()
            print("Generando archivo descomprimido...")
            newname = path.dirname(__file__) +"/" + "descomprimido.txt"
            archivo = open(newname, 'w')
            archivo.write(descomprimido)
            archivo.close()
            print("Archivo generado correctamente")