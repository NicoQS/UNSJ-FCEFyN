class medicamento:
    __idCama : int
    __idMedica : int
    __nombreCom: str
    __monodrog : str
    __presentacion : str
    __ct_aplic: int
    __precio : float
    def __init__(self,idcam,idmed,nombrecom,mono,presen,ctaplic,precio):
        self.__idCama=int(idcam)
        self.__idMedica=int(idmed)
        self.__nombreCom=nombrecom
        self.__monodrog=mono
        self.__presentacion=presen
        self.__ct_aplic=int(ctaplic)
        self.__precio=float(precio)
    def __str__(self):
        return ("ID: {} - IDMedicamento: {} - Nombre: {} - Monodroga: {} - Presentacion: {} - Cantidad: {} - Precio: {}".format(self.__idCama,self.__idMedica,self.__nombreCom,self.__monodrog,self.__presentacion,self.__ct_aplic,self.__precio))
    def get_idcam(self):
        return self.__idCama
    def get_nom(self):
        return self.__nombreCom
    def get_mono(self):
        return self.__monodrog
    def get_pres(self):
        return self.__presentacion
    def get_precio(self):
        return self.__precio
    def get_ct(self):
        return self.__ct_aplic