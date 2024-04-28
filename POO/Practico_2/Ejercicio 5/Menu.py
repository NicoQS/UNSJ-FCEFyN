class Menu:
    __lista=None
    def __init__(self,lista):
        self.__lista=lista
    def actualizar(self):
        for i in range(len(self.__lista)):
            print ("Codigo {}, Modelo {}, Version {}".format(self.__lista[i].get_cod(),self.__lista[i].get_mod(),self.__lista[i].get_ver()))
            actual=int(input("Ingrese el precio actual: "))
            self.__lista[i].modifica_precio(actual)
    def opcion2(self):
        valor=float(input("Ingrese un valor de cuota: "))
        print ("Vehiculos con un valor de cuota menor al ingresado")
        for i in range(len(self.__lista)):
            if  valor > self.__lista[i].getvalor():
                print ("Codigo {}, Modelo {}, Version {}".format(self.__lista[i].get_cod(),self.__lista[i].get_mod(),self.__lista[i].get_ver()))
    def opcion3(self):
        for i in range(len(self.__lista)):
            #print ("Cuota {}".format(self.__lista[i].getvalor()))
            print("El importe que se necesita para licitar el vehiculo de codigo {} es de {:.2f}".format(self.__lista[i].get_cod(),self.__lista[i].getMonto_a_lic()))
    def opcion4(self):
        c=int(input("Ingrese el codigo de un plan: "))
        for i in range(len(self.__lista)):
            if (c==self.__lista[i].get_cod()):
                print("Cuotas actuales: {}".format(self.__lista[i].get_cuot_lic()))
                self.__lista[i].modifica(input("Ingrese las cuotas a licitar nuevas: "))
                print("Cuota modificada a: {}".format(self.__lista[i].get_cuot_lic()))
    def Menu_1 (self):
        op=int(input("1- Actualizar el valor del vehículo de cada plan. Para esto se muestra el código del plan, el modelo y versión del vehículo, luego se ingresa el valor actual del vehículo y se modifica el atributo correspondiente\n2-Dado un valor, mostrar código del plan, modelo y versión del vehículo cuyo valor de la cuota sea inferior al valor dado\n3- Mostrar el monto que se debe haber pagado para licitar el vehículo (cantidad de cuotas para licitar * importe de la cuota)\n4- Dado el código de un plan, modificar la cantidad cuotas que debe tener pagas para licitar: 0 para terminar\n"))
        while op != 0:
            if op==1:
                self.actualizar()
            elif op==2:
                self.opcion2()
            elif op==3:
                self.opcion3()
            elif op==4:
                self.opcion4()
            op=int(input("1- Actualizar el valor del vehículo de cada plan. Para esto se muestra el código del plan, el modelo y versión del vehículo, luego se ingresa el valor actual del vehículo y se modifica el atributo correspondiente\n2-Dado un valor, mostrar código del plan, modelo y versión del vehículo cuyo valor de la cuota sea inferior al valor dado\n3- Mostrar el monto que se debe haber pagado para licitar el vehículo (cantidad de cuotas para licitar * importe de la cuota)\n4- Dado el código de un plan, modificar la cantidad cuotas que debe tener pagas para licitar: 0 para terminar\n"))
        print("--FIN--")