from ClaseCalefactor import Calefactor
class CalefactorGas(Calefactor):
    __matricula: str
    __calorias: int

    def __init__(self,marca,modelo,matricula,calorias):
        self.__matricula=matricula
        self.__calorias=int(calorias)
        super().__init__(marca,modelo)

    def __str__(self):
        return ("Calefactor a gas, Marca: {}, Modelo: {}, Matricula: {}, Calorias: {}".format(super().getMarca(),super().getModelo(),self.__matricula,self.__calorias))

    def getMatricula(self):
        return self.__matricula

    def getCalorias(self):
        return self.__calorias

    def getTipoG(self):
        cadena="Calefactor a Gas"
        return cadena