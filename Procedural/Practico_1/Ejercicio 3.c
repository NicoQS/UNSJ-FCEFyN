#include <stdio.h>
#include <string.h>
#define N 3
/*Generar un arreglo de registros que posea la siguiente información de 10 alumnos de procedural: Nombre,
Apellido y DNI.
a) Cargar los datos de los alumnos.
b) Listar los alumnos cargados.
c) Indicar cuántos alumnos tiene DNI mayor a 40 millones.
*/
 
typedef struct{
char NyA[30];  //Si nos llegan a pedir una modificacion en especifico, pueden ser miembros separadps
int DNI;
}alumno;

void carga (alumno al[N]){
int i;
    for (i=0;i<N;i++){
        printf ("\nIngrese la informacion del alumno:Nombre-Apellido y DNI\n");
        fflush(stdin);
        gets(al[i].NyA);
        scanf("%d",&al[i].DNI);
    }
}
void itemb(alumno al[N]){
int i;
    printf("\n---Listado de Alumnos---\n");
    for (i=0;i<N;i++){
        printf("\n Nombre y Apellido: %s - DNI: %d\n",al[i].NyA,al[i].DNI);
    }
}

int may40 (alumno al[N]){
int i, ct;
ct=0;
    for (i=0;i<N;i++){
        if (al[i].DNI>40000000){
            ct++;
        }
    }
return (ct);
}
int main(){
alumno al[N];
carga(al);
itemb(al);
    if (may40(al)!=0){
        printf("\nLa cantidad de alumnos con un DNI mayor a 40 millones es de: %d\n",may40(al));
    }
}
