from ClaseStock import Stock
import csv
class ManejaStock:
    __lista: list
    def __init__(self):
        self.__lista=[]
    def cargarLista(self):
        with open('Stock.csv','r',encoding='latin-1') as archivo:
            reader=csv.reader(archivo,delimiter=";")
            next(reader,None)
            for fila in reader:
                S=Stock(fila[0],fila[1])
                self.__lista.append(S)
            archivo.close()
    def getID(self,pos):
        return self.__lista[pos].getCod()
    def getStock(self,pos):
        return self.__lista[pos].getStock()
    def apartado3(self):
        cod=int(input("Ingrese un codigo de producto entre 1 y {}: ".format(len(self.__lista))))
        ct=int(input("Ingrese la cantidad que desea comprar o vender: "))
        tipo=input("Ingrese un tipo de transaccion: C-Compra o V-Venta: ").lower()
        print("--Stock actual--")
        print(self.__lista[cod-1])
        if tipo == "c":
            self.__lista[cod-1]+=ct
        elif tipo == "v":
            self.__lista[cod-1]-=ct
        print("--Stock actualizado--")
        print(self.__lista[cod-1])
    def apartado4(self):
        for elemento in self.__lista:
            print("El codigo de producto: {}, posee un stock de: {}".format(elemento.getCod(),elemento.getStock()))