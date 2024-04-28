class Conjunto:
    __lista: list
    def __init__(self,lista):
        self.__lista=lista
    def __add__(self,otro):
        result=[]
        for i in self.__lista:
            result.append(i)
        for i in otro.__lista:
            if i not in result:
                result.append(i)
        return Conjunto(result)
    def __str__(self):
        return str(self.__lista)
    def __sub__(self, otro):
        result=[]
        for i in self.__lista:
            if i not in otro.__lista:
                result.append(i)
        return Conjunto(result)
    def __eq__(self, otro):
        if len(self.__lista) != len(otro.__lista):
            return False
        for i in self.__lista:
            if i not in otro.__lista:
                return False
        return True

