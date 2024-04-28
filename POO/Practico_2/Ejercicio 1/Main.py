'''''
Defina una clase “Email” con los siguientes atributos: idCuenta, dominio, tipo de dominio y contraseña (todos estos datos se ingresan por teclado). Y los siguientes métodos:

a- El constructor.

b- Método “retornaEmail()” que construye una dirección e-mail con los valores de los atributos de Email. Por ejemplo:

idCuenta.: alumnopoo

dominio: gmail

tipoDominio: com

Resultado devuelto por retornaEmail: alumnopoo@gmail.com

c- Método “getDominio()”, que retorna el dominio.

d- Método “crearCuenta(), crea una cuenta a partir de una dirección de correo que recibe como parámetro.

Implemente un programa que permita:

1- Ingresar el nombre de una persona y de su cuenta de correo, el identificador de cuenta, dominio y tipo de dominio (crear una instancia de la clase Email) y luego imprima el siguiente mensaje:

Estimado <nombre> te enviaremos tus mensajes a la dirección <dirección de correo>.

2- Para la instancia creada en el ítem anterior, modificar la contraseña, teniendo en cuenta que se debe ingresar la contraseña actual, y ésta debe ser igual a la registrada en la instancia. Luego se debe ingresar la nueva contraseña y realizar la modificación correspondiente.

3- Crear un objeto de clase Email, a partir de una dirección de correo, por ejemplo: informatica.fcefn@gmail.com, juanLiendro1957@yahoo.com, etc.

4- Leer de un archivo separado por comas 10 direcciones de e-mail, crear instancias de la clase Email; luego ingresar un identificador de cuenta e indicar si está repetido o no.
'''
from ClaseEmail import Email
from Funcion4 import funcion4

if __name__ == '__main__':
    nom = input("Ingrese su nombre:")
    p = Email(input ("Ingrese su ID:"),input ("Ingrese su dominio:"),input ("Ingrese su tipo de dominio:"),input ("Ingrese su contraseña:"))
    print("Estimado "+nom+" te enviaremos tus mensajes a la direccion "+p.retornarEmail())
    p.modifica_contra(input("Ingrese contraseña actual:"))
    corr = Email("","","","")
    corr.crearCuenta(input("Ingrese su correo:"))
    archivo = open ("Correos.csv")
    direcciones = archivo.read().split(",")
    funcion4(direcciones) 
    archivo.close()