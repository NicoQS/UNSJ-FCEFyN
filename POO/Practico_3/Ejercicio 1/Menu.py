from ManejaFacultades import ManejaFacultades
class Menu:
    __instancia: ManejaFacultades
    def __init__(self):
        self.__instancia=ManejaFacultades()
        self.__instancia.carga_lista()
    def mostrar(self):
        print ("\n1- Listado")
        print("2- Dado un codigo de facultad, informa sus datos")
        print("3- Dado un nombre de carrera, informa sus datos")
        print("0 para salir")
    def funcion_2(self):
        cod=int(input("Ingrese un codigo de facultad: "))
        self.__instancia.informa_facu(cod)
    def funcion_3(self):
        nm=input("Ingrese el nombre de una carrera: ")
        self.__instancia.informa_carrera(nm)
        #self.__instancia.busca_prueba(nm)
    def Menu_op(self):
        self.mostrar()
        op=int(input("Ingrese una opcion: "))
        while op != 0:
            if op==1:
                self.__instancia.listado()
            elif op ==2:
                self.funcion_2()
            elif op==3:
                self.funcion_3()
            self.mostrar()
            op = int(input("Ingrese una opcion: "))