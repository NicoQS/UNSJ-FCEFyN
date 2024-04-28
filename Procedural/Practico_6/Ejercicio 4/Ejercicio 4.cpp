#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <malloc.h>
#define N 4
typedef char cadena[30];
typedef struct{
int cod;
cadena titulo;
cadena direc;
int ct;
}titu;

int menu(){
int d;
    printf ("Ingrese una opcion\n");
    printf ("1: Crear archivo TITULOS.dat\n");
    printf ("2: Para cada pelicula se indica titulo y cantidad\n");
    printf ("3: Dado un codigo se muestra titulo y cantidad de ejemplares\n");
    printf("4: En base al nombre de un director se muestra toda su informacion sobre las peliculas\n");
    printf ("5: Se genera una estructura que almacena la informacion de peliculas en base al nombre del director ingresado anteriormente\n");
    printf("6: Total de peliculas realizadas por el director y cantidad de peliculas con menos de 2 ejemplares\n");
    printf("7: Salir\n");
    scanf("%d",&d);
    return d;
}
void carga (FILE *f){
int i;
titu t;
if ((f=fopen("TITULOS.dat","wb"))==NULL)
    printf ("Ocurrio un error\n");

    for (i=0;i<N;i++){
        fseek(f,0,SEEK_END);
        printf ("Ingrese el codigo de la pelicula (1-1500[Sin repetir codigo])\n");
        scanf("%d",&t.cod);
        printf ("Ingrese el titulo de la pelicula\n");
        fflush(stdin);
        gets(t.titulo);
        printf ("Ingrese el directos de la pelicula\n");
        fflush(stdin);
        gets(t.direc);
        printf("Ingrese la cantidad de ejemplares\n");
        scanf("%d",&t.ct);
        fwrite(&t,sizeof(titu),1,f);
    }
    fclose(f);
}
void item_a(FILE *f){
titu t;
if ((f=fopen("TITULOS.dat","rb"))==NULL)
    printf ("Ocurrio un error\n");
rewind(f);
fread(&t,sizeof(titu),1,f);
    while (feof(f)==0){
        printf ("Pelicula: %s\n",t.titulo);
        printf ("Cantidad de ejemplares: %d\n",t.ct);
        printf("\n");
        fread(&t,sizeof(titu),1,f);
    }
    fclose(f);
}

void busca (FILE *f,int code){
titu t;
if ((f=fopen("TITULOS.dat","rb"))==NULL)
    printf ("Ocurrio un error\n");
rewind(f);
fread(&t,sizeof(titu),1,f);
    while (!feof(f)&&(t.cod!=code)){
        fread(&t,sizeof(titu),1,f);
    }
    if (!feof(f)){
        printf ("Pelicula encontrada\n");
        printf ("Titulo: %s\n",t.titulo);
        printf("Cantidad de ejemplares: %d\n",t.ct);
    }
    else printf ("La pelicula no se encuentra almacenada en el archivo\n");

fclose(f);
}

void item_b (FILE *f){
int cod;
printf ("Ingrese un codigo de pelicula para observar sus datos\n");
scanf("%d",&cod);
busca(f,cod);
}

int calcula (FILE *f,int &men,cadena dir){
titu t;
int cant=0;
if ((f=fopen("TITULOS.dat","rb"))==NULL)
    printf ("Ocurrio un error\n");
rewind(f);
fread(&t,sizeof(titu),1,f);
    while (feof(f)==0){
        if (stricmp(t.direc,dir)==0){
            cant++;
        }
        if (t.ct<2){
            men+=1;
        }
       fread(&t,sizeof(titu),1,f); 
    }
fclose(f);
return cant;
}
void item_c(FILE *f,cadena dir){
int c,men_2=0;
c=calcula(f,men_2,dir);
printf ("El total de peliculas realizadas por el director %s es de %d y de todas las peliculas existen %d que poseen menos de 2 ejemplares\n",dir,c,men_2);
}

int calcula_d(FILE *f,cadena dir){
titu t;
int cant=0;
if ((f=fopen("TITULOS.dat","rb"))==NULL)
    printf ("Ocurrio un error\n");
rewind(f);
fread(&t,sizeof(titu),1,f);
    while (feof(f)==0){
        if (stricmp(t.direc,dir)==0){
            cant++;
        }
       fread(&t,sizeof(titu),1,f); 
    }
fclose(f);
return cant;
}

void item_d (FILE *f,titu *&t,cadena dir,int ct){
int i=0;
titu aux;
t=(titu*)malloc(sizeof(titu)*ct);
    if ((f=fopen("TITULOS.dat","rb"))==NULL)
    printf ("Ocurrio un error\n");
rewind(f);
fread(&aux,sizeof(titu),1,f); 
    while (feof(f)==0){
        if (stricmp(aux.direc,dir)==0){
            t[i].cod=aux.cod;
            t[i].ct=aux.ct;
            i++;
        }
        fread(&aux,sizeof(titu),1,f); 
    }
    fclose(f);
}
int calculo_e (titu *tit,int ct,int &men,int i){
    if (i<ct){
        if (tit[i].ct<2){
            men+=1;
            return 1+calculo_e(tit,ct,men,i+1);
        }
        else return 1+calculo_e(tit,ct,men,i+1);
    }
    else return 0;
}

int main(){
FILE *f;
titu *tit;
int ct;
cadena dir;
int op;
    do {
        system("cls");
        op=menu();
        switch(op){
            case 1:{
                carga(f);
            }
            break;
            case 2:{
                item_a(f);
                system("pause");
            }
            break;
            case 3:{
                item_b(f);
                system("pause");
            }
            break;
            case 4:{
                 printf ("Ingrese el nombre de un director para observar su informacion\n");
                fflush(stdin);
                gets(dir);
                item_c(f,dir);
                system("pause");
            }
            break;
            case 5:{
                ct=calcula_d(f,dir);
                item_d(f,tit,dir,ct);
                system("pause");
            }
            break;
            case 6:{
             int d,menos=0;
             d=calculo_e(tit,ct,menos,0);
             printf ("Para el director %s el total de peliculas es de %d y la cantidad de peliculas de este mismo con menos de 2 ejemplares es de %d\n",dir,d,menos); 
             system("pause");  
            }
            break;
        }
    }
    while(op!=7);
free(tit);
}

/*
Lote de prueba
2
Avengers
Stuart
6
4
Venom
Stuart
1
1
Bajo La Luna
Margaret
7
9
Tom y Jerry
Spirit
1
*/