#include <stdio.h>

/*En la Facultad se realiza un congreso para el cual se destinan 6 salas de conferencias y cada una representa un
área temática. En cada sala se dictan 4 conferencias en distintos turnos. Por cada interesado se ingresa número
del área temática (1-6), y turno al que quiere asistir (1-4). La Facultad desea llevar un registro de la cantidad
de alumnos inscriptos en cada área y en cada turno, para ello realizar los siguientes items:
a) Carga de los datos. La carga es desordenada, cada alumno indica área y turno. No se sabe la cantidad de
alumnos.
b) Indicar la cantidad de inscriptos en cada turno de cada área.
c) Dada un área temática, indicar el promedio de inscriptos.
*/

void cerea (int arre[6][4]){
int i,j;
    for (i=0;i<6;i++){
        for (j=0;j<4;j++){
            arre[i][j]=0;
        }
    }
}

void carga (int arre[6][4]){
int sala,turno;
    printf("Ingrese la sala que desea asistir(1-6): 0 para finalizar\n");
    scanf("%d",&sala);
    while (sala!=0){
     printf("Ingrese el turno que desea asistir-(1-4)\n");
     scanf("%d",&turno);
     arre[sala-1][turno-1]++;
    printf("Ingrese la sala que desea asistir(1-6): 0 para finalizar\n");
    scanf("%d",&sala);
    }
}

void item_b (int arre[6][4]){
int i,j;
    printf("            Turnos\n          [1  2  3  4]\n\n");
    for (i=0;i<6;i++){
        printf("{Area %d}  ",i+1);
        for (j=0;j<4;j++){
            printf(" %d ",arre[i][j]);
        }
        printf("\n");
    }
    printf("   [Cantidad de inscriptos]\n");
}
/*
void item_b (int arre[6][4]){
int i,j;
    for (i=0;i<6;i++){
        printf ("AREA: 1\n")
        for (j=0;j<4;j++){
            printf("\nLa cantidad de alumnos inscriptos en el turno %d es: %d \n",j+1,arre[i][j]);
        }
    }
}
*/

int calculo (int arre[6][4],int area){
int j, suma=0;
    for (j=0;j<4;j++){
        suma+=arre[area-1][j];
    }
    return (suma/4);
}

void item_c (int arre[6][4]){
int area;
    printf("\nIngrese un area tematica para verificar el promedio de inscriptos: 0 para terminar\n");
    scanf("%d",&area);
        while (area!=0){
            if ((area>=1) && (area<=6)){
            printf("El promedio de inscriptos del area tematica %d es de: %d\n",area,calculo(arre,area));}

            else { printf ("\nNumero de area incorrecto\n");
            }
            printf("\nIngrese un area tematica para verificar el promedio de inscriptos: 0 para terminar\n");
            scanf("%d",&area);
        }
    }


int main(){
int arre[6][4];
cerea(arre);
carga(arre);
item_b(arre);
item_c(arre);
getchar();

}
