class Organo:
    __nom: str
    __domic: str
    __loc : str
    __tel : str
    def __init__(self,nom,domic,loc,tel):
        self.__nom=nom
        self.__domic=domic
        self.__loc=loc
        self.__tel=tel
    def __str__(self):
        return ("Nombre: {}, Domicilio: {}, Localidad: {}, Telefono: {}".format(self.__nom,self.__domic,self.__loc,self.__tel))
    def getNomorg(self):
        return self.__nom