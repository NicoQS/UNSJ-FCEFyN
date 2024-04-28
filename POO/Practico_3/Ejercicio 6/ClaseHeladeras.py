from ClaseAparatos import Aparato
class Heladera(Aparato):
    __capacidadLit: int
    __freezer: bool
    __ciclica: bool

    def __init__(self,marca,model,col,pais,precio,capacidad,freezer,cicl):
        self.__capacidad = int(capacidad)
        self.__freezer = bool(freezer)
        self.__ciclica = bool(cicl)
        super().__init__(marca,model,col,pais,precio)

    def __str__(self):
        return ("Aparato: Heladera, Marca: {}, Modelo: {}, Color: {}, Precio: {}, Capacidad: {}, Freezer: {}, Ciclica: {}".format(self.getMarca(),self.getModelo(),self.getColor(),self.getPreciobase(),self.__capacidad,self.__freezer,self.__ciclica))
    def getCapacidadlit(self):
        return self.__capacidadLit

    def getFreezer(self):
        return self.__freezer

    def getCiclica(self):
        return self.__ciclica

    def getImporteF(self):
        total = self.getPreciobase()
        if self.__freezer == False:
            total = total + total*0.01
        elif self.__freezer == True:
            total = total  + total*0.05
        elif self.__ciclica == True:
            total = total  + total*0.10
        return total
    def getTipo(self):
        return "Heladera"
    def toJson(self):
            d = dict(
                __class__=self.__class__.__name__,
                __atributos__=dict(
                    marca=self.getMarca(),
                    model=self.getModelo(),
                    col=self.getColor(),
                    pais=self.getPais(),
                    precio=self.getPreciobase(),
                    capacidad=self.__capacidad,
                    freezer=self.__freezer,
                    cicl=self.__ciclica,
                )
            )
            return d