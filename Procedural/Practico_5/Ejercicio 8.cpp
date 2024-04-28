#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <malloc.h>

typedef char cadena[30];

struct nodo{
cadena nom;
float prom;
int anio;
struct nodo*sig;
};
typedef struct{
    cadena nombre;
    struct nodo *ins;
}datos;
typedef struct nodo *inscripciones; 

void crear(datos &d){
d.ins=NULL;
}
void inicia (datos *facu,int N,int i){
    if (i<N){
        printf ("Ingrese el nombre de la facultad %d\n",i+1);
        fflush(stdin);
        gets(facu[i].nombre);
        crear(facu[i]);
        inicia(facu,N,i+1);
    }
}
void inserta(inscripciones &in,cadena nm){
inscripciones nuevo;
nuevo=(inscripciones)malloc(sizeof(struct nodo));
strcpy(nuevo->nom,nm);
printf ("Ingrese el promedio del alumno\n");
scanf("%f",&nuevo->prom);
printf ("Ingrese el año que cursa el alumno\n");
scanf("%d",&nuevo->anio);
nuevo->sig=in;
in=nuevo;
}
void carga (datos *facu,int N){
int i;
cadena nm;
    for (i=0;i<N;i++){
        printf ("--CARGA DE INSCRIPCIONES PARA LA FACULTAD %d--\n",i+1);
        printf("Ingrese el nombre del alumno:FIN para terminar\n");
        fflush(stdin);
        gets(nm);
        while (strcmp(nm,"FIN")!=0)
        {
        inserta(facu[i].ins,nm);
        printf("Ingrese el nombre del alumno:FIN para terminar\n");
        fflush(stdin);
        gets(nm);
        }      
    }
}
void muestra (datos *facu,int N){
int i;
inscripciones x;
    for (i=0;i<N;i++){
        printf ("Alumnos de la facultad %s\n",facu[i].nombre);
        x=facu[i].ins;
        while (x!=NULL)
        {
            printf ("Nombre: %s-Promedio: %.2f-Anio: %d\n",x->nom,x->prom,x->anio);
            x=x->sig;
        }
    }
}
int busca (datos *facu,int N,cadena fc){
int i=0;
    while ((i<N)&&(stricmp(facu[i].nombre,fc)!=0))
    {
        i+=1;
    }
    if (i<N){
        return i;
    }
    else return -1;
}
void ordena(inscripciones in){
inscripciones k,cota,p;
float aux;
cadena aux_c;
int aux_ani;
cota=NULL;
k=NULL;
    while (k!=in)
    {
        k=in;
        p=in;
        while (p->sig!=cota)
        {
            if(p->prom>p->sig->prom){
               strcpy(aux_c,p->sig->nom); 
               strcpy(p->sig->nom,p->nom);
                strcpy(p->nom,aux_c); 
                aux=p->sig->prom;
                p->sig->prom=p->prom;
                 p->prom=aux;
                aux_ani=p->sig->anio;    
                p->sig->anio=p->anio;       
                p->anio=aux_ani;      
                k=p;
            }
            p=p->sig;
        }
        cota=k->sig;     
    }  
}
void item_a(inscripciones in){
    if (in!=NULL){
        printf("Nombre: %s\n",in->nom);
        printf("Promedio: %.2f\n",in->prom);
        printf ("Anio que cursa: %d\n",in->anio);
        printf("\n");
        item_a(in->sig);
    }
}

int menos (datos *facu,int N,int &fc){
int i;
inscripciones x;
int min=9999;
    for (i=0;i<N;i++){
        int ct=0;
        x=facu[i].ins;
        while (x!=NULL)
        {
            ct+=1;
            x=x->sig;
        }
        if (ct<min){
            min=ct;
            fc=i;
        }
        
    }
    return min;
}

int calculo(inscripciones in){
    if (in!=NULL){
        if ((in->prom>=7)&&(in->anio>=2)){
            return 1+calculo(in->sig);
        }
        calculo(in->sig);
    }
    else return 0;
}
void item_c (datos *facu,int N,int i){
    if (i<N){
            printf ("\nPara la facultad %s la cantidad de alumnos con promedio mayor a 7 y que cursan de 2 anio en adelante es de %d\n",facu[i].nombre,calculo(facu[i].ins));
            item_c(facu,N,i+1);
        }
    }
/*
void item_c(datos *facu,int N){
int i,ct;
inscripciones x;
    for (i=0;i<N;i++){
        ct=0;
        x=facu[i].ins;
        while (x!=NULL)
        {
            if ((x->prom>=7)&&(x->anio>=2)){
            ct++;
            x=x->sig;
            }
            else x=x->sig;
        }
        printf ("\nPara la facultad %s la cantidad de alumnos con promedio mayor a 7 y que cursan de 2 anio en adelante es de %d\n",facu[i].nombre,ct);
    }
}
*/
int main(){
int N,b,men,f;
cadena fc;
datos *facu;
printf ("Ingrese la cantidad de facultades que participan\n");
scanf("%d",&N);
facu=(datos*)malloc(sizeof(datos)*N);
inicia(facu,N,0);
carga(facu,N);
muestra(facu,N);
printf ("Ingrese el nombre de una facultad para ordenar a los alumnos inscriptos\n");
fflush(stdin);
gets(fc);
b=busca(facu,N,fc);
ordena(facu[b].ins);
printf ("LISTADO ORDENADO POR PROMEDIO\n");
item_a(facu[b].ins);
men=menos(facu,N,f);
printf ("\nLa facultad %s cuenta con la menor cantidad de inscriptos que es de %d\n",facu[f].nombre,men);
item_c(facu,N,0);
//item_c(facu,N);
system("pause");
}