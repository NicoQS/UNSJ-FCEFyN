from ManejaEntrega import ManejaEntrega
from ManejaRecepcion import ManejaRecepcion
if __name__ == "__main__":
    manejaEntr=ManejaEntrega()
    manejaRecep=ManejaRecepcion()
    manejaEntr.cargarLista()
    listaID=manejaRecep.getIDs()
    lista=[]
    for i in range (len(listaID)):
        b=manejaEntr.buscaEntrega(listaID[i])
        if b==-1:
            lista.append(manejaRecep.getProd(i))
    manejaRecep.apartado3(lista)
    marca=input("Ingrese el nombre de una marca ver su monto en concepto de reparaciones: ")
    ListIdmarca=manejaRecep.buscaMarca(marca)
    if ListIdmarca != -1:
        print("Para la marca {} se registro el siguiente monto: {}$".format(marca,manejaEntr.apartado4(ListIdmarca)))
    else:
        print("Para la marca seleccionada no se registro el monto final ya que no fue entregada")