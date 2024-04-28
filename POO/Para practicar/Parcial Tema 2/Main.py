from ManejadorPersonas import ManejadorPersonas
from ManejadorOrganismos import ManejadorOrganismos
if __name__== "__main__":
    manejaPer=ManejadorPersonas()
    manejaOrg=ManejadorOrganismos()
    manejaOrg.cargarLista()
    nomOrganizaciones=manejaOrg.nombreOrgas()
    print("--APARTADO 3--")
    for i in nomOrganizaciones:
        print("Para el organismo --{}--, se registran los siguientes datos:".format(i))
        manejaPer.apartado3(i)
        print("\n")
    print("--APARTADO 4--")
    N=input("Ingrese el nombre de una organizacion: ")
    manejaPer.apartado4(N)