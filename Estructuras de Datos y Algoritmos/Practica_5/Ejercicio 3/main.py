from TablaHash import TablaHash

import random

if __name__ == "__main__":
    Tabla1 = TablaHash(1000)
    Tabla2 = TablaHash(1000,True)
    
    for i in range(1000):
        Tabla1.insertar(random.randint(0,10000))
        Tabla2.insertar(random.randint(0,10000))
    
    print("----------Tabla 1 (sin usar numero primo)----------------")
    Tabla1.item1()
    print("Cantidad de listas que registran una cantidad >= 3 al promedio registrado ",Tabla1.item2())
    print("-----------Tabla 2 (Usando numero primo)-----------")
    Tabla2.item1()
    print("Cantidad de listas que registran una cantidad >= 3 al promedio registrado ",Tabla2.item2())