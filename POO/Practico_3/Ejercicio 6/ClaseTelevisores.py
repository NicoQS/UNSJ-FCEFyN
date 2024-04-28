from ClaseAparatos import Aparato
class Televisor(Aparato):
    __tipo_pantalla: str
    __pulgadas: str
    __tipo_definicion: str
    __conexion_internet: bool

    def __init__(self,marca,model,col,pais,precio,tipo_pant,pulgad,tipo_def,conexion):
        self.__tipo_pantalla = tipo_pant
        self.__pulgadas = pulgad
        self.__tipo_definicion = tipo_def
        self.__conexion_internet = bool(conexion)
        print(conexion)
        super().__init__(marca,model,col,pais,precio)

    def __str__(self):
        return ("Aparato: Televisor, Marca: {}, Modelo: {}, Color: {}, Precio: {}, Tipo de Pantalla: {}, Pulgadas: {}, Tipo de definicion: {}, Conexion: {}".format(self.getMarca(),self.getModelo(),self.getColor(),self.getPreciobase(),self.__tipo_pantalla,self.__pulgadas,self.__tipo_definicion,self.__conexion_internet))

    def getTipopant(self):
        return self.__tipo_pantalla

    def getPulgadas(self):
        return self.__pulgadas

    def getTipodefi(self):
        return self.__tipo_definicion

    def getConexion(self):
        return self.__conexion_internet

    def getTipo(self):
        return "Televisor"

    def getImporteF(self):
        total = self.getPreciobase()
        if self.__tipo_definicion.lower() == "sd":
            total = total  + total*0.01
        elif self.__tipo_definicion.lower() == "hd":
            total = total + total * 0.02
        elif self.__tipo_definicion.lower() == "full hd":
            total = total  + total * 0.03
        if self.__conexion_internet == True:
            total = total  + total * 0.10
        return total
    def toJson(self):
            d = dict(
                __class__=self.__class__.__name__,
                __atributos__=dict(
                    marca=self.getMarca(),
                    model=self.getModelo(),
                    col=self.getColor(),
                    pais=self.getPais(),
                    precio=self.getPreciobase(),
                    tipo_pant=self.__tipo_pantalla,
                    pulgad=self.__pulgadas,
                    tipo_def=self.__tipo_definicion,
                    conexion=self.__conexion_internet
                )
            )
            return d