import os
from ObjectEncoder import ObjectEncoder
from ClaseDocente import Docente
from ClaseInvestigador import Investigador
from ClasePersonalApoyo import PersonalApoyo
from ClaseDocenteInvestigador import DocenteInvestigador
from ManejaInterfaz import ManejaInterface
from ClaseLista import Lista
class Menu:
    __claseLista: Lista

    def __init__(self):
        self.__claseLista=Lista()

    def mostrar(self):
        print("1 - Crear archivo .json si es que no existe")
        print("2 - Insertar un agente en la colección en una posición determinada.\n3 - Agregar un agente a la colección.")
        print("4 - Dada una posición de la lista: Mostrar por pantalla que tipo de agente se encuentra almacenado en dicha posición.")
        print("5 - Ingresar por teclado el nombre de una carrera y generar un listado ordenado por nombre con todos los datos de los agentes que se desempeñan como docentes investigadores.")
        print("6 - Dada un área de investigación, contar la cantidad de agentes que son docente    investigador, y la cantidad de investigadores que trabajen en ese área.\n7 - Recorrer la colección y generar un listado que muestre nombre y apellido, tipo de Agente y sueldo de todos los agentes, ordenado por apellido.")
        print("8 - Dada una categoría de investigación (I, II, III, IV o V), leída desde teclado, listar apellido, nombre e importe extra por docencia e investigación, de todos los docentes investigadores que poseen esa categoría, al final del listado deberá mostrar el total de dinero que la Secretaría de Investigación debe solicitar al Ministerio en concepto de importe extra que cobran los docentes investigadores de la categoría solicitada. ")
        print("9 - Almacenar los datos de todos los agentes en el archivo “Personalnew.json” ")

    def cargaJson(self,jsonF):
        objeto1 = Docente(cuil="20-3454506-8", apellido="Perez", nombre="Nicolas", sueldo=89000, anti=3,carrera="LCC", cargo="JTP", catedra="Sistemas de Informacion")
        objeto2 = Investigador(cuil="15-324235-5", apellido="Dominguez", nombre="Juan", sueldo=120000, anti=2,area="Computacional", tipo="Cientifica")
        objeto3 = PersonalApoyo(cuil="12-456543-4", apellido="Castro", nombre="Maria", sueldo=140000, anti=2,categoria="I")
        objeto4 = DocenteInvestigador(programa="I", importe=25000, cuil="18-3446706-8", apellido="Lopez",nombre="Marcos", sueldo=89000, anti=3, catedra="EyFCI", carrera="LCC",cargo="Jefe de Catedra", area="Estructuras", tipo="Teorica")
        d = objeto1.toJson()
        d1 = objeto2.toJson()
        d2 = objeto3.toJson()
        d3 = objeto4.toJson()
        lista = [d, d1, d2, d3]
        jsonF.guardarJSONArchivo(lista, "Personal.json")

    def menuOp(self):
        try:
            jsonF = ObjectEncoder()
            jsonF.decodificarDiccionario(self.__claseLista)
            manejaInterfaz = ManejaInterface()
        except:
            print("Necesita crearse el archivo, puede ingresar la opcion 1 del programa")
        self.mostrar()
        op=int(input("Ingrese una opcion 0 para terminar: "))
        while op != 0:
            os.system('cls')
            if op == 1:
                self.cargaJson(jsonF)
                jsonF.decodificarDiccionario(self.__claseLista)
                manejaInterfaz = ManejaInterface()

            elif op == 2:
                manejaInterfaz.llamaInterface(self.__claseLista,op)

            elif op == 3:
                manejaInterfaz.llamaInterface(self.__claseLista,op)

            elif op == 4:
                manejaInterfaz.llamaInterface(self.__claseLista,op)

            elif op == 5:
                self.__claseLista.listado_ordenado_porNombre()

            elif op == 6:
                self.__claseLista.cuentaAgenteInvestigadores()

            elif op == 7:
                self.__claseLista.listadoOrdenado()

            elif op == 8:
                self.__claseLista.listadoporCategoria()

            elif op == 9:
                self.__claseLista.almacenaJson(jsonF)

            self.mostrar()
            op = int(input("Ingrese una opcion 0 para terminar: "))
            os.system('cls')