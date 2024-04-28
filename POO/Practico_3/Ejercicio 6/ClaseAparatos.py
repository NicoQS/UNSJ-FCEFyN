class Aparato:
    __marca: str
    __modelo: str
    __color: str
    __pais_de_fabricacion: str
    __precio_base: float
    def __init__(self,marca,model,col,pais,precio):
        self.__marca = marca
        self.__modelo = model
        self.__color = col
        self.__pais_de_fabricacion = pais
        self.__precio_base = float(precio)

    def getMarca(self):
        return self.__marca

    def getModelo(self):
        return self.__modelo

    def getColor(self):
        return self.__color

    def getPais(self):
        return self.__pais_de_fabricacion

    def getPreciobase(self):
        return self.__precio_base