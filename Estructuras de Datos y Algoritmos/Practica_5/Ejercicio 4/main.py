from TablaHash import TablaHash
import random

if __name__=="__main__":

    n=1000
    long_bucket = 8
    cant_buckets = n // long_bucket
    Tabla1 = TablaHash(cant_buckets,long_bucket)
    Tabla2 = TablaHash(cant_buckets,long_bucket,True)
    
    for i in range(1000):
        Tabla1.insertar(random.randint(0,10000))
        Tabla2.insertar(random.randint(0,10000))
    
    print("Tabla 1 (sin usar numero primo)")
    Tabla1.Mostrar()
    
    print("\nTabla 2 (usando numero primo)")
    Tabla2.Mostrar()