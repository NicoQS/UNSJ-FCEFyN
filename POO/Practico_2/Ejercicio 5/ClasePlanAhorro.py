class PlanAhorro:
    __cod=int
    __modelo=""
    __version=""
    __precio=float
    __cuotas=0
    __ct_cuot_lic=0
    def __init__(self,codigo,mod,ver,pre):
        self.__cod=int(codigo)
        self.__modelo=mod
        self.__version=ver
        self.__precio=float(pre)
    def get_cod(self):
        return self.__cod
    def get_mod(self):
        return self.__modelo
    def get_ver(self):
        return self.__version
    def get_pre(self):
        return self.__precio
    def modifica_precio(self,actual):
        self.__precio=actual
        print("El precio se modifico a: "+ str(self.__precio))
    def __str__(self):
        return  (str(self.__cod)+ " " + self.__modelo+ " " + self.__version + " "+ str(self.__precio))
    def getvalor(self):
        return  float((self.__precio/self.__cuotas) + self.__precio * 0.10)
    def getMonto_a_lic(self):
        return float(self.__ct_cuot_lic*self.getvalor())
    @classmethod
    def get_cuot_lic(cls):
        return cls.__ct_cuot_lic
    @classmethod
    def modifica(cls,ct):
        cls.__ct_cuot_lic=int(ct)
    @classmethod
    def cuotas(cls,cuotas,licitar):
        cls.__cuotas=int(cuotas)
        cls.__ct_cuot_lic=int(licitar)