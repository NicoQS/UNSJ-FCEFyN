from ClaseNodo import Nodo
from zope.interface import implementer
from Interfaz import Interfaz
@implementer(Interfaz)
class Lista:
    __comienzo = None
    __actual = None
    __indice = 0
    __tope = 0

    def __init__(self):
        self.__comienzo=None
        self.__actual=None

    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato=self.__actual.getDato()
            self.__actual=self.__actual.getSiguiente()
            return dato

    def agregarAparato(self,aparato):
        nodo=Nodo(aparato)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo=nodo
        self.__actual=nodo
        self.__tope+=1

    def insertarElemento(self,pos,objeto):
        cont = 1
        cabeza = self.__comienzo
        if self.__comienzo is None:
            nodo = Nodo(objeto)
            nodo.setSiguiente(self.__comienzo)
            self.__comienzo = nodo
            self.__actual = nodo
            self.__tope += 1
        else:
            while cont < pos - 1  and cabeza is not None:
                cont += 1
                cabeza = cabeza.getSiguiente()
            if pos == 1:
                nuevoNodo = Nodo(objeto)
                nuevoNodo.setSiguiente(cabeza)
                self.__comienzo = nuevoNodo
                self.__actual = nuevoNodo
            else:
                nuevoNodo = Nodo(objeto)
                nuevoNodo.setSiguiente(cabeza.getSiguiente())
                cabeza.setSiguiente(nuevoNodo)
            self.__tope+=1

    def insertarFinal(self,objeto):
        if self.__comienzo is None:
            nodo = Nodo(objeto)
            nodo.setSiguiente(self.__comienzo)
            self.__comienzo = nodo
            self.__actual = nodo
        else:
            cabeza = self.__comienzo
            while cabeza.getSiguiente() is not None:
                cabeza = cabeza.getSiguiente()
            nodo = Nodo(objeto)
            cabeza.setSiguiente(nodo)
        self.__tope+=1

    def tipodeObjeto(self, pos):
        dato = None
        cont = 1
        if self.__comienzo is None and pos != 1:
            dato = None
        cabeza = self.__comienzo
        while cabeza.getSiguiente() is not None and cont < pos:
            cont += 1
            cabeza = cabeza.getSiguiente()
        if cont == pos:
            dato = cabeza.getDato()
        return dato

    def ctPhillips(self):
        cont = 0
        cabeza = self.__comienzo
        while cabeza is not None:
            dato = cabeza.getDato()
            if dato.getMarca().lower() == "phillips":
                cont += 1
            cabeza = cabeza.getSiguiente()
        return cont

    def lavaSup(self):
        cabeza = self.__comienzo
        while cabeza is not None:
            dato = cabeza.getDato()
            if dato.getTipo().lower() == "lavarropa" and dato.getTipocarga().lower() == "superior":
                print("Lavarropa de Marca: {}".format(dato.getMarca()))
            cabeza = cabeza.getSiguiente()

    def todoslosAparatos(self):
        cabeza = self.__comienzo
        while cabeza is not None:
            dato = cabeza.getDato()
            print("Marca: {}, Pais de fabricacion: {}, Importe de Venta: ${}".format(dato.getMarca(),dato.getPais(),dato.getImporteF()))
            cabeza = cabeza.getSiguiente()

    def almacenaJson(self,objectEncoder):
        lista = []
        cabeza = self.__comienzo
        while cabeza is not None:
            dato = cabeza.getDato()
            dicc = dato.toJson()
            lista.append(dicc)
            cabeza = cabeza.getSiguiente()
        objectEncoder.guardarJSONArchivo(lista, "NuevosAparatos.json")
        print("--Archivo guardado correctamente--")