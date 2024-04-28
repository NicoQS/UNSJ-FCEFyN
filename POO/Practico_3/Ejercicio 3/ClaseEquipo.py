class Equipo:
    __nombre: str
    __ciudad: str
    __contratos: list

    def __init__(self,nom,ciudad):
        self._validar_string(nom)
        self._validar_string(ciudad)

        self.__nombre=nom
        self.__ciudad=ciudad
        self.__contratos=[]

    def __str__(self):
        return ("Nombre: {}, Ciudad: {}".format(self.__nombre,self.__ciudad))

    def _validar_string(self,dato):
        if type(dato) != str:
            raise TypeError("Se esperaba una cadena")

    def _validar_contrato(self,dato):
        from ClaseContrato import Contrato
        if type(dato) != Contrato:
            raise TypeError("Se esperaba un contrato")

    def agregarContrato(self,contrato):
        self._validar_contrato(contrato)
        self.__contratos.append(contrato)

    def getNombre(self):
        return self.__nombre

    def getCiudad(self):
        return self.__ciudad

    def getContratos(self):
        contrats=None
        if len(self.__nombre) != 0:
            contrats=self.__contratos
        return contrats