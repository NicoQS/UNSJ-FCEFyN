from ClaseCarrera import Carrera
class Facultad:
    __code: int
    __Nombre: str
    __direcc: str
    __localidad: str
    __tel: str
    __carreras: list[Carrera]
    def __init__(self,cd,nom,dir,loc,prov,tel):
        self.__code=cd
        self.__Nombre=nom
        self.__direcc=dir
        self.__localidad=loc+", "+prov
        self.__tel=tel
        self.__carreras=[]
    def agrega_obj(self,objeto):
        self.__carreras.append(objeto)
    def __str__(self):
        return ("Codigo: {}, Nombre: {}, Direccion: {}, Localidad: {}, Tel: {}".format(self.__code,self.__Nombre,self.__direcc,self.__localidad,self.__tel))
    def get_lista(self):
        return self.__carreras
    def getNom(self):
        return self.__Nombre
    def getLoc(self):
        return self.__localidad
    def getcod(self):
        return self.__code