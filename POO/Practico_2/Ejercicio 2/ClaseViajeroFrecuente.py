class ViajeroFrecuente:
    __num_viajero= ""
    __dni= ""
    __nombre=""
    __apellido= ""
    __millas_acum=""
    def __init__(self,numviaj,DNI,nombre,apellido,millacum):
        self.__num_viajero=int(numviaj)
        self.__dni=DNI
        self.__nombre=nombre
        self.__apellido=apellido
        self.__millas_acum=int(millacum)
    def cantidadTotaldeMillas(self):
        return self.__millas_acum
    def acumularMillas (self,cant):
        self.__millas_acum+=cant
        return self.__millas_acum
    def  canjearMillas(self,ct_canje):
        if ct_canje <= self.__millas_acum:
            self.__millas_acum-=ct_canje
            return self.__millas_acum
        else:
            return print ("Error en la operacion")
    def getNumViajero(self):
        return self.__num_viajero
