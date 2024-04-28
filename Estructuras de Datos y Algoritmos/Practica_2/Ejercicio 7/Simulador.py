from ColaEncadenada import ColaEncadenada
import random

class Simulador:
    __cola: ColaEncadenada
    __frecuenciaLlegada: int
    __tAtencion: int
    __tSimulacion: int
    __tActualCajero:int
    __reloj: int
    __maximo: int
    
    
    def __init__(self,tSim,tAten,frecuenciaLleg) -> None:
        self.__tSimulacion = tSim
        self.__tAtencion = tAten
        self.__frecuenciaLlegada = frecuenciaLleg
        self.__tActualCajero = tAten + 1
        self.__maximo = -1
        self.__reloj = 0
        self.__cola = ColaEncadenada()
    
    def simular(self):
        while self.__reloj <= self.__tSimulacion:
            self.ingresaCliente()
            self.cajero()
            self.__reloj += 1
        print("El tiempo maximo de espera de un cliente fue de: {} minutos".format(self.__maximo))
    
    def ingresaCliente(self):
        numero = random.random()
        if numero <= (1/self.__frecuenciaLlegada):
            self.__cola.insertar(self.__reloj)
    
    def cajero(self):
        if self.__tActualCajero == self.__tAtencion + 1:
            if self.__cola.Vacia() == False:
                tiempo = self.__reloj - self.__cola.suprimir()
                self.__tActualCajero = self.__tAtencion
                if tiempo > self.__maximo:
                    self.__maximo = tiempo
        else:
            self.__tActualCajero -= 1
            if self.__tActualCajero == 0:
                self.__tActualCajero = self.__tAtencion +1