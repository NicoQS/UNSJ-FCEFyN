from ManejadorEquipos import ManejadorEquipos
from ManejadorJugadores import ManejadorJugadores
from ManejadorContratos import ManejadorContratos
from ClaseContrato import Contrato
import os
class Menu:
    __manejaEquipos: ManejadorEquipos
    __manejaJugadores: ManejadorJugadores
    __manejaContratos: ManejadorContratos

    def __init__(self):
        self.__manejaEquipos=ManejadorEquipos()
        self.__manejaJugadores=ManejadorJugadores()
        self.__manejaContratos=ManejadorContratos()
        self.__manejaEquipos.cargarEquipos()
        self.__manejaJugadores.cargarJugadores()

    def mostrarOp(self):
        print("1 - Generar un contrato para un jugador")
        print("2 - Consultar jugadores Contratados")
        print("3 - Consultar Contratos que vencen dentro de 6 meses")
        print("4 - Obtener importe de contratos")
        print("5 - Guardar Contratos\n")

    def apartado_1(self):
        dni_jugador=input("Ingrese DNI del jugador: ")
        club=input("Ingrese el nombre del club o equipo a generar el contrato: ")
        indice_jugador=self.__manejaJugadores.buscaJugador(dni_jugador)
        indice_equipo=self.__manejaEquipos.buscaEquipo(club)
        if indice_jugador != -1 and indice_equipo != -1:
            jugador=self.__manejaJugadores.getJugador(indice_jugador)
            equipo=self.__manejaEquipos.getEquipo(indice_equipo)
            if not self.__manejaContratos.verificar_si_hay_contrato(jugador,equipo):
                fecha_inicio=input("Ingrese la fecha de inicio del contrato(dd/mm/aaaa): ")
                fecha_fin = input("Ingrese la fecha de fin del contrato(dd/mm/aaaa): ")
                monto_men=float(input("Ingrese el monto mensual de cobro del jugador: "))
                contrato=Contrato(fecha_inicio,fecha_fin,monto_men,jugador,equipo)
                self.__manejaContratos.agregarContrato(contrato)
                os.system('cls')
                print("Contrato generado de manera correcta")
            else:
                print("Al parecer intenta añadir un contrato en el que incluye a un Jugador y un Equipo, que ya se encuentran vinculados previamente por un contrato")

    def apartado_2(self):
        dni_jugador = input("Ingrese DNI del jugador: ")
        indice_jugador = self.__manejaJugadores.buscaJugador(dni_jugador)
        if indice_jugador != -1:
            jugador=self.__manejaJugadores.getJugador(indice_jugador)
            self.__manejaContratos.consulta_jugadores_contratados(jugador)
        else:
            print("Jugador no encontrado")

    def apartado_3(self):
        club = input("Ingrese el nombre del club: ")
        indice_equipo = self.__manejaEquipos.buscaEquipo(club)
        if indice_equipo != -1:
            equipo = self.__manejaEquipos.getEquipo(indice_equipo)
            self.__manejaContratos.consulta_contratos_de_un_equipo(equipo)
    def apartado_4(self):
        club = input("Ingrese el nombre del club: ")
        indice_equipo = self.__manejaEquipos.buscaEquipo(club)
        if indice_equipo != -1:
            equipo = self.__manejaEquipos.getEquipo(indice_equipo)
            self.__manejaContratos.importe_de_contratos(equipo)
    def menuOp(self):
        self.mostrarOp()
        op=int(input("Ingrese una opcion: 0 para terminar: "))
        while op != 0:
            os.system('cls')
            if op == 1:
                self.apartado_1()
            if op == 2:
                self.apartado_2()
            if op == 3:
                self.apartado_3()
            if op == 4:
                self.apartado_4()
            if op == 5:
                self.__manejaContratos.crear_archivo()
            self.mostrarOp()
            op = int(input("Ingrese una opcion: 0 para terminar: "))
            os.system('cls')
        print("--FIN DEL PROGRAMA--")