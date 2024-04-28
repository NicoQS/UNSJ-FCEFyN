from PilaSecuencial import PilaSecuencial

if __name__ == "__main__":
    tamanio = int(input("Ingrese el tamaño de la pila: "))
    Binario=PilaSecuencial(tamanio)
    num = int(input("Ingrese un numero entero: "))
    Binario.conversionBinario(num) 