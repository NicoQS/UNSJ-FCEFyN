from ClaseEquipo import Equipo
from ClaseJugador import Jugador
import datetime
class Contrato:
    __fechaInic: datetime
    __fechaFin: datetime
    __pagoMens: float
    __jugador: Jugador
    __equipo: Equipo

    def __init__(self,inicio,fin,pago,jugador=None,equipo=None):
        self.__fechaInic=self.setDate(inicio)
        self.__fechaFin=self.setDate(fin)
        self.__pagoMens=float(pago)
        self.__jugador=jugador
        self.__jugador.agregarContrato(self)
        self.__equipo=equipo
        self.__equipo.agregarContrato(self)

    def setDate(self,cadena:str):
        fecha=datetime.datetime.strptime(cadena,"%d/%m/%Y").date()
        return fecha
    def __str__(self):
        return ("- Jugador [{}]\n- Equipo - [{}]\n- Fecha de Inicio: [{}]\n- Fecha de fin: [{}]\n- Pago mensual: $ {}".format(self.__jugador,self.__equipo,self.__fechaInic,self.__fechaFin,self.__pagoMens))

    def getFechain(self):
        return self.__fechaInic

    def getFechafin(self):
        return self.__fechaFin

    def getJugador(self):
        return self.__jugador

    def getEquipo(self):
        return self.__equipo

    def  getPago(self):
        return self.__pagoMens