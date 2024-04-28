""""
Sobrecarga por derecha (reverse operators)


Dada la clase ViajeroFrecuente definida en el ejercicio 2 con las sobrecargas de operadores solicitadas en el ejercicio 6, resolver lo siguiente:

1-    Comparar las cantidad de millas acumuladas de un viajero frecuente con un valor entero a través de la sobrecarga del operador igual (== o __eq__). Por ejemplo, sea v una instancia de la clase ViajeroFrecuente, debe ser posible realizar tanto v ==  100 como 100 == v.

2-    Acumular millas se pueda resolver de la siguiente forma: sea v una instancia de la clase ViajeroFrecuente, debe ser posible realizar v =  100 + v.

3-    Canjear millas se pueda resolver de la siguiente forma: sea v una instancia de la clase ViajeroFrecuente, debe ser posible realizar v =  100 - v.
"""
from Manejador import Manejador
if __name__ == "__main__":
    V=Manejador()
    V.cargarobjetos()
    V.funcion_1_2_3()