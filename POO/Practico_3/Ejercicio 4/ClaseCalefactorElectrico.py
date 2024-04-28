from ClaseCalefactor import Calefactor
class CalefactorElectrico(Calefactor):
    __potencia: int

    def __init__(self,marca,modelo,potencia):
        self.__potencia=int(potencia)
        super().__init__(marca,modelo)

    def __str__(self):
        return ("Calefactor electrico, Marca: {}, Modelo: {}, Potencia: {}".format(super().getMarca(),super().getModelo(),self.__potencia))
    def getPotencia(self):
        return self.__potencia

    def getTipoE(self):
        cadena = "Calefactor a Gas"
        return cadena