#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#define N 50
/*A partir de un arreglo generado aleatoriamente con 50 números enteros, codificar un programa en C que permita:
a) Indicar si alguno de los números generados es un cero.
b) Escribir el contenido de las componentes que se encuentren en las posiciones pares.
c) Indicar cantidad de números pares que contiene.
d) Leer un número y si se encuentra en el arreglo indicar su posición (realizar búsqueda óptima).
*/


void carga (int arre[N]){
int i;
    srand(time(NULL));
    for (i=0;i<N;i++){
        arre[i]=rand()%5;
    }
}
/*
void mostrar (int arre[N]){
int i;
    for (i=0;i<N;i++){
    printf("[%d]  ",arre[i]);
    }
}
*/
int indicar_cero (int arre[N]){
int i=0,band=0;
    while ((i<N)&&(band!=0)){
        if (arre[i]==0){
            band=1;
        }
        i++;
    }
    return (band);
}
void mostrar_a (int arre[N]){
int b=indicar_cero(arre);
    if (b!=0){
    printf("\nDe los numeros generados, existe al menos uno que es cero\n");
    }
    else {printf("\nDe los numeros generados, no existe al menos un cero\n");}
}
void mostrar_b (int arre[N]){
int i;
    printf ("\n--Contenido de componentes en posiciones pares--\n");
    for (i=0;i<N ;i+=2){
        printf ("\nPosicion:[%d]- Numero: %d\n",i,arre[i]);
    }
}
void mostrar_c(int arre[N]){
int i,ct;
ct=0;
    for (i=0;i<N;i++){
        if ((arre[i]%2)==0){
            ct=ct+1;
        }
    }
    printf("\nLa cantidad de numeros pares que contiene el arreglo es de: %d\n",ct);
}

int busqueda (int arre[N],int num){
int i=0;
    while ((i<N)&&(arre[i]!=num)){
        i++;
    }
    if (i<N){
        return (i);
    }
    else {return(-1);}
}

void mostrar_d(int arre[N]){
int num,pos;
    printf("\nIngrese un numero para determinar si se encuentra en el arreglo\n");
    scanf("%d",&num);
    pos=busqueda(arre,num);
    if (pos!=-1){
        printf("\nEl numero ingresado se encuentra en el arreglo y en la posicion: %d\n",pos);
    }
    else {printf("\nEl numero ingresado no se encuentra en el arreglo\n");
    }
}
int main(){
int arre[N];
carga(arre);
//mostrar(arre);
mostrar_a(arre);
mostrar_b(arre);
mostrar_c(arre);
mostrar_d(arre);
getchar();

}
