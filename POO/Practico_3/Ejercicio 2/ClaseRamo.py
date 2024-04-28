from ClaseFlores import Flor
class Ramo:
    __tam: str
    __flores: list[Flor]
    def __init__(self,t):
        self.__tam=t
        self.__flores=[]
    def getTam(self):
        return self.__tam
    def agregar_flor(self,flor):
        self.__flores.append(flor)
    def ct_flores(self,num):
        ct=0
        for i in range(len(self.__flores)):
            if self.__flores[i].getNum() == num:
                ct+=1
        return ct
    def flores_porTam(self):
        for i in range(len(self.__flores)):
            print(self.__flores[i])
    def getFlores(self):
        return self.__flores