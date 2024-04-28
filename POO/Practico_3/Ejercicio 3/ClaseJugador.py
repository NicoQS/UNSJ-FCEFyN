import datetime
class Jugador:
    __nombre: str
    __DNI: str
    __ciudadnat: str
    __paisorigen: str
    __fechanac: datetime
    __contratos: list

    def __init__(self,dni,nom,ciudad,pais,fecha):
        self._validar_string(nom)
        self._validar_string(dni)
        self._validar_string(ciudad)
        self._validar_string(pais)
        self.__nombre=nom
        self.__DNI=dni
        self.__ciudadnat=ciudad
        self.__paisorigen=pais
        self.__fechanac=self.setDate(fecha)
        self.__contratos=[]

    def __str__(self):
        return ("Nombre: {}, DNI: {}, Ciudad Natal: {}, Pais de origen: {}, Fecha de nacimiento: {}".format(self.__nombre,self.__DNI,self.__ciudadnat,self.__paisorigen,self.__fechanac))

    def setDate(self,cadena:str):
        fecha=datetime.datetime.strptime(cadena,"%d/%m/%Y").date()
        return fecha

    def _validar_string(self,dato):
        if type(dato) != str:
            raise TypeError("Se esperaba un tipo de dato string")

    def _validar_fecha(self,dato):
        if type(dato) != datetime:
            raise TypeError("Se esperaba una fecha")

    def _validar_contrato(self,contrato):
        from ClaseContrato import Contrato
        if type(contrato) != Contrato:
            raise TypeError("Se esperaba un contrato")

    def agregarContrato(self,contrato):
        self._validar_contrato(contrato)
        self.__contratos.append(contrato)

    def getDNI(self):
        return self.__DNI

    def getNombre(self):
        return self.__nombre

    def getContratos(self):
        contrats=None
        if len(self.__contratos) != 0:
            contrats=self.__contratos
        return contrats