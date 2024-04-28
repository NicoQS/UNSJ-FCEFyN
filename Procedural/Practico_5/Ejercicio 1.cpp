#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>
#include <conio.h>


void carga (int *x,int i,int N){
    if (i<N){
        printf ("Ingrese un valor para la posicion %d\n",i+1);
        scanf("%d",&x[i]);
        carga(x,i+1,N);
    }
}
int prod_esc (int *arre1,int *arre2,int N){
int i,acum=0;
    for (i=0;i<N;i++){
        acum+=arre1[i]*arre2[i];
    }
return acum;
}
int item_b(int *arre1, int *&sub,int N){
int i,j=0;
int ct;
printf ("Porfavor ingrese la memoria necesaria para la nueva estructura\n");
scanf ("%d",&ct);
sub=(int*)malloc(sizeof(int)*ct);
    for (i=0;i<N;i++){
        if ((arre1[i]%2!=0)&&(j!=ct)){
            sub[j]=arre1[i];
            j++;
        }
    }
    return j;
}
void mostrar_b (int *sub,int sb){
int i;  
    printf ("--Nueva estructura que contiene valores impares de un vector--\n");
    for (i=0;i<sb;i++){
        printf ("%d ",sub[i]);
    }
printf ("\n");
}
/*
int cuenta(int *arre1,int N){
int i,j=0;
    for (i=0;i<N;i++){
        if (arre1[i]%2!=0){
            j++;
        }
    }
    return j;
}
*/
/*
int cuenta(int *arre1,int i,int N){
    if (i<N){
        if (arre1[i]%2!=0){
            return 1+cuenta(arre1,i+1,N);
        }
        else return cuenta(arre1,i+1,N);
    }
    else return 0;
}
*/
/*
int item_b(int *arre1, int *&st,int N,int ct){
int i,j=0;
sub=(int*)malloc(sizeof(int)*ct);
    for (i=0;i<N;i++){
        if ((arre1[i]%2!=0)&&(j!=ct)){
            sub[j]=arre1[i];
            j++;
        }
    }
}
*/
int main (){
int N,sb;
int *arre1,*arre2,*sub;
printf ("Ingrese la dimension de los arreglos \n");
scanf ("%d",&N);
arre1=(int*)malloc(sizeof(int)*N);
arre2=(int*)malloc(sizeof(int)*N);
printf("CARGA DEL ARREGLO 1\n");
carga(arre1,0,N);
printf("\nCARGA DEL ARREGLO 2\n");
carga(arre2,0,N);
printf("El producto escalar de los vectores es: %d\n",prod_esc(arre1,arre2,N));
/*ct=cuenta(arre1,N);*/
/*sub_vec(arre1,sub,N,ct);*/
sb=item_b(arre1,sub,N);
mostrar_b(sub,sb);
system("pause");
}