from tkinter import * 
from tkinter import ttk
from unittest import result
from functools import partial
import re
from ClaseFraccion import Fraccion

class Calculadora:
    __ventana : Tk
    __operando1 = None
    __operando2 = None
    __pos : int


    def __init__(self):
        self.__pos = 0

        #ENTRADA
        self.__ventana = Tk()
        self.__ventana.title('Tk-Calculadora')
        self.__ventana.resizable(False, False)
        mainframe = ttk.Frame(self.__ventana, padding="3 10 3 10")
        mainframe.grid(column=0, row=0, stick=N + W + E + S)
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        self.e_texto = Entry(mainframe, font= ("Calibri 20"), width=15)
        self.e_texto.grid(row = 0, column = 0, columnspan = 4)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'

        #VARIABLES
        self.__operando1 = StringVar()
        self.__operando2 = StringVar()


        #BOTONES 
        self.boton1 = Button(mainframe, text = "1", width = 5, height = 2, command = partial(self.ponerEnPANTALLA,1))
        self.boton2 = Button(mainframe, text = "2", width = 5, height = 2, command =  partial(self.ponerEnPANTALLA,2))
        self.boton3 = Button(mainframe, text = "3", width = 5, height = 2, command =  partial(self.ponerEnPANTALLA,3))
        self.boton4 = Button(mainframe, text = "4", width = 5, height = 2, command =  partial(self.ponerEnPANTALLA,4))
        self.boton5 = Button(mainframe, text = "5", width = 5, height = 2, command =  partial(self.ponerEnPANTALLA,5))
        self.boton6 = Button(mainframe, text = "6", width = 5, height = 2, command =  partial(self.ponerEnPANTALLA,6))
        self.boton7 = Button(mainframe, text = "7", width = 5, height = 2, command =  partial(self.ponerEnPANTALLA,7))
        self.boton8 = Button(mainframe, text = "8", width = 5, height = 2, command =  partial(self.ponerEnPANTALLA,8))
        self.boton9 = Button(mainframe, text = "9", width = 5, height = 2, command =  partial(self.ponerEnPANTALLA,9))
        self.boton0 = Button(mainframe, text = "0", width = 5, height = 2, command =  partial(self.ponerEnPANTALLA,0))

        self.boton_borrar = Button(mainframe, text = "CE", width = 5, height = 2, command =  partial(self.borrarPANEL))

        self.boton_div = Button(mainframe, text = "%", width = 5, height = 2, command =   partial(self.ponerEnPANTALLA,"%"))
        self.boton_mult = Button(mainframe, text = "X", width = 5, height = 2, command =   partial(self.ponerEnPANTALLA,"*"))
        self.boton_sum = Button(mainframe, text = "+", width = 5, height = 2, command =   partial(self.ponerEnPANTALLA,"+"))
        self.boton_rets = Button(mainframe, text = "-", width = 5, height = 2, command =   partial(self.ponerEnPANTALLA,"-"))
        self.boton_fraccion = Button(mainframe, text = "/", width = 5, height = 2, command =  partial(self.ponerEnPANTALLA,"/"))
        self.boton_igual = Button(mainframe, text = "=", width = 5, height = 2, command =  partial(self.resolverOperacion))
        #---------------------------------------------------------------------------------------------------------------------
        
        #GRID
        self.boton_borrar.grid(row = 1, column = 0, padx = 5, pady = 5)
        self.boton_div.grid(row = 1, column = 3, padx = 5, pady = 5)

        self.boton7.grid(row = 2, column = 0, padx = 5, pady = 5)
        self.boton8.grid(row = 2, column = 1, padx = 5, pady = 5)
        self.boton9.grid(row = 2, column = 2, padx = 5, pady = 5)
        self.boton_mult.grid(row = 2, column = 3, padx = 5, pady = 5)

        self.boton4.grid(row = 3, column = 0, padx = 5, pady = 5)
        self.boton5.grid(row = 3, column = 1, padx = 5, pady = 5)
        self.boton6.grid(row = 3, column = 2, padx = 5, pady = 5)
        self.boton_sum.grid(row = 3, column = 3, padx = 5, pady = 5)

        self.boton1.grid(row = 4, column = 0, padx = 5, pady = 5)
        self.boton2.grid(row = 4, column = 1, padx = 5, pady = 5)
        self.boton3.grid(row = 4, column = 2, padx = 5, pady = 5)
        self.boton_rets.grid(row = 4, column = 3, padx = 5, pady = 5)
        self.boton_fraccion.grid(row = 1, column = 2, padx = 5, pady = 5)
        self.boton0.grid(row = 5, column = 0, padx = 5, pady = 5)
        self.boton_igual.grid(row = 5, column = 3, padx = 5, pady = 5)
        #----------------------------------------------------------------------------------------------------------------------
        self.__ventana.mainloop()

    #CALCULA FRACCIONES
    def resolverFracciones(self, ecuacion):
        try:
            fraccion = ""
            Fracciones = re.split("[+ - % *]", ecuacion)
            self.__operando1 = Fraccion(Fracciones[0].split("/")) #Crea una fraccion a partir de la clase Fraccion
            self.__operando2 = Fraccion(Fracciones[1].split("/"))
            if "+" in ecuacion:
                fraccion = self.__operando1 + self.__operando2
            elif "-" in ecuacion:
                fraccion = self.__operando1 - self.__operando2
            elif "%" in ecuacion:
                fraccion = self.__operando1 / self.__operando2
            elif "*" in ecuacion:
                fraccion = self.__operando1 * self.__operando2
        except:
            fraccion = "SyntaxError"
        return fraccion
    
    #----------------------------------------------------------------------------------------------------------------------
    
    #FUNCIONES PARA CALCULAR OPERACIONES
    def ponerEnPANTALLA(self, valor):
        self.e_texto.insert(self.__pos, valor)
        self.__pos += 1

    def borrarPANEL(self):
        self.e_texto.delete(0, END)
        self.__pos = 0

    def resolverOperacion(self):
        ecuacion = self.e_texto.get()
        try:
            if "/" not in ecuacion:
                #re(expresion regular) especifica un conjunto de cadenas que coinciden con ella
                #re. split devuelve una lista formada por cadenas de texto
                Operandos = re.split("[+ - % *]", ecuacion) 
                self.__operando1 = int(Operandos[0])
                self.__operando2 = int(Operandos[1])
                if '+' in ecuacion:
                    resultado = self.__operando1 + self.__operando2
                elif '-' in ecuacion:
                    resultado = self.__operando1 - self.__operando2
                elif '*' in ecuacion:
                    resultado = self.__operando1 * self.__operando2
                elif '%' in ecuacion:
                    resultado = self.__operando1 / self.__operando2
            else:
                resultado = self.resolverFracciones(ecuacion)
        except:
            resultado = "MathError"
        self.e_texto.delete(0, END)
        self.e_texto.insert(0, str(resultado)) #type: ignore
        self.__pos+= len(str(resultado))    #type: ignore
    #----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    calc = Calculadora()