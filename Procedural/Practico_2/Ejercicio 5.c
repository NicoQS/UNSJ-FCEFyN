#include <stdio.h>
#include <string.h>
#define S 3
#define C 2


typedef struct{
char nom[30];
int cupo;
}salas;

void cerea (int arre[S][C]){
int i,j;
    for (i=0;i<S;i++){
        for (j=0;j<C;j++){
            arre[i][j]=0;
        }
    }
}

void inicia (salas sal[S]){
int i;
    for (i=0;i<S;i++){
        printf ("Ingrese el nombre de la sala %d\n",i+1);
        fflush(stdin);
        gets(sal[i].nom);
        printf ("Ingrese el cupo de la sala %d\n",i+1);
        scanf("%d",&sal[i].cupo);
    }
}
int busqueda (salas sal[S],char nom_area[30]){
int i=0;
    while ((i<S) && (strcmp(sal[i].nom,nom_area))!=0){
        i++;
    }
    if (i<S){
        return (i);
    }
}
void carga (int arre[S][C],salas sal[S]){
char nombre[30],nom_area[30];
int numc,b;
    printf ("Ingrese su nombre: FIN para terminar\n");
    fflush(stdin);
    gets(nombre);
    fflush(stdin);
    while (strcmp(nombre,"FIN")!=0){
        printf ("Ingrese el nombre del area tematica\n");
        fflush(stdin);
        gets(nom_area);
        b=busqueda(sal,nom_area);
        printf ("Ingrese el numero correspondiente del turno que desea asistir (1-4)\n");
        scanf("%d",&numc);
        arre[b][numc-1]++;
    printf ("Ingrese su nombre: FIN para terminar\n");
    fflush(stdin);
    gets(nombre);
    }
}
void item_b (int arre[S][C],salas sal[S]){
int i,j;
    for (i=0;i<S;i++){
        printf ("Sala: %s\n",sal[i].nom);
        for (j=0;j<C;j++){
            fflush(stdin);
            printf("\nLa cantidad de alumnos inscriptos en el turno %d es: %d \n",j+1,arre[i][j]);
        }
    }
}

int min_nom (int arre[S][C]){
int i,j,min,ar,acum;
min=arre[0][0];
    for (i=1;i<S;i++){
        acum=0
        for (j=1;j<C;j++){
            acum+=arre[i][j];
            }
        if (acum<min)
        }
    }
    return (ar);
}

int busca (salas sal[S],char nom_ar[30]){
int i=0;
    while ((i<S) && (strcmp(sal[i].nom,nom_ar))!=0){
        i++;
    }
    if (i<S){
        return (i);
    }
}
void item_d (int arre[S][C],salas sal[S]){
int j,acum=0,b;
char nom_ar[30];
    printf ("Ingrese el nombre de un area tematica para determinar el promedio de inscriptos\n");
    fflush(stdin);
    gets(nom_ar);
    b=busca(sal,nom_ar);
    for (j=0;j<C;j++){
        acum+=arre[b][j];
    }
    printf ("El promedio de inscriptos en el area tematica %s fue de: %d",nom_ar,(acum/C));
}
int main (){
int arre[S][C];
int mn;
cerea(arre);
salas sal[S];
inicia(sal);
carga(arre,sal);
item_b(arre,sal);
mn=min_nom(arre);
printf ("El area tematica con menos inscriptos es: %s\n",sal[mn].nom);
item_d(arre,sal);

}
