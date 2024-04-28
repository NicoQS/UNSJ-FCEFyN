#include <stdio.h>
#include <string.h>

/*Dada la frase “Programación Procedural 2021”, leerla desde teclado en una cadena de caracteres y:
a) Reemplazar el 1 por un 0 (Solo cambiar ese carácter)
b) Copiar la palabra “Programación” a una nueva cadena de caracteres.
c) Contar la cantidad de vocales de la frase.*/


int vocales (char cad2[100]){
int i,cont,limite=strlen(cad2);
cont=0;
    for (i=0;i<limite;i++){
        switch(cad2[i]){
            case 'a': cont++;break;
            case 'e': cont++;break;
            case 'i': cont++;break;
            case 'o': cont++;break;	
            case 'u': cont++;break;
        }
    }
    return (cont);
}
int main (){
char cad[100],cad2[100],*p=cad;
printf ("Ingrese el texto solicitado\n");
fflush(stdin);
gets(cad);
cad[strlen(cad)-1]='0';
printf("\nEl texto nuevo generado es: %s\n",cad);
strncpy(cad2,cad,12);
cad2[12]='\0';
printf("\nCadena 2: %s\n",cad2);
printf("\nLa cantidad de vocales que tiene la cadena 2 es: %d",vocales(cad2));
getchar();
}
