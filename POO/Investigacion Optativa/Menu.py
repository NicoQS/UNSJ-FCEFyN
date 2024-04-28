from ManejadorProyectos import ManejadorProyectos
from ManejadorIntegrantes import ManejadorIntegrantes
class Menu:
    __instanciaProyectos: ManejadorProyectos
    __instanciaIntegrantes: ManejadorIntegrantes
    __IDs: list
    def __init__(self):
        self.__instanciaProyectos=ManejadorProyectos()
        self.__instanciaIntegrantes = ManejadorIntegrantes()
        self.__instanciaProyectos.carga_lista()
        self.__IDs=self.__instanciaProyectos.IDs()
    def mostrar(self):
        print("1- Lista de Proyectos")
        print("2- Lista de Integrantes")
        print ("3- Listado de proyectos ordeandos de mayor a menor por puntaje")
    def funcion_A(self):
        for i in range(len(self.__IDs)):
            ct=self.__instanciaIntegrantes.Ct_Integrantes(self.__IDs[i])
            if ct >= 3:
                self.__instanciaProyectos.puntaje(i,10)
            else:
                print("El proyecto {} debe tener como minimo 3 integrantes".format(self.__IDs[i]))
                self.__instanciaProyectos.puntaje(i,-20)
    def funcion_B_a_F(self):
        for i in range(len(self.__IDs)):
            b1=self.__instanciaIntegrantes.buscaDir_cat(self.__IDs[i])
            b2=self.__instanciaIntegrantes.buscaCodir_cat(self.__IDs[i])
            if b1 != "No-cate":
                if b1=="I" or b1=="II":
                    self.__instanciaProyectos.puntaje(i,10)
                else:
                    print("El Director del Proyecto {} debe tener categoria I o II".format(self.__IDs[i]))
                    self.__instanciaProyectos.puntaje(i,-5)
            else:
                print("El Proyecto {} debe tener un Director".format(self.__IDs[i]))
                self.__instanciaProyectos.puntaje(i, -10)
            if b2 != "No-cate":
                    if b2 == "I" or b2=="II" or b2=="III":
                        self.__instanciaProyectos.puntaje(i, 10)
                    else:
                        print("El CoDirector del Proyecto {} debe tener categoria como minimo de III".format(self.__IDs[i]))
                        self.__instanciaProyectos.puntaje(i, -5)
            else:
                print("El Proyecto {} debe tener un CodDirector".format(self.__IDs[i]))
                self.__instanciaProyectos.puntaje(i,-10)
    def Menu_1(self):
        self.mostrar()
        op=int(input("Ingrese una opcion: 0 para terminar:"))
        while op != 0:
            if op == 1:
                self.__instanciaProyectos.mostrar_proy()
            elif op == 2:
                self.__instanciaIntegrantes.mostrar_inte()
            elif op == 3:
                self.funcion_A()
                self.funcion_B_a_F()
                self.__instanciaProyectos.ordenamiento()
            self.mostrar()
            op = int(input("Ingrese una opcion: 0 para terminar:"))