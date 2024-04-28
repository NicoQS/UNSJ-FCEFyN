from ManejaProductos import ManejaProductos
from ManejaStock import ManejaStock
if __name__ == "__main__":
    manejaProd=ManejaProductos()
    manejaStock=ManejaStock()
    manejaStock.cargarLista()
    print("--APARTADO 3--")
    manejaStock.apartado3()
    print("--APARTADO 4--")
    manejaStock.apartado4()
    print("--APARTADO 5--")
    print("Productos con stock < 10 y ordenados alfabeticamente por descripcion")
    Cantidad=manejaProd.getCt()
    manejaProd.ordenaporDescripcion()
    for i in range(Cantidad):
        ID=manejaProd.getID(i)
        ID2=manejaStock.getID(ID-1)
        if ID == ID2 and manejaStock.getStock(ID2-1) <= 10:
            print("Descripcion: {}, Stock: {}".format(manejaProd.getDesc(i),manejaStock.getStock(ID2-1)))
