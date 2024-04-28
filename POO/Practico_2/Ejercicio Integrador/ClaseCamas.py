class cama:
    __id: int
    __habitacion: int
    __estado : bool
    __NyA : str
    __diagnostico : str
    __fecha_de_int : str
    __fecha_alta : str =None
    def __init__(self,id,hab,est,nya,diag,fecha):
        self.__id=int(id)
        self.__habitacion=int(hab)
        self.__estado=bool(est)
        self.__NyA=nya
        self.__diagnostico=diag
        self.__fecha_de_int=fecha
    def set_alta(self,dia):
        self.__fecha_alta=dia
        self.__estado=False
    def __str__(self):
        return ("Cama: {} - Habitacion: {} - NyA: {} - Diagnostico: {} - Fecha de Internacion: {}".format(self.__id,self.__habitacion,self.__NyA,self.__diagnostico,self.__fecha_de_int))
    def get_nom(self):
        return self.__NyA
    def get_habitacion(self):
        return self.__habitacion
    def get_diag(self):
        return self.__diagnostico
    def get_internacion(self):
        return self.__fecha_de_int
    def get_fecha_alt(self):
        return self.__fecha_alta
    def get_cama(self):
        return self.__id
    def get_estado(self):
        return self.__estado