class Carrera:
    __cod: int
    __nom: str
    __tipo: str
    __duracion: str
    __tit: str
    def __init__(self,cd,nm,tip,dur,t=""):
        self.__cod= int(cd)
        self.__nom=nm
        self.__tipo=tip
        self.__duracion=dur
        self.__tit=t
    def __str__(self):
        return ("Codigo: {}, Nombre: {}, Tipo: {}, Duracion: {}, Titulo: {}".format(self.__cod,self.__nom,self.__tipo,self.__duracion,self.__tit))
    def getname(self):
        return self.__nom
    def getdur(self):
        return self.__duracion
    def getCod(self):
        return self.__cod
    def __cmp__(self, other):
        return self.__nom==other