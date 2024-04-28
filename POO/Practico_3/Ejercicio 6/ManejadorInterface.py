from Interfaz import Interfaz
from ObjectEncoder import ObjectEncoder
class ManejaInterface:
    __controlador: ObjectEncoder

    def __init__(self):
        self.__controlador = ObjectEncoder()

    def opciones (self,Ilista: Interfaz,op):
        if op == 2:
            obj = self.__controlador.retornarObjeto()
            pos = int(input("Ingrese la posicion a insertar el objeto: "))
            if obj != None:
                Ilista.insertarElemento(pos,obj)
            else:
                print("Intenta insertar un elemento que no es un objeto de tipo aparato")
        elif op == 3:
            obj = self.__controlador.retornarObjeto()
            if obj != None:
                Ilista.insertarFinal(obj)
            else:
                print("Intenta insertar un elemento que no es un objeto de tipo aparato")
        elif op == 4:
            pos = int(input("Ingrese una posicion de la lista: "))
            dato = Ilista.tipodeObjeto(pos)
            if dato != None:
                print("Tipo de dato: {}".format(dato.getTipo()))
            else:
                print("Posicion incorrecta")

    def llamaInterface(self,lista,op):
        self.opciones(Interfaz(lista),op)



