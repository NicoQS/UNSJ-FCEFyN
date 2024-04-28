#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>
#define N 2

struct nodo{
int dni;
struct nodo *sig;
};
typedef char cadena[30];
typedef struct{
cadena titulo;
struct nodo *ins;
}datos;
typedef struct nodo *inscriptos;

void crear(datos &d){
d.ins=NULL;
}

void carga(datos t[N],int i){
    if (i<N){
        printf ("Ingrese el titulo del tutorial %d\n",i+1);
        fflush(stdin);
        gets(t[i].titulo);
        crear(t[i]);
        carga(t,i+1);
    }
}

void inserta(inscriptos &ins,int dni){
inscriptos nuevo;
    nuevo=(inscriptos)malloc(sizeof(struct nodo));
    nuevo->dni=dni;
    nuevo->sig=ins;
    ins=nuevo;
}


void suprimir (inscriptos &in,int dato)
{
    inscriptos anterior, p;
    if (in->dni == dato)
    {
    p=in;
    in=in->sig;
    free (p); /*eliminación de la cabeza de la lista */
    }
    else
    { p=in;
    anterior=in;
    while ((p != NULL) && (p->dni != dato))
    {
    anterior = p;
    p=p->sig;
    }
    if (p != NULL)
    {
    anterior->sig = p->sig;
    free(p);
    printf("\n El número fue eliminado de la lista");
    }
    else
    printf("\n No se encuentra el número en la lista");
    return;
    }
}

int calcula (inscriptos in){
    if (in!=NULL){
        return 1+calcula(in->sig);
    }
    else return 0;
}
/*
void item_e (datos t[N],int dn){
int i;
inscriptos xp;
    for (i=0;i<N;i++){
        xp=t[i].ins;
        while (xp!=NULL)
        {
            if (xp->dni==dn){
                printf ("\nLa persona con DNI %d se encuentra inscripta en el tutorial %d llamado %s\n",dn,t[i].numero,t[i].titulo);
            }
            xp=xp->sig;
        }
    }
}
*/
int busca (inscriptos in,int dn){
    if (in==NULL){
        return -1;
    }
    else if (in->dni==dn){
        return 1;
    }
    else busca(in->sig,dn);
}

void item_e (datos t[N],int dn,int i)//intento recursiva
{
    int b;
    if (i<N){
            b=busca(t[i].ins,dn);
            if(b!=-1){
            printf ("\nLa persona con DNI %d se encuentra inscripta en el tutorial %d llamado %s\n",dn,i+1,t[i].titulo);
            }
            else printf ("El DNI ingresado no es correcto o no se encuentra inscripto en el tutorial\n",dn,i+1);

            item_e(t,dn,i+1);
        }
    }
int main(){
datos tuto[N];
int op,n,dn;
carga(tuto,0);
    do { 
    system ("cls");
    printf ("\n ******** MENU DE OPCIONES ***********\n");
    printf ("\n 1 - Realizar una inscripcion: ");
    printf ("\n 2 - Eliminar una inscripcion: ");
    printf ("\n 3 - Mostrar Datos de un tutorial(Titulo-Cantidad de inscriptos): ");
    printf ("\n 4 - Mostrar tutoriales en los cuales se inscribio una persona : ");
    printf ("\n 5 - Salir del Menu: \n");
    scanf ("%d", &op);
    switch (op){ 
    case 1: { 
    printf ("Ingrese un numero de tutorial\n");
    scanf("%d",&n);
    printf ("Ingrese su DNI\n");
    scanf("%d",&dn);
    inserta(tuto[n-1].ins,dn);break;
    }
    break; 
    case 2:{ 
       printf ("Ingrese un numero de tutorial\n");
        scanf("%d",&n);
        printf ("Ingrese su DNI\n");
        scanf("%d",&dn);
        suprimir(tuto[n-1].ins,dn);
        }
        break;
        case 3:{ 
        int nm;
        printf("Ingrese el numero de un tutorial para observar sus datos\n");
        scanf("%d",&nm);
        printf ("Para el tutorial %d llamado %s posee una cantidad de %d inscriptos\n",nm,tuto[nm-1].titulo,calcula(tuto[nm-1].ins));
        system("pause");
        }
        break;
        case 4:{ 
            int dn;
            printf ("Ingrese un DNI para mostrar los tutoriales inscriptos\n");
            scanf("%d",&dn);
            //item_e(tuto,dn);
            item_e(tuto,dn,0);
            system("pause");
        }
        break;
    } 
}
    while (op !=5);

}