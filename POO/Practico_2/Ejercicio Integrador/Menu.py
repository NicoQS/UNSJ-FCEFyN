from ManejadorCamas import ManejadorCamas
from ManejadorMedicamentos import ManejadorMedicamentos
class Menu:
    __instancia_camas: ManejadorCamas
    __instancia_medicamentos: ManejadorMedicamentos
    def __init__(self):
        self.__instancia_camas=ManejadorCamas()
        self.__instancia_medicamentos=ManejadorMedicamentos()
        #self.__instancia_camas.cargar_objetos()
        self.__instancia_medicamentos.cargarlista()
    def mostrar_op(self):
        print ("\n1-Mostrar Camas")
        print ("2- Mostrar medicamentos")
        print("3  -Dado un el nombre y apellido de un paciente internado al que se le da el alta, listará los datos del paciente y los medicamentos que deberá devolver ")
        print("4 - Listado de los datos de pacientes internados (cama ocupada), que tienen un diagnóstico leído desde teclado.")
    def funcion_3 (self):
        b=self.__instancia_camas.busca(input("Ingrese el nombre del paciente (Ejemplo: Quiroga, Juan): "))
        if b !=-1:
            self.__instancia_camas.alta(input("Ingrese la fecha de alta: "),b)
            self.__instancia_camas.muestra_paciente(b)
            id=self.__instancia_camas.get_id(b)
            self.__instancia_medicamentos.prueba_listado(id)
        else:
            print ("No se encuentra el paciente ingresado")
    def Menu_opciones(self):
        self.mostrar_op()
        op=int(input("Ingrese una opcion 0 para salir: "))
        while op != 0:
            if op == 1:
                self.__instancia_camas.mostrar()
            if op == 2:
                self.__instancia_medicamentos.mostrar()
            if op == 3:
                self.funcion_3()
            if op == 4:
                self.__instancia_camas.listado_internados()
            self.mostrar_op()
            op = int(input("Ingrese una opcion 0 para salir: "))
        print("--FIN--")