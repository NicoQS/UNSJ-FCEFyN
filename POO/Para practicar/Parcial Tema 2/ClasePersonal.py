class Persona:
    __apell: str
    __nom: str
    __dni: str
    __edad: int
    __direcc: str
    __tel: str
    __factor: str
    __organismo: str
    def __init__(self,a,n,dn,e,direcc,tel,fac,org):
        self.__apell=a
        self.__nom=n
        self.__dni=dn
        self.__edad=int(e)
        self.__direcc=direcc
        self.__tel=tel
        self.__factor=fac
        self.__organismo=org
    def __str__(self):
        return ("Apellido y Nombre: {}, DNI: {}, Edad: {}, Factor de riesgo: {}, Organismo: {}".format(self.__apell+" "+self.__nom,self.__dni,self.__edad,self.__factor,self.__organismo))
    def getEdad(self):
        return self.__edad
    def getFactor(self):
        return self.__factor
    def getOrga(self):
        return self.__organismo
    def getApell(self):
        return self.__apell
    def __lt__(self, other):
        return self.__apell < other.__apell