from ClaseNodo import Nodo

class Paciente:
    __nombre: str
    __DNI: str
    __especialidad: str
    
    def __init__(self,nom,dni,esp):
        self.__nombre = nom
        self.__DNI = dni
        self.__especialidad = esp
    
    def getEspecialidad(self):
        return self.__especialidad

    def getNombre(self):
        return self.__nombre
#----------------------------------------------------------------------------------------------

class Especialidad: #Cola enlazada
    __nombre: str
    __primero: Nodo
    __ultimo: Nodo
    __cantidad: int
    __tiempoEspera: int
    
    def __init__(self,nom):
        self.__nombre = nom
        self.__cantidad = 0
        self.__primero = None
        self.__ultimo = None
        self.__tiempoEspera = 0
    
    def agregarTurno(self,elemento):
        nuevaNodo = Nodo(elemento)
        if self.__cantidad < 10:
            if self.Vacia():
                self.__primero = nuevaNodo
            else:
                self.__ultimo.setSiguiente(nuevaNodo)
            self.__ultimo = nuevaNodo
            self.__cantidad += 1
        else:
            print("No se pueden anotar mas pacientes")

    def Vacia(self):
        return self.__primero == None
    
    def finTurno(self):
        if not self.Vacia():
            aux = self.__primero
            self.__primero = self.__primero.getSiguiente()
            if self.__primero == None:
                self.__ultimo = None
            print("El paciente "+aux.getDato().getNombre()+" ha terminado su turno")
            del aux
            self.__cantidad -= 1
        else:
            print("No hay personas en la cola")
    
    def getCantidad(self):
        return self.__cantidad
    
    def getNombreEsp(self):
        return self.__nombre
    
    def recorrer(self):
        aux=self.__primero
        while aux != None:
            print(aux.getDato())
            aux=aux.getSiguiente()
    #def  get(self,pos):
        
    def acumulaTiempo(self):
        self.__tiempoEspera += self.__cantidad

    def getTiempo(self):
        return self.__tiempoEspera
#----------------------------------------------------------------------------------------------

class Hospital:
    __especialidades: list
    
    def __init__(self):
        self.__especialidades = [
            Especialidad("Cardiologia"),
            Especialidad("Pediatria"),
            Especialidad("Ginecologia"),
            Especialidad("Odontologia")
            ]
    
    def anotarPaciente(self,paciente):
        especialidad = paciente.getEspecialidad()-1
        self.__especialidades[especialidad].agregarTurno(paciente)
        
    def pacientesAtendidos(self):
        for elem in self.__especialidades:
            elem.finTurno()

    def getEspecialidad(self,esp):
        return self.__especialidades[esp].getNombreEsp()
    
    def getTiempoEspera(self):
        Tiempo = 0
        for elem in self.__especialidades:
            Tiempo += elem.getCantidad()
        return Tiempo

    def calcularPromedioEspecialidad(self):
        for elem in self.__especialidades:
            elem.acumulaTiempo()
    
    def getPromedioEspecialidad(self):
        print("B ) Promedio de espera por especialidad ")
        for elem in self.__especialidades:
            print(elem.getCantidad())
            if elem.getCantidad() != 0:
                print("Para la especialidad {}, el tiempo de espera promedio es: {}".format(elem.getNombreEsp(),elem.getTiempo()/elem.getCantidad()))
            else:
                print("Para la especialidad {}, no hay pacientes en la cola".format(elem.getNombreEsp()))