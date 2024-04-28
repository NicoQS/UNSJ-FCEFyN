from TablaHash import TablaHash

import random

if __name__ == "__main__":
    Tabla1 = TablaHash(1000)
    Tabla2 = TablaHash(1000,True)
    
    for i in range(1000):
        Tabla1.insertar(random.randint(0,10000))
        Tabla2.insertar(random.randint(0,10000))
    
    print("Tabla 1 (sin usar numero primo)")
    dato = Tabla1.buscar(650)
    if dato != None:
        print("Dato encontrado: ",dato," Longitud de prueba: ",Tabla1.getLongPrueba())
    else:
        print("Dato no encontrado"," Longitud de prueba: ",Tabla1.getLongPrueba())
    print("Factor de carga: {:.2f} %".format(Tabla1.calcularFactorCarga()*100))
    
    print("Tabla 2 (Usando numero primo)")
    dato = Tabla2.buscar(650)
    if dato != None:
        print("Dato encontrado: ",dato," Longitud de prueba: ",Tabla2.getLongPrueba())
    else:
        print("Dato no encontrado"," Longitud de prueba: ",Tabla2.getLongPrueba())
    print("Factor de carga: {:.2f} %".format(Tabla2.calcularFactorCarga()*100))