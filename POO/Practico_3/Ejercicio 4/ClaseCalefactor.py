class Calefactor:
    __marca: str
    __modelo: str

    def __init__(self,mar,mol):
        self.__marca=mar
        self.__modelo=mol

    def getMarca(self):
        return self.__marca

    def getModelo(self):
        return self.__modelo