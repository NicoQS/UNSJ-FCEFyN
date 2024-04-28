#include <stdio.h>
#include <string.h>
#define N 3
typedef struct{
int cant;
char nom[30];
}lenguajes;
void inicia (lenguajes len[N],int i){
    if (i!=N){
        printf ("Ingrese el nombre del lenguaje %d\n",i+1);
        fflush(stdin);
        gets(len[i].nom);
        len[i].cant=0;
        inicia(len,i+1);
    }
}

int busca (lenguajes len[N],int i,char nombre[30]){

    if (i==N){
        return (-1);
    }
    else if (strcmp(len[i].nom,nombre)==0){
        return i;
    }
    else {
        return busca(len,i+1,nombre);
    }
}


void carga (lenguajes len[N]){
int b;
char nombre[30];
    printf ("\n---Carga de los datos---\n");
    printf ("Ingrese el nombre del lenguaje que utiliza: FIN para terminar\n");
    fflush(stdin);
    gets(nombre);
    while (strcmp(nombre,"FIN")!=0){
        b=busca(len,0,nombre);
        if (b!=-1){
           len[b].cant++;
        }
        else {printf ("Nombre ingresado incorrecto\n");
        }
    printf ("Ingrese el nombre del lenguaje que utiliza: FIN para terminar\n");
    fflush(stdin);
    gets(nombre);
    }
}

void item_b (lenguajes len[N],int i){

    if (i<N){
        if (len[i].cant<4000){
            printf ("El lenguaje denominado %s es uno de los cuales no tiene mas de 4000 programadores\n",len[i].nom);
            item_b(len,i+1);
        }
    }
}
/*
int mas_pop (lenguajes len[N]){
int i,posi=0;
int max=len[0].cant;
    for (i=1;i<N;i++){
        if (len[i].cant>max){
            max=len[i].cant;
            posi=i;
        }
    }
    return (posi);
}
*/
int mas_pop (lenguajes len[N],int i, int max,int pos){
    if (i==N){
        return pos;
    }
    else {
            if (len[i].cant>max){
            max=len[i].cant;
            pos=i;
            }
    return mas_pop(len,i+1,max,pos);}
}
int item_d (lenguajes len[N],int i,int *con_9k){

        if (i<N){
            if ((len[i].cant>5000) && (len[i].cant<9000)){
            return 1+item_d(len,i+1,con_9k);
        }
        else if (len[i].cant>9000){
            *con_9k+=1;
        }
        return item_d(len,i+1,con_9k);
    }
    else return 0;
}

int total (lenguajes len[N],int i){
    if (i<N){
        return len[i].cant+total(len,i+1);
    }
    else return 0;
}
int main (){
lenguajes len[N];
int max, ct,pos;
int con_9k=0;
inicia(len,0);
carga(len);
item_b (len,0);
max=mas_pop(len,1,len[0].cant,pos);
ct=item_d(len,0,&con_9k);
printf ("\nEl lenguaje mas popular es el %d llamado %s\n",max+1,len[max].nom);
printf ("\nLa cantidad de lenguajes que eligieron entre 5000 y 9000 programadores fue de %d\n",ct);
printf ("\nLa cantidad de lenguajes que eligieron mas de 9000 programadores fue de %d\n",con_9k);
printf ("\nEl total de programadores registrados es de %d\n",total(len,0));
}
