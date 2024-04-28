from PilaSecuencial import PilaSecuencial

if __name__ == "__main__":
    tamanio = int(input("Ingrese el tamaño de la pila doble: "))
    PilaDoble = PilaSecuencial(tamanio)
    PilaDoble.insertar(1)
    PilaDoble.insertar(2)
    PilaDoble.insertar(3)
    PilaDoble.insertar(4)
    PilaDoble.recorrer()