import random

names=['Mark', 'Sam', 'Henry','Marcos', 'Juan', 'Martin','Nico', 'Samanta']
class Paciente:
    __nombre: str
    __DNI: str
    __especialidad: str
    __tiempoEspera: int
    
    def __init__(self,espera):
        self.__nombre = random.choice(names)
        self.__DNI = random.randrange(1500000,5500000)
        self.__especialidad = random.randint(0,3)
        self.__tiempoEspera = espera
    
    def getEspecialidad(self):
        return self.__especialidad

    def getNombre(self):
        return self.__nombre

    def getTiempoEspera(self):
        return self.__tiempoEspera

    def setTiempoDeEspera(self,espera):
        self.__tiempoEspera = espera