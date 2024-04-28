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
f=fopen("alumnosAL.dat","rb");
if (f==NULL) printf ("Ocurrio un error");
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
void muestra_3(FILE *f){
alumno al,pp;
FILE *fpp;
f=fopen("alumnosAL.dat","rb");
fpp=fopen("alumnosPP.dat","rb");
if (f==NULL) printf ("Ocurrio un error");
rewind(f);
rewind(fpp);
fread(&al,sizeof(alumno),1,f);
fread(&pp,sizeof(alumno),1,fpp);
printf ("ALUMNOS QUE APROBARON AMBAS MATERIAS\n");
    while ((feof(f)==0)&&(feof(fpp)==0)){
        if ((al.nota=='A')&&(pp.nota=='A')){
        printf ("Numero de registro: %d\n",al.reg);
        printf ("Nombre: %s\n",al.nom);
         printf ("\n");
        }
        fread(&al,sizeof(alumno),1,f);
        fread(&pp,sizeof(alumno),1,fpp);
    }
    fclose(f);
    fclose(fpp);
}

int main(){
FILE *f;
int op;
    do{
        system("cls");
        printf ("Ingrese una opcion:\n");
        printf ("1: Para crear un nuevo archivo o sobreescribir uno creado(Algebra Lineal)\n");
        printf ("2: Para observar el contido del archivo(Algebra)\n");
        printf ("3: Para observar alumnos que aprobaron ambas materias\n");
        printf ("4: Para terminar\n");
        scanf("%d",&op);
        switch (op){
            case 1:{
            f=fopen("alumnosAL.dat","wb");
            if (f==NULL){
             printf ("Ocurrio un error\n");
            }
            carga(f);
            break;
            }
            break;
            case 2:{
             muestra(f);
            // muestra_pp(F);;    
            system("pause");
            break;
            }
            break;
            case 3:{

                muestra_3(f);
                
                system("pause");
                break;
            }
            break;
        }
    }
    while (op!=4);
}
/*
Lote de prueba 
500
Luan
A
400
Pedro
R 
300
Lucia
A
200
Pia
R
100
Juan
A
*/