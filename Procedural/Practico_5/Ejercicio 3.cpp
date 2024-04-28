#include <stdio.h>
#include <stdio.h>
#include <string.h>
#include <malloc.h>
#define N 2

typedef struct 
{
    int DNI;
    float monto;
}adju;


 typedef struct 
{
    adju *ad;
    int ct;
}plan;

void carga_ad(plan p[N],int j,int n,int i){
    if (j<n){
        printf ("Ingrese el DNI del adjudicatario %d\n",j+1);
        scanf("%d",&p[i].ad[j].DNI);
        printf ("Ingrese el monto del adjudicatario %d\n",j+1);
        scanf("%f",&p[i].ad[j].monto);
        carga_ad(p,j+1,n,i);
    }
}
void carga_prueba(adju ad[],int i,int ct){
    if (i<ct){
        printf ("Ingrese el DNI del adjudicatario %d\n",i+1);
        scanf("%d",&ad[i].DNI);
        printf ("Ingrese el monto del adjudicatario %d\n",i+1);
        scanf("%f",&ad[i].monto);
        carga_prueba(ad,i+1,ct);
    }

}
void carga (plan p[N],int i){
    if  (i<N){
        printf ("Ingrese la cantidad de adjudicatarios del plan %d\n",i+1);
        scanf("%d",&p[i].ct);
        p[i].ad=(adju*)malloc(p[i].ct*sizeof(adju));
      /*  carga_ad(p,0,p[i].ct,i);*/
        carga_prueba(p[i].ad,0,p[i].ct);
        /*
        for (int j=0;j<p[i].ct;j++){
            printf ("Ingrese el DNI del adjudicatario %d\n",j+1);
            scanf("%d",&p[i].ad[j].DNI);
            printf ("Ingrese el monto adeudado del adjudicatario %d\n",j+1);
            scanf("%d",&p[i].ad[j].monto);
        }
        */
        carga(p,i+1);
    }
}
void mostrar (plan p[N]){
int i,j;
    for (i=0;i<N;i++){
        printf ("--PLAN N: %d--\n",i+1);
        for (j=0;j<p[i].ct;j++){
            printf ("Adjudicatario %d -DNI: %d Adeuda: %.2f\n",j+1,p[i].ad[j].DNI,p[i].ad[j].monto);
        }
    }
}
int buscar (plan p[N],int &j,int dn){
int i=0;
    while ((i<N) && (p[i].ad[j].DNI!=dn)){
        if(j<p[i].ct){
            j++;
        }
        else {i++;
            j=0;
        }
    }
    if (i<N){
        return i;
    }
    else return -1;
}
int main(){
plan p[N];
int dn,b,j=0;
carga(p,0);
mostrar(p);
printf ("Ingrese el un DNI \n");
scanf ("%d",&dn);
b=buscar(p,j,dn);
    if (b!=-1){
        printf ("\nEl adjudicatario con DNI %d se adhirio al plan %d y el monto total adeudado es de: %.2f\n",dn,b+1,p[b].ad[j].monto);
    }
    else printf ("DNI Ingresado incorrecto\n");
system("pause");
}