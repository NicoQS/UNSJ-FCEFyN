#include <stdio.h>
#include <malloc.h>
#include <stdlib.h>
#include <string.h>

typedef char cadena[30];

struct alumno{
    cadena nom;
    cadena carr;
    struct alumno *sig;
};

struct libro{
    int cod;
    struct alumno *cola;
    struct libro *sig;
};

typedef struct alumno *al;
typedef struct libro *lib;


void cargar (lib &libros){
lib nuevo;
int code;
    printf ("Ingrese un codigo de libro: 0 para terminar\n");
    scanf("%d",&code);
    while (code!=0)
    {
        nuevo=(lib)malloc(sizeof(struct libro));
        nuevo->sig=libros->sig;
      //  nuevo->sig=libros;
        nuevo->cod=code;
        nuevo->cola=NULL;
        libros->sig=nuevo;
      //  libros=nuevo;
    printf ("Ingrese un codigo de libro: 0 para terminar\n");
    scanf("%d",&code);
    }
}
int menu(){
    int d;
    printf ("--Introduzca una opcion--\n");
    printf ("1: Inicializar en NULL la lista\n");
    printf("2: Carga de libros\n");
    printf("3: Registrar alumno para cola\n");
    printf("4: Ingresar un nuevo libro\n");
    printf("5: Ingresar un codigo de libro y una carrera: Muestra los alumnos\n");
    printf ("6: Muestra nombres de alumnos para cierta carrera y codigo de libro\n");
    printf("7: Salir\n");
    scanf("%d",&d);
    return d;
}

void inserta_2(lib &libros){
    al p, nuevo, anterior;
    nuevo =(al) malloc(sizeof(struct alumno));
    printf ("Ingrese el nombre del alumno\n");
    fflush(stdin);
    gets(nuevo->nom);
    printf ("Ingrese la carrera del alumno\n");
    fflush(stdin);
    gets(nuevo->carr);
    nuevo->sig = NULL;
    if (libros->cola == NULL) /* controla si la lista está vacía */
    libros->cola = nuevo;
    else
    { p = libros->cola; /* resguarda a xp de las siguientes modificaciones */
    while (p != NULL)
    { anterior = p;
    p = p->sig;
    }
    anterior->sig = nuevo;
    printf("El nuevo elemento ha sido insertado al final de la lista.");
    }
    return;
}

void inserta (lib libros,int cod){
    if (libros==NULL){
        printf ("El codigo es incorrecto o no se encuentra en la lista\n");
        return;
    }
    libros=libros->sig;
    if (libros->cod==cod){
       inserta_2(libros);
    }
    else inserta(libros,cod);
}

void mostrar (lib libros){
al alum;
    while (libros->sig!=NULL){
        printf ("\nAlumnos en espera del libro %d\n",libros->sig->cod);
            alum=libros->sig->cola;
            while(alum!=NULL){
                printf ("Alumno: %s\n",alum->nom);
                printf("Carrera: %s\n",alum->carr);
                printf("\n");
                alum=alum->sig;
            }
            libros=libros->sig;
    }
}

void inserta_nuevo(lib &libros){
lib nuevo;
nuevo=(lib)malloc(sizeof(struct libro));
printf ("Ingrese el codigo para el nuevo libro\n");
scanf("%d",&nuevo->cod);
nuevo->sig=libros->sig;
nuevo->cola=NULL;
libros->sig=nuevo;
}

void suprimir (lib &libros,int cod){

}

int main(){
lib libros;
int op;
int cod;
cadena nm;
    do{
        system("cls");
        op=menu();
        switch(op){
            case 1: {
                
                libros->sig=NULL;
                libros->cod=-1;
                libros->cola=NULL;
                break;
            }
            break;
            case 2: {
                cargar(libros);break;
            }
            break;
            case 3:{
               printf ("Ingrese el codigo del libro\n");
               scanf("%d",&cod);
               inserta(libros,cod);
               break;
            }
            break;
            case 4:{
                inserta_nuevo(libros);
            }
            case 5:{
                printf ("Ingrese un codigo de libro para realizar un prestamo\n");
                scanf("%d",&cod);
                suprimir(libros,cod);
            }
            break;
            case 6:{

            } 
            break;
            case 8: {
                mostrar(libros);
                system("pause");
                break;
            }

        }
    }
    while(op!=7);
}