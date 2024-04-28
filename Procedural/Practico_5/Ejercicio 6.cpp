#include <stdio.h>
#include <malloc.h>
#include <stdlib.h>
#include <string.h>
#define N 2
typedef char cadena[30];

struct nodo
{
    cadena nom;
    cadena nom_c;
    cadena reino;
    int ct;
    struct nodo *sig;
};

typedef struct 
{
    cadena ps;
    cadena contin;
    struct nodo *esp;
}dato;
typedef struct nodo *especies;

void crear(dato &d){
d.esp=NULL;
}

void carga_esp(especies &es){
especies nuevo;
cadena nm;
    printf ("Ingrese el nombre de la especie: FIN para terminar\n");
    fflush(stdin);
    gets(nm);
    while (stricmp(nm,"FIN")!=0){
        nuevo=(especies)malloc(sizeof(struct nodo));
        strcpy(nuevo->nom,nm);
        printf ("Ingrese el nombre cientifico de la especie \n");
        fflush(stdin);
        gets(nuevo->nom_c);
        printf ("Ingrese el reino  de la especie \n");
        fflush(stdin);
        gets(nuevo->reino);
        printf ("Ingrese cantidad de ejemplares de la especie\n");
        scanf("%d",&nuevo->ct);
        nuevo->sig=es;
        es=nuevo;
        printf ("Ingrese el nombre de la especie: FIN para terminar\n");
        fflush(stdin);
        gets(nm);
    }
}
void carga (dato pais[N]){
int i;
    for (i=0;i<N;i++){
        printf ("Ingrese el nombre del pais %d\n",i+1);
        fflush(stdin);
        gets(pais[i].ps);
        printf ("Ingrese el continente del pais %d\n",i+1);
        fflush(stdin);
        gets(pais[i].contin);
        crear(pais[i]);
        printf ("--CARGA DE ESPECIES PARA EL PAIS %s\n",pais[i].ps);
        carga_esp(pais[i].esp);
    }
}
void mostrar (dato pais[N]){
int i;
especies x;
    for (i=0;i<N;i++){
        printf ("Datos del pais %s\n",pais[i].ps);
        x=pais[i].esp;
        while (x!=NULL){
            printf ("Nombre: %s-Nombre cientifico: %s- Reino:%s-Cantidad:%d\n",x->nom,x->nom_c,x->reino,x->ct);
            x=x->sig;
        }
    }
}
int busca(dato pais[N],cadena p,int i){
    if (i==N){
        return -1;
    }
    else if (strcmp(pais[i].ps,p)==0){
        return i;
    }
    else return busca(pais,p,i+1);
}
int calcula (especies es,int &d){
    if (es!=NULL){
        if(stricmp(es->reino,"Flora")==0){
            return 1+calcula(es->sig,d);
        }
        else if(stricmp(es->reino,"Fauna")==0){
            d=d+1;
        }
        calcula(es->sig,d);
    }
    else return 0;
}
void incrementa(especies &es){
    if (es!=NULL){
        if ((stricmp(es->nom,"Petiribi")==0)&&(stricmp(es->nom_c,"Arbol")==0)){
            es->ct=es->ct+200;
        }
       else incrementa(es->sig);
    }
    else  printf ("FIN DEL INCREMENTO\n");
}
int item_d(especies es){
    while ((es!=NULL))
    {
        if ((stricmp(es->nom,"Petiribi")==0)&&(stricmp(es->nom_c,"Arbol")==0)){
            return es->ct;
        }
        else es=es->sig;
    }
}
/*
int item_d (especies es){
    if(es==NULL){
        printf("La especie no se encuentra dentro del registro\n");
    }
    else if ((stricmp(es->nom,"Petiribi")==0)&&(stricmp(es->nom_c,"Arbol")==0)){
        return es->ct;
    }
    else item_d(es->sig);
}
*/
int main(){
dato pais[N];
cadena pa;
int b,cont,d=0;
carga(pais);
mostrar(pais);
printf ("Ingrese un pais para determinar la cantidad de especies de la flora y fauna en peligro de extincion\n");
fflush(stdin);
gets(pa);
b=busca(pais,pa,0);
cont=calcula(pais[b].esp,d);
printf ("\nPara el pais %s la cantidad de especies de la flora es de %d y de la fauna es %d\n",pais[b].ps,cont,d);
incrementa(pais[1].esp);
printf ("\nLa cantidad de Petiribi-Arbol presente en Argentina es de %d y en Brasil de %d\n",item_d(pais[0].esp),item_d(pais[1].esp));
system("pause");
}