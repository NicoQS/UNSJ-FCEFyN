#include <stdio.h>
#include <malloc.h>
#include <stdlib.h>

 struct nodo 
{
    int num;
    struct nodo *sig;
};

typedef struct nodo *puntero;




void validar (int &nm){
    while (nm<0)
    {
        printf ("ERROR-Ingrese nuevamente un numero entero positivo\n");
        scanf ("%d",&nm);
    }
}

void carga (puntero &cabeza,int dato){
    if (dato!=0){
        validar(dato);
        puntero nuevo;
        nuevo=(puntero)malloc(sizeof(struct nodo));
        nuevo->num=dato;
        if (cabeza==NULL){
            cabeza=nuevo;
            nuevo->sig=NULL;
        }
        else if(dato<=cabeza->num){
            nuevo->sig=cabeza;
            cabeza=nuevo;
        }
            else {
                puntero p,ant;
                p=cabeza->sig;
                ant=cabeza;
                while ((p!=NULL)&&(p->num<nuevo->num)){
                    ant=p;
                    p=p->sig;                 
                }
                ant->sig=nuevo;
                nuevo->sig=p;    
            }
            printf ("Ingrese un numero entero 0 para terminar\n");
            scanf("%d",&dato);
            if (dato!=0){
            validar(dato);
            carga(cabeza,dato);
            }
    }

}
void muestra(puntero cb){
    
    if (cb!=NULL){
        printf ("El nodo es: %d\n",cb->num);
        muestra(cb->sig);
    }

}
void item_b (puntero cb){
    if (cb->sig!=NULL){
        item_b(cb->sig);
    }
    else  if ((cb->num%2)==0){
        printf ("El ultimo nodo es un numero par\n");
    }
    else printf ("El ultimo nodo no es numero par\n");
}

void libera (puntero &cb,puntero p){
    if (cb!=NULL){
        libera(cb->sig,cb);
        free(p);
    }
    else printf ("Memoria liberada\n");
}
int main(){
puntero cabeza;
int nm;
cabeza=NULL;
printf ("Ingrese un numero entero positivo o 0 para terminar\n");
scanf ("%d",&nm);
carga(cabeza,nm);
muestra(cabeza);
item_b(cabeza);
libera(cabeza->sig,cabeza);
system("pause");
}