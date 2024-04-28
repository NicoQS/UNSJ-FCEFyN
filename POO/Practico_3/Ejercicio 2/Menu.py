from ManejadorRamos import ManejadorRamos
class Menu:
    __instanciaRamos: ManejadorRamos
    def __init__(self):
        self.__instanciaRamos=ManejadorRamos()
    def mostrar(self):
        print("1 - Registrar un ramo vendido")
        print("2 - 5 Flores mas pedidas")
        print("3 - Tipo de ramo y sus flores vendidas en ese tamaño")
        print("0 - Salir")
    def menuOp (self):
        self.mostrar()
        op=int(input("Ingrese una opcion: "))
        while op != 0:
            if op == 1:
                self.__instanciaRamos.agregar_Venta()
            elif op == 2 :
                self.__instanciaRamos.calcula_Max()
            elif op == 3:
                self.__instanciaRamos.tipoDeRamo()
            self.mostrar()
            op = int(input("Ingrese una opcion: "))
        print("--FIN--")