class Producto:
    __codigo: int
    __descrip: str
    __precioU: float
    def __init__(self,c,d,p):
        self.__codigo=int(c)
        self.__descrip=d
        self.__precioU=float(p)
    def __str__(self):
        return ("Codigo: {}, Descripcion: {}, Precio Unitario: {}".format(self.__codigo,self.__descrip,self.__precioU))
    def getCode(self):
        return self.__codigo
    def getPrecio(self):
        return self.__precioU
    def getDescrip(self):
        return self.__descrip
    def __lt__(self, other):
        return self.__descrip < other.__descrip