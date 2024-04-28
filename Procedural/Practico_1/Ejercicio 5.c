#include <stdio.h>
#include <time.h>
#include <stdlib.h>

/*Cargar aleatoriamente una tabla de 5x4 con números enteros y:
a) Mostrar la suma de cada una de las filas.
b) Calcular el promedio de la tercera columna.
c) Decir cuántos números mayores a 100 se ingresaron.*/


void carga (int arre[5][4]){
int i,j;
    srand(time(NULL));
    for (i=0;i<5;i++){
        for (j=0;j<4;j++){
            arre[i][j]=rand()%120;
        }
    }
}
void mostrar (int arre[5][4]){
int i,j;
    for (i=0;i<5;i++){
        for (j=0;j<4;j++){
            printf(" %d  ",arre[i][j]);
        }
        printf("\n");
    }
}

void suma(int a[5][4]){
    int i=0,acum,c;
    printf("\n ||SUBPROGRAMA SUMA|| \n");
    while (i<5)
    {
        acum=0;
        for (c = 0; c < 4; c++)
        {
            acum=acum+a[i][c];
        }
        printf("Fila %d Sumatoria igual a %d \n",i+1, acum);
        i++;
    }
    return;
}

/*
void item_a (int arre[5][4],int vertical[5]){
int suma,i,j;
    for (i=0;i<5;i++){
        suma=0;
        for (j=0;j<4;j++){
            suma+=arre[i][j];
        }
        vertical[i]=suma;
    }
}
void mostrar_a (int vertical[5]){
int i;
    printf("\n---Resultado de cada una de las sumas de las filas de la matriz---\n");
    for (i=0;i<5;i++){
        printf("%d\n",vertical[i]);
    }
}
*/
float item_b (int arre[5][4]){
int i, suma=0;
    for (i=0;i<5;i++){
        suma+=arre[i][2];
    }
    return (suma/5);
}
void item_c (int arre[5][4]){
int i, j, cont=0;
    for (i=0;i<5;i++){
        for (j=0;j<4;j++){
            if (arre[i][j]>100){
                cont++;
            }
        }
    }
    printf("\nLa cantidad de numeros ingresados que son mayores a 100 es de: %d\n",cont);
}
int main (){
int arre[5][4],vertical[5];
carga(arre);
mostrar (arre);
suma(arre);
//item_a(arre,vertical);
//mostrar_a(vertical);
printf("\nEl promedio de la tercera columna es de %.2f\n",item_b(arre));
item_c(arre);
getchar();
}
