class Entrega:
    __fecha: str
    __id: int
    __detalle: str
    __monto : float
    def __init__(self,f,id,det,mon):
        self.__fecha=f
        self.__id=int(id)
        self.__detalle=det
        self.__monto=float(mon)
    def __str__(self):
        return ("Fecha de entrega: {}, ID: {}, Detalle: {}, Monto: {}$".format(self.__fecha,self.__id,self.__detalle,self.__monto))
    def getId(self):
        return self.__id
    def getMonto(self):
        return self.__monto