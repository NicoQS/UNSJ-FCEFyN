class Recibe:
    __id: int
    __fecha: str
    __producto: str
    __marca: str
    __problema: str
    __observacion: str
    def __init__(self,id,fe,pro,marca,problem,ob):
        self.__id=int(id)
        self.__fecha=fe
        self.__producto=pro
        self.__marca=marca
        self.__problema=problem
        self.__observacion=ob
    def __str__(self):
        return ("Marca: {},ID: {},Fecha: {}, Producto: {}, Problema: {}, Observacion: {}".format(self.__marca,self.__id,self.__fecha,self.__producto,self.__problema,self.__observacion))
    def getID(self):
        return self.__id
    def getMarca(self):
        return self.__marca
    def __gt__(self, other):
        return self.__marca > other.__marca