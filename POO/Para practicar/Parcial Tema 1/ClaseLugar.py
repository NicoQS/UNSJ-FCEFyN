class Lugar:
    __zona: str
    __lugar: str
    def __init__(self,z,l):
        self.__zona=z
        self.__lugar=l
    def __str__(self):
        return("Zona: {}, Lugar: {}".format(self.__zona,self.__lugar))
