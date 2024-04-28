from MonticuloBinario import ColadePrioridad
from Quirofano import Quirofano
import random

class Simulador:
    __reloj: int
    __Tsimulacion: int
    __Tllegada: int
    __ColaPacientes: ColadePrioridad
    __Quirofano: Quirofano
    __totalP: int
    __totalAtendidos: int
    
    
    def __init__(self):
        self.__reloj = 0
        self.__Tsimulacion = 60 * 8 # 8 horas
        self.__Tllegada = 30 # Llegan pacientes cada 30 minutos
        self.__ColaPacientes = ColadePrioridad(100)
        self.__Quirofano = Quirofano()
        self.__totalP = 0
        self.__totalAtendidos = 0
    
    def simular(self):
        while self.__reloj <= self.__Tsimulacion:
            self.llegaPaciente()
            self.AtencionQuirofano()
            self.__reloj += 1
        print("\nTotal de pacientes:",self.__totalP)
        print("Total de pacientes atendidos:",self.__totalAtendidos)
        print("Total de pacientes que esperaron ser atendidos:",self.__totalP - self.__totalAtendidos)
    
    def llegaPaciente(self):
        numero = random.random() # Genera un numero aleatorio entre 0 y 1
        if numero <= (1/self.__Tllegada):
            #Prioridad 1: Pacientes con mayor riesgo a 100 Pacientes con menor riesgo
            prioridad = random.randint(1,100)
            self.__ColaPacientes.insertar(prioridad)
            if not self.__Quirofano.estaLibre():
                print("El paciente con prioridad",prioridad,"debe esperar","|quirofano ocupado|")
            self.__totalP += 1
    
    def AtencionQuirofano(self):
        if self.__Quirofano.estaLibre():
            if not self.__ColaPacientes.vacio():
                prioridad = self.__ColaPacientes.eliminar()
                self.__Quirofano.ocupar()
                TiempoAtencion = random.randint(60,120) # Tiempo de atencion entre 1 y 2 horas
                self.__Quirofano.setTiempoAtencion(TiempoAtencion)
                print("\n<|> El paciente con prioridad",prioridad,"esta siendo atendido <|>\n")
                self.__totalAtendidos += 1
        else:
            self.__Quirofano.actualizar()