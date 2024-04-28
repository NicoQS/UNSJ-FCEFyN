class Flor:
    __num: int
    __nom: str
    __color: str
    __descrip: str
    def __init__(self,num,nom,col,des):
        self.__num=int(num)
        self.__nom=nom
        self.__color=col
        self.__descrip=des
    def __str__(self):
        return ("Numero: {}, Nombre: {}, Color: {}, Descripcion: {}".format(self.__num,self.__nom,self.__color,self.__descrip))
    def getNom (self):
        return self.__nom
    def  getNum(self):
        return self.__num
    def getCol(self):
        return self.__color