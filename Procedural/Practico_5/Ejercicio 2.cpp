#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct{
int DNI;
char categ;
int kg;
}boxeo;


/*
void carga (boxeo *box,int i, int N){
    if (i<N){
        printf ("Ingrese el DNI del boxeador %d\n",i+1);
        scanf("%d",&box[i].DNI);
        printf ("Ingrese el DNI del boxeador %d\n",i+1);
        fflush(stdin);
        getc(box[i].categ);
        printf ("Ingrese el DNI del boxeador %d\n",i+1);
        scanf("%f",&box[i].kg);
        carga(box,i+1,N);
    }
}
*/
int validar(){
int peso;
    printf ("Ingrese el peso del boxeador\n");
    scanf("%d",&peso);
    while ((peso<47) && (peso>90))
    {
        printf ("Peso ingresado incorrecto, ingrese nuevamente(47-90)");
    }
    return peso;
}
void carga (boxeo *box,int N){
int i;
int peso;
    for  (i=0;i<N;i++){
        printf ("Ingrese el DNI del boxeador %d\n",i+1);
        scanf("%d",&box[i].DNI);
        printf ("Ingrese la categoria del boxeador %d[A-H]\n",i+1);
        fflush(stdin);
        scanf(" %c",&box[i].categ);
        peso=validar();
        box[i].kg=peso;
    }
}

int item_b (boxeo *box,char cat,int N){
int i;
int max=box[0].kg;
    for (i=1;i<N;i++){
        if ((box[i].categ==cat)&&(box[i].kg>max)){
            max=box[i].kg;
        }
    }
    return max;
}
int ig_max (boxeo *box,char cat,int N,int max){
int i,ct=0;
    for (i=0;i<N;i++){
        if ((box[i].categ==cat)&&(box[i].kg==max)){
            ct+=1;
        }
    }
    return ct;
}
/*
int ig_max (boxeo *box,char cat,int N,float max,int i){
    if (i<N){
        if ((box[i].categ==cat)&&(box[i].kg==max)){
          return  1+ig_max(box,cat,N,max,i+1);
        }
       else ig_max(box,cat,N,max,i+1);
    }
    else return 0;
}
*/
void genera_dni(boxeo *box,int *dni,char cat,int max,int N){
int i,j=0;
    for (i=0;i<N;i++){
    if ((box[i].categ==cat)&&(box[i].kg==max)){
            dni[j]=box[i].DNI;
            j++;
        }
   }
}
void mostrar_b(int *dni,int i,int cont,char cat,int max){
    if (i<cont){
        printf ("\nEl boxeador con DNI: %d y de la categoria %c es uno de los que cuenta con mayor peso que es: %d\n",dni[i],cat,max);
        mostrar_b(dni,i+1,cont,cat,max);
    }

}
int maximo (boxeo *box,int N){
int i;
int max=box[0].kg;
    for (i=1;i<N;i++){
        if (box[i].kg>max){
            max=box[i].kg;
        }
    }
    return max;
}
int minimo (boxeo *box,int N){
int i;
int min=box[0].kg;
    for (i=1;i<N;i++){
        if (box[i].kg<min){
            min=box[i].kg;
        }
    }
    return min;
}
void cereo (int *aux,int tam){
int i;
    for (i=0;i<tam;i++){
        aux[i]=0;
    }
}
void calcula_c (boxeo *box,int *aux,int N,int min){
int i;  
    for (i=0;i<N;i++){
        aux[box[i].kg-min]+=1;
    }
}
void muestra_c (int *aux,int tam){
int i;
    for (i=0;i<tam;i++){
        printf ("");
    }
}
int main(){
boxeo *box;
int *dni,N,cont,tam,tmax,tmin,*aux;
char cat;
int max;
printf ("Ingrese la cantidad de participantes\n");
scanf("%d",&N);
box=(boxeo*)malloc(sizeof(boxeo)*N);
carga(box,N);
printf ("Ingrese una categoria (A-H) para mostrar los DNI de los boxeadores que tiene el peso maximo\n");
scanf(" %c",&cat);
max=item_b(box,cat,N);
cont=ig_max(box,cat,N,max);
dni=(int*)malloc(sizeof(int)*cont);
genera_dni(box,dni,cat,max,N);
mostrar_b(dni,0,cont,cat,max);
tmax=maximo(box,N);
tmin=minimo(box,N);
tam=(tmax-tmin)+1;
printf ("%d",tam);
aux=(int*)malloc(sizeof(int)*tam);
cereo(aux,tam);
calcula_c(box,aux,N,tmin);
muestra_c(aux,tam);
free(box);
free(dni);
system("pause");
}