#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define N 4
typedef char cadena[30];
typedef struct{
cadena titulo;
cadena direc;
int cant;
int cod;
}titu;
struct nodo{
cadena nombre;
cadena peli;
int ct;
struct nodo *sig;
};
typedef struct nodo *lista;
int menu(){
int d;
    printf ("Ingrese una opcion\n");
    printf ("1: Crear archivo TITULO.dat ordenado\n");
    printf("2: Dado un codigo de pelicula se muestra su informacion\n");
    printf("3: Eliminacion de una pelicula y muestra el total de peliculas\n");
    printf("4: Genera una lista con la informacion de TITULOS.dat\n");
    printf("5: Salir\n");
    scanf("%d",&d);
    return d;
}

void carga (FILE *f){
titu t;
int i,code;
fpos_t x;
    if ((f=fopen("TITULOS.dat","wb"))==NULL)
    printf ("Ocurrio un error\n");

    for (i=0;i<N;i++){
        fseek(f,0,SEEK_END);
        fgetpos(f,&x);
        code=(int)(x/sizeof(titu))+1;
        t.cod=code;
        printf ("Ingrese el Titulo de la pelicula con el codigo %d\n",t.cod);
        fflush(stdin);
        gets(t.titulo);
        printf ("Ingrese el director de la pelicula con el codigo %d\n",t.cod);
        fflush(stdin);
        gets(t.direc);
        printf ("Ingrese la cantidad de ejemplares de la pelicula\n");
        scanf("%d",&t.cant);
        fwrite(&t,sizeof(titu),1,f);
    }
    fclose(f);
}

void informa (FILE *f,int pos){
titu t;
     if ((f=fopen("TITULOS.dat","rb"))==NULL)
    printf ("Ocurrio un error\n");
rewind(f);
    fseek(f,pos*sizeof(titu),SEEK_SET);
    fread(&t,sizeof(titu),1,f);
    if (!feof(f)){
    printf ("-Pelicula encontrada-\n");
    printf ("Titulo: %s\n",t.titulo);
    printf("Cantidad de ejemplares: %d\n",t.cant);
    }
    else printf ("La pelicula no se encuentra en el archivo\n");
fclose(f);
}
void item_a(FILE *f){
int code;
printf ("Ingrese el codigo de una pelicula para observar su informacion\n");
scanf("%d",&code);
informa(f,code-1);
}
void marcar (FILE *f){
titu t;
int b;
cadena peli;
  if ((f=fopen("TITULOS.dat","r+"))==NULL)
    printf ("Ocurrio un error\n");

    printf ("Ingrese el nombre de una pelicula a eliminar: FIN para terminar\n");
    fflush(stdin);
    gets(peli);
    while(stricmp(peli,"FIN")!=0){
        b=0;
        fseek(f,0,SEEK_SET);
        while ((b==0)&&(fread(&t,sizeof(titu),1,f))){
            if (stricmp(t.titulo,peli)==0)
            b=1;
        }
        if (b==1){
            fseek(f,-sizeof(titu),SEEK_CUR);
            t.cod=-1;
            fwrite(&t,sizeof(titu),1,f);
            printf ("La pelicula %s fue marcada para eliminar\n",t.titulo);
        }
        else printf ("No se encontro la pelicula ingresada\n");
    printf ("Ingrese el nombre de una pelicula a eliminar: FIN para terminar\n");
    fflush(stdin);
    gets(peli);
    }
    fclose(f);
}
void compactar (FILE *f,FILE *aux){
titu t;
 if ((f=fopen("TITULOS.dat","rb"))==NULL)
    printf ("Ocurrio un error\n");

    fseek(f,0,SEEK_SET);
    fread(&t,sizeof(titu),1,f);
    while (!feof(f)){
        if (t.cod!=-1){
            fwrite(&t,sizeof(titu),1,aux);
        }
        fread(&t,sizeof(titu),1,f);
    }
    fclose(f);
}
void elimina (FILE *f){
FILE *aux;
marcar(f);
aux=fopen("auxiliar.dat","wb");
compactar(f,aux);
fclose(aux);
remove("TITULOS.dat");
rename("auxiliar.dat","TITULOS.dat");
}

void item_b (FILE *f){
titu t;
fpos_t x;
int cant;
 if ((f=fopen("TITULOS.dat","rb"))==NULL)
    printf ("Ocurrio un error\n");
fseek(f,0,SEEK_END);
fgetpos(f,&x);
cant=x/sizeof(titu);
printf ("Luego de la eliminacion la cantidad de peliculas es de %d\n",cant);
fclose(f);
}

void genera_lista (FILE *f,lista &li){
titu t;
lista nuevo;
if ((f=fopen("TITULOS.dat","rb"))==NULL)
    printf ("Ocurrio un error\n");
rewind(f);
    fread(&t,sizeof(titu),1,f);
    while(!feof(f)){
        nuevo=(lista)malloc(sizeof(struct nodo));
        strcpy(nuevo->nombre,t.direc);
        strcpy(nuevo->peli,t.titulo);
        nuevo->ct=t.cant;
        nuevo->sig=li;
        li=nuevo;
        fread(&t,sizeof(titu),1,f);
    }
    printf ("--LISTA GENERADA CORRECTAMENTE--\n");
    fclose(f);
}

void mostrar (lista li){
    while (li!=NULL){
        printf ("Director: %s\n",li->nombre);
        printf("Pelicula: %s\n",li->peli);
        printf("Cantidad de ejemplares: %d\n",li->ct);
        printf ("\n");
        li=li->sig;
    }
}
int main(){
FILE *f;
int op;
    do {
        system("cls");
        op=menu();
        switch (op)
        {
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
           elimina(f);
           item_b(f);
           system("pause");
        }
        break;
        case 4:{
            lista li;
            li=NULL;
            genera_lista(f,li);
            mostrar(li);
            system("pause");
        }
        break;
        }
    }
    while(op!=5);
}
/*
Lote de prueba
Avengers
Stuart
6
Venom
Stuart
1
Bajo La Luna
Margaret
7
Tom y Jerry
William
1

*/