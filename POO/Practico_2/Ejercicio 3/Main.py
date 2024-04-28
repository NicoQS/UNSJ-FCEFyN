"""""
Se necesita desarrollar una aplicación que procese la información de las variables meteorológicas temperatura, humedad y presión atmosférica. El registro de estas variables se hace cada una hora durante todos los días del mes. Esto se guarda en un archivo de texto separado con coma que contiene los siguientes datos: número de día, hora, valor de la variable temperatura, valor de la variable humedad y valor de la variable presión atmosférica. Se genera un archivo por cada mes.

Defina la clase “Registro” que posea como atributos los valores de las tres variables meteorológicas que se registran.

Implemente un programa que:

1.    Defina una lista bidimensional en la que se almacene el registro de las variables meteorológicas (instancia de la clase Registro) para cada día del mes, por cada hora.

2.    Almacene en la lista bidimensional los datos registrados en el archivo.

3.    Presente un menú de opciones permita realizar las siguientes tareas:

3.1.        Mostrar para cada variable el día y hora de menor y mayor valor.

3.2.        Indicar la temperatura promedio mensual por cada hora.

3.3.        Dado un número de día listar los valores de las tres variables para cada hora del día dado. El listado debe tener el siguiente formato.

"""""
import csv

from numpy import diag
from ClaseVariables import variables
from Menu import Menu_1
if __name__ == "__main__":
    lista =[]
    archivo = open("VariablesdelMes.csv")
    reader= csv.reader(archivo,delimiter=",")
    next(reader)
    
    for i in range(30):
        lista.append([variables(0,0,0)]*24)
    for fila in reader:
        dia=int(fila[0])
        hora=int(fila[1])
        p=variables(fila[2],fila[3],fila[4])
        lista[dia-1][hora-1]=p
Menu_1(lista)
