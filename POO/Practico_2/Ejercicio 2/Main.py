"""""
En una aerolínea ofrece una promoción a sus viajeros frecuentes que consiste en acumular puntos por los viajes que realizan, pudiendo luego recibir beneficios a través del canje de puntos.

Usted trabaja en el área de sistemas de la aerolínea y le han solicitado la implementación de un sistema capaz de gestionar la promoción. Respetando el siguiente diseño de clase:
Atributos: número de viajero, DNI, nombre, apellido y millas acumuladas
Métodos:
a- El constructor.
b- “cantidadTotaldeMillas”, retorna la cantidad de millas acumuladas.
c- “acumularMillas”, recibe como parámetro la cantidad de millas recorridas, las suma en el atributo correspondiente y retorna el valor del atributo actualizado.
d- “canjearMillas”, recibe como parámetro la cantidad de millas a canjear. Para utilizar las millas debe verificarse que la cantidad a canjear sea menor o igual a la cantidad de millas acumuladas, caso contrario mostrar un mensaje de error en la operación. Retorna el valor de la cantidad de millas acumuladas.
Implemente un programa que:

1- Leer de un archivo separado por comas los datos para crear instancias de la clase ViajeroFrecuente, y almacenarlas en una lista.

2- Lea por teclado un número de viajero frecuente y presente un menú con las siguientes opciones:

a- Consultar Cantidad de Millas.

b- Acumular Millas.

c- Canjear Millas.

3- Represente el almacenamiento en memoria para la lista cargada con 4 viajeros.
"""""
import csv
from ClaseViajeroFrecuente import ViajeroFrecuente
from Menu import Menu_1
if __name__ == "__main__":
    archivo = open("Viajeros.csv")
    reader= csv.reader(archivo,delimiter=",")
    lista=[]
    next(reader)
    for fila in reader:
        p=ViajeroFrecuente(fila[0],fila[1],fila[2],fila[3],fila[4])
        lista.append(p)
Menu_1(lista)