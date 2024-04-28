"""
Sobrecarga de operadores

Dada la clase ViajeroFrecuente definida en el ejercicio 2, resolver lo siguiente:

1-    Determinar el/los viajero/s con mayor cantidad de millas acumuladas. Para distinguir entre dos objetos ViajeroFrecuente cuál posee mayor cantidad de millas acumuladas, sobrecargue el operador relacional mayor (> o  __gt__ en python).

2-    Acumular millas usando la sobrecarga del operador binario suma(+), obteniendo como resultado de la suma una instancia de la clase ViajeroFrecuente. Por ejemplo, sea v una instancia de la clase ViajeroFrecuente, la función de acumular millas se resuelve de la siguiente forma v = v + 100.

3-    Canjear millas usando la sobrecarga del operador binario resta(-),obteniendo como resultado de la resta una instancia de la clase ViajeroFrecuente. Por ejemplo, sea v una instancia de la clase ViajeroFrecuente, la función de canjear millas se resuelve de la siguiente forma v = v - 100.
"""

from Manejador import Manejador

if __name__ == "__main__":
    V=Manejador()
    V.cargarobjetos()
    V.funcion1()
    V.funcion2_3()