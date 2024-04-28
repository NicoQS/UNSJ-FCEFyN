from ClaseAparatos import Aparato
class Lavarropa(Aparato):
    __capacidad: int
    __velocidad: int
    __ct_program: int
    __tipo_de_carga: str

    def __init__(self,marca,model,col,pais,precio,capacidad,velocidad,ct,tipo):
        self.__capacidad = int(capacidad)
        self.__velocidad = int(velocidad)
        self.__ct_program = int(ct)
        self.__tipo_de_carga = tipo
        super().__init__(marca,model,col,pais,precio)
    def __str__(self):
        return ("Aparato: Lavarropa, Marca: {}, Modelo: {}, Color: {}, Precio: {}, Capacidad: {}Kg, Velocidad: {}, Cantidad de programas: {}, Tipo {}".format(self.getMarca(),self.getModelo(),self.getColor(),self.getPreciobase(),self.__capacidad,self.__velocidad,self.__ct_program,self.__tipo_de_carga))
    def getCapacidad(self):
        return self.__capacidad

    def getVelocidad(self):
        return self.__velocidad

    def getCtprogram(self):
        return self.__ct_program

    def getTipocarga(self):
        return self.__tipo_de_carga

    def getTipo(self):
        return "Lavarropa"

    def getImporteF(self):
        total = self.getPreciobase()
        if self.__capacidad <= 5:
            total = total + total*0.01
        elif self.__capacidad > 5:
            total = total  + total*0.03
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
                    capacidad=self.__capacidad,
                    velocidad=self.__velocidad,
                    ct=self.__ct_program,
                    tipo=self.__tipo_de_carga
                )
            )
            return d