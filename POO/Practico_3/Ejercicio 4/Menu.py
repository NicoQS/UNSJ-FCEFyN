from ManejadorCalefactores import ManejadorCalefactores
class Menu:
    __manejaCalefactores: ManejadorCalefactores

    def __init__(self):
        self.__manejaCalefactores=ManejadorCalefactores()
        self.__manejaCalefactores.cargaGas()
        self.__manejaCalefactores.cargaElectricos()

    def mostrar(self):
        print("1- Ingresar por teclado el  costo por m3 y cantidad que se estima consumir en m3 y mostrar marca y modelo del calefactor a gas natural de menor costo de consumo.\n2 - Ingresar por teclado el costo de el kilowatt/h, la cantidad que se estima consumir por hora y mostrar  marca  y modelo del calefactor eléctrico de menor consumo.\n3 - Teniendo en cuenta los dos ítems anteriores, muestre: tipo de calefactor y todos los datos del calefactor de menor consumo.")

    def menu_Op(self):
        self.mostrar()
        op=int(input("Ingrese una opcion 0 para terminar: "))
        while op != 0:
            if op == 1:
                c1 = int(input("Ingrese el costo por metro al cubo: "))
                h1 = int(input("Ingrese la cantidad que se estima que consumira por hora: "))
                self.__manejaCalefactores.opciones(op,c1,h1)
            elif op == 2:
                c2 = int(input("Ingrese el costo por metro al cubo: "))
                h2 = int(input("Ingrese la cantidad que se estima que consumira por hora: "))
                self.__manejaCalefactores.opciones(op,c2,h2)
            elif op == 3:
                self.__manejaCalefactores.opciones(op,c1,h1)
            self.mostrar()
            op = int(input("Ingrese una opcion 0 para terminar: "))