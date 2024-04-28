#include <stdio.h>
#define N 4

/*Generar un arreglo con 20 números enteros y codificar un programa en C que permita:
a) Indicar si alguno de los números generados es un cero.
b) Escribir el contenido de las componentes que se encuentren en las posiciones pares.
c) Indicar cantidad de números pares que contiene.*/

void carga (int num[N]){
int i;
    for (i=0;i<N;i++){
        printf ("Ingrese un numero entero\n");
        scanf ("%d",&num[i]);
    }
}

void mostrar (int num[N]){
int i;
    for (i=0;i<N;i++){
        printf ("\nNumero:%d\n",num[i]);
    }
}
int numcero (int num[N]){
int i,c;
i=0;
c=0;
    while (i<N && c==0 ){
        if (num[i]==0){
            c=1;
        }
        else {
        	i++;
		}
    }

return (c);
}
void mostrarb (int num[N]){
int i;
    printf ("\nContenido de componentes en posiciones pares\n");
    for (i=0;i<N ;i+=2){
        printf ("\nPosicion:[%d]- Numero: %d\n",i,num[i]);
    }
}
void itemc (int num[N]){
int i,ct;
ct=0;
    for (i=0;i<N;i++){
        if ((num[i]%2)==0){
            ct=ct+1;
        }
    }
    printf("\nLa cantidad de numeros pares que contiene el arreglo es de: %d\n",ct);
}
int main (){
int num[N];
carga(num);
//mostrar(num);
    if (numcero(num)==0){
        printf ("\nDe los numeros generados no hay un cero\n");
        }
    else {printf("\nDe los numeros generados existe un cero\n");}
mostrarb(num);
itemc(num);
return (0);
}
