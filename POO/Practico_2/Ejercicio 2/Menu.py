def busca (numero,lista):
    pos=-1
    i=0
    for i in range(len(lista)):
        if int(numero) == lista[i].getNumViajero():
            pos=i
    return pos
def Menu_1 (lista):
    b=busca(input("Ingrese numero de viajero: "),lista)
    if b !=-1:
        op=input("a- Consultar Cantidad de Millas.\nb- Acumular Millas.\nc- Canjear Millas.\nIngrese una opcion (z Para salir):")
        while op != "z":
            if op=="a":
                print("\nLa cantidad de millas del Numero de Viajero {} es: {} \n".format(lista[b].getNumViajero(),lista[b].cantidadTotaldeMillas()))
            elif op=="b":
                print ("\nLas millas que posee actualmente el viajero es: {}\n".format(+lista[b].acumularMillas(int(input("Ingrese la cantidad de millas para acumular:")))))
            elif op=="c":
                print ("\nLas millas que posee actualmente el viajero es: {}\n".format(+lista[b].canjearMillas(int(input("Ingrese la cantidad de millas a canjear:")))))
            op=input("a- Consultar Cantidad de Millas.\nb- Acumular Millas.\nc- Canjear Millas.\nIngrese una opcion (z Para salir):")
    else: 
        print ("No se encuentra el viajero ingresado")
    print("--FIN--")