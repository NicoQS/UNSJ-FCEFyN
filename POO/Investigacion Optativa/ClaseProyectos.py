class Proyecto:
    __idProyecto: str
    __Titulo: str
    __palabrasClave: str
    __Puntos: int =0

    def __init__(self, id, tit, palabras):
        self.__idProyecto = id
        self.__Titulo = tit
        self.__palabrasClave = palabras
        self.__Puntos=0

    def __str__(self):
        return ("Puntaje: {}, ID :{}, Titulo: {}, Palabras Claves: {}".format(self.__Puntos,self.__idProyecto, self.__Titulo, self.__palabrasClave))
    def get_ID(self):
        return self.__idProyecto
    def puntos(self,ct):
        self.__Puntos+=ct
    def muestrapuntos(self):
        return self.__Puntos
    def __gt__(self, other):
        return self.__Puntos > other.__Puntos
