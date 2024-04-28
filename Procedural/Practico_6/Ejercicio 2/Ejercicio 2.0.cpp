#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef char cadena[30];
typedef struct{
cadena nom;
char nota;
int reg;
}alumno;


void carga (FILE *f){
alumno al;
int num;
    printf ("Ingrese en forma ordenada un numero de registro: 0 para terminar\n");
    scanf("%d",&num);
    while(num!=0){
        al.reg=num;
        printf ("Ingrese el nombre del alumno\n");
        fflush(stdin);
        gets(al.nom);
        printf ("Ingrese la nota de un parcial: A aprobado o R reprobado\n");
        scanf (" %c",&al.nota);
        fwrite(&al,sizeof(alumno),1,f);
        printf ("Ingrese en forma ordenada un numero de registro: 0 para terminar\n");
        scanf("%d",&num);
    }
    fclose(f);
}
void muestra (FILE *f){
alumno al;
f=fopen("alumnosPP.dat","rb");
rewind(f);
fread(&al,sizeof(alumno),1,f);
    while (feof(f)==0){
        printf ("Numero de registro: %d\n",al.reg);
        printf ("Nombre: %s\n",al.nom);
        printf ("Nota de un parcial: %c\n",al.nota);
        fread(&al,sizeof(alumno),1,f);
        printf ("\n");
    }
    fclose(f);
}

int main(){
FILE *f;
int op;
    do{
        system("cls");
        printf ("Ingrese una opcion:\n");
        printf ("1: Para crear un nuevo archivo o sobreescribir uno creado(Programacion procedural)\n");
        printf ("2: Para observar el contido del archivo(Programacion procedural)\n");
        printf ("3: Para terminar\n");
        scanf("%d",&op);
        switch (op){
            case 1:{
            f=fopen("alumnosPP.dat","wb");
            if (f==NULL){
             printf ("Ocurrio un error\n");
            }
            carga(f);
            }
            break;
            case 2:{
             muestra(f);
            system("pause");
            }
            break;
        }
    }
    while (op!=3);
}

/*
Lote de prueba 
100
Juan
A
200
Pia
R 
300
Lucia
A
400
Pedro
R
500
Luan
A
*/