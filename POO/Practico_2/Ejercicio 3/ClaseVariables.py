from numpy import true_divide


class variables:
    __temp=""
    __humedad=""
    __presion=""
    def __init__(self,temperatura,humedad,presion):
        self.__temp=float(temperatura)
        self.__humedad=int(humedad)
        self.__presion=float(presion)
    def get_temp(self):
        return (self.__temp)
    def get_hum(self):
        return (self.__humedad)
    def get_pre(self):
        return (self.__presion)