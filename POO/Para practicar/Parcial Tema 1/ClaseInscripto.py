class Inscripto:
    __apell: str
    __nom: str
    __dni: str
    __edad: int
    __tel: str
    __zona: str
    __factor: str
    __prioridad: int
    def __init__(self,a,n,d,e,t,z,f):
        self.__apell=a
        self.__nom=n
        self.__dni=d
        self.__edad=int(e)
        self.__tel=t
        self.__zona=z
        self.__factor=f
        self.__prioridad=int(e)
    def __str__(self):
        return("Apellido y Nombre: {}, DNI: {}, Edad: {},Telefono: {}, Zona: {}, Factor: {}, Prioridad: {}".format(self.__apell+" "+self.__nom,self.__dni,self.__edad,self.__tel,self.__zona,self.__factor,self.__prioridad))
    def prioridad(self,ct):
        self.__prioridad+=ct
    def getFactor(self):
        return self.__factor
    def getEdad(self):
        return self.__edad
    def getZona(self):
        return self.__zona
    def __gt__(self, other):
        return self.__prioridad > other.__prioridad