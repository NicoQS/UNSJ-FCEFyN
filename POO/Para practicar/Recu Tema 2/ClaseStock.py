class Stock:
    __cod: int
    __canti: int
    def __init__(self,c,cant):
        self.__cod=int(c)
        self.__canti=int(cant)
    def __str__(self):
        return ("Codigo: {}, Cantidad: {}".format(self.__cod,self.__canti))
    def getCod(self):
        return self.__cod
    def getStock(self):
        return self.__canti
    def __add__(self, other):
        self.__canti+=other
        return self
    def __sub__(self, other):
        if self.__canti >= other:
            self.__canti-=other
        else:
            print("El local no posee el producto con el stock ingresado para vender")
        return self