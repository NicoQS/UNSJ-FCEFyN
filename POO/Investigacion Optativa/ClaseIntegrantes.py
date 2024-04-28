class Integrante:
    __IDP: str
    __NyA: str
    __DNI: str
    __categoria: str
    __rol: str
    def __init__(self,id,nya,dni,cat,rol):
        self.__IDP=id
        self.__NyA=nya
        self.__DNI=dni
        self.__categoria=cat
        self.__rol=rol
    def __str__(self):
        return ("ID: {}, NyA: {}, DNI: {}, Categoria: {}, Rol: {}".format(self.__IDP,self.__NyA,self.__DNI,self.__categoria,self.__rol))
    def get_ID_int(self):
        return self.__IDP
    def get_rol(self):
        return self.__rol
    def get_cat(self):
        return self.__categoria