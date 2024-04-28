from zope.interface import Interface
'''
Defina una interface con los siguientes m�todos:

a- insertarElemento: para insertar un objeto en una posici�n determinada en una colecci�n, teniendo en cuenta el manejo de excepciones cuando la posici�n donde se vaya a insertar no sea v�lida.

b-  agregarElemento: para agregar un elemento al final de una colecci�n.

c- mostrarElemento: dada una posici�n de la colecci�n, mostrar los datos del elemento almacenado en dicha posici�n si esa posici�n es v�lida, en caso de que no sea v�lida lanzar una excepci�n que controle el error.
'''

class Interfaz(Interface):
    def instertarElemento(self,objeto):
        pass

    def agregarElemento(self,elemento):
        pass

    def mostrarElemento(self,pos):
        pass