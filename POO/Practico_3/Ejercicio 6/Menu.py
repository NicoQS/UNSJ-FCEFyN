from ObjectEncoder import ObjectEncoder
from ClaseHeladeras import Heladera
from ClaseLavarropas import Lavarropa
from ClaseTelevisores import Televisor
from ManejadorInterface import ManejaInterface
from ClaseLista import Lista
import os
class Menu:
    __claseLista: Lista
    def __init__(self):
        self.__claseLista=Lista()
    def mostrar(self):
        print("1 - Crear archivo .json si es que no existe")
        print("2 - Insertar un aparato en la colección en una posición determinada.\n3 - Agregar un aparato a la colección (solicitar el tipo de aparato, y luego los datos que correspondan).")
        print("4 - Dada una posición de la Lista: Mostrar por pantalla qué tipo de objeto se encuentra almacenado en dicha posición.")
        print("5 - Mostrar la cantidad de heladeras, lavarropas y televisores cuya marca sea phillips.")
        print("6 - Mostrar la marca de todos los lavarropas que tienen carga superior .\n7 - Mostrar para todos los aparatos que la empresa tiene a la venta, marca, país de fabricación e importe de venta.")
        print("8 - Almacenar los objetos de la colección Lista en el archivo “aparatoselectronicos.json”.")
    def cargaJson(self,jsonF):
        objeto1 = Heladera("Lg", "FKROA", "Negro", "Argentina", 325000, 2300, True, False)
        objeto2 = Lavarropa("Liliana", "45LDKN", "Blanco", "Argentina", 450000, 4, 2300, 2, "Superior")
        objeto3 = Televisor("Hitachi", "IIOER89", "Blanco", "USA", 45400, "LCD", "55.5", "HD", True)
        d = objeto1.toJson()
        d1 = objeto2.toJson()
        d2 = objeto3.toJson()
        lista = [d, d1, d2]
        jsonF.guardarJSONArchivo(lista, "Aparatos.json")

    def apartado_4(self):
        ct = self.__claseLista.ctPhillips()
        if ct != 0:
            print("Cantidad de aparatos de la marca phillips: {}".format(ct))
        else:
            print("No hay aparatos de la marca phillips")

    def menuOp(self):
        manejaInterfaz = ManejaInterface()
        jsonF = ObjectEncoder()
        jsonF.decodificarDiccionario(self.__claseLista)
        self.mostrar()
        op=int(input("Ingrese una opcion 0 para terminar: "))
        while op != 0:
            os.system('cls')
            if op == 1:
                self.cargaJson(jsonF)

            elif op == 2:
                manejaInterfaz.llamaInterface(self.__claseLista,op)

            elif op == 3:
                manejaInterfaz.llamaInterface(self.__claseLista,op)

            elif op == 4:
                manejaInterfaz.llamaInterface(self.__claseLista,op)

            elif op == 5:
                self.apartado_4()

            elif op == 6:
                self.__claseLista.lavaSup()

            elif op == 7:
                self.__claseLista.todoslosAparatos()

            elif op == 8:
                self.__claseLista.almacenaJson(jsonF)
            self.mostrar()
            op = int(input("Ingrese una opcion 0 para terminar: "))
            os.system('cls')