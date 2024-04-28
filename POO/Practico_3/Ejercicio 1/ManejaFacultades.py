import csv
from ClaseFacultad import Facultad
from ClaseCarrera import Carrera
class ManejaFacultades:
    __listaF: list[Facultad]
    def __init__(self):
        self.__listaF=[]
    def carga_lista(self):
        with open('Facultades.csv', 'r', encoding='utf8') as archivo:
            reader=csv.reader(archivo,delimiter=",")
            cod=-1
            for fila in reader:
                if int(fila[0]) == cod:
                    C=Carrera(fila[1],fila[2],fila[3],fila[4],fila[5])
                    self.__listaF[cod-1].agrega_obj(C)
                else:
                    cod=int(fila[0])
                    F=Facultad(cod,fila[1],fila[2],fila[3],fila[4],fila[5])
                    self.__listaF.append(F)
            archivo.close()
    def listado(self):
        for elementoI in self.__listaF:
            lista=elementoI.get_lista()
            print("--Facultad--")
            print(elementoI)
            print("--Carreras--")
            for elementoJ in lista:
                print(elementoJ)
    def informa_facu(self,cod):
        lista=self.__listaF[cod-1].get_lista()
        print("Facultad: {}".format(self.__listaF[cod-1].getNom()))
        for elemento in lista:
            print("Nombre de la carrera: {}, Duracion: {}".format(elemento.getname(),elemento.getdur()))
    def informa_carrera(self,nm):
        i=0
        bandera=False
        posF=-1
        posC=-1
        while i<len(self.__listaF) and not bandera:
            j=0
            #ban=False
            lista=self.__listaF[i].get_lista()
            while j<len(lista) and not bandera:
                if lista[j].getname() == nm:
                    bandera=True
                    posF=i
                    posC=j
                else:
                    j+=1
            i+=1
        if posF != -1:
            print("Codigo de Facultad: {},Codigo de Carrera: {}, Nombre: {}, Localidad: {}".format(self.__listaF[posF].getcod(),posC+1,self.__listaF[posF].getNom(),self.__listaF[posF].getLoc()))
    def busca_prueba(self,nm):
        i=0
        band=False
        pos=-1
        while i<len(self.__listaF) and not band:
            lista=self.__listaF[i].get_lista()
            pos=lista.index(nm)
            if pos !=-1:
                band=True
            else:
                i+=1
        print("Codigo de Facultad: {},Codigo de Carrera: {}, Nombre: {}, Localidad: {}".format(
            self.__listaF[i].getcod(), pos + 1, self.__listaF[i].getNom(), self.__listaF[i].getLoc()))