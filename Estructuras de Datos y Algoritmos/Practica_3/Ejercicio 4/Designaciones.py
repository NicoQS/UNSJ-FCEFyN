class Designacion:
    __anio: int
    __justicia: str
    __cargo: str
    __instancia: str
    __materia: str
    __ct_varones: int
    __ct_mujeres: int
    
    def __init__(self, anio, justicia, cargo, instancia,materia ,ct_varones, ct_mujeres):
        self.__anio = int(anio)
        self.__justicia = justicia
        self.__cargo = cargo
        self.__materia = materia
        self.__instancia = instancia
        self.__ct_varones = int(ct_varones)
        self.__ct_mujeres = int(ct_mujeres)
    
    def getAnio(self):
        return self.__anio
    
    def getJusticia(self):
        return self.__justicia
    
    def getMateria(self):
        return self.__materia

    def getCargo(self):
        return self.__cargo
    
    def getInstancia(self):
        return self.__instancia
    
    def getCtVarones(self):
        return self.__ct_varones
    
    def getCtMujeres(self):
        return self.__ct_mujeres