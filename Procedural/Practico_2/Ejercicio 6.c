#include <stdio.h>
#define M 6
#define D 8

void cerea (float arre[M][D],float depto[D]){
int i,j;
    for (i=0;i<M;i++){
        for (j=0;j<D;j++){
            arre[i][j]=0;
            depto[j]=0;
        }
    }

}
int validar (){
int num;
    printf("Ingrese el mes que se realizo la venta(1-6): 0 para terminar\n");
    scanf("%d",&num);
    while ((num<1) && (num>M)&& (num!=0)){
        printf("Mes incorrecto ingrese nuevamente");
    }
    return(num);
}

void carga (float arre[M][D]){
int mes,nump;
float imp;
    mes=validar();
    while (mes!=0){
        printf("Ingrese el numero de departamento (1-8)\n");
        scanf("%d",&nump);
        printf("Introduzca el importe de la venta realizada\n");
        scanf("%f",&imp);
        arre[mes-1][nump-1]+=imp;
        mes=validar();
    }
}
void imp_cdep (float arre[M][D], float depto[D]){
int i,j;
    for (i=0;i<M;i++){
        for (j=0;j<D;j++){
            depto[j]+=arre[i][j];
        }
    }
}
int menor_ve (float depto[D]){
int i,dep=0;
float min=depto[0];
    for (i=1;i<D;i++){
        if (depto[i]<min){
            min=depto[i];
            dep=i;
        }
    }
return (dep+1);
}


float imp_prom (float depto[D]){
int i;
float suma=0;
    for (i=0;i<D;i++){
        suma+=depto[i];
    }
    return (suma/(M*D));
}


void item_d (float depto[D],float p){
int i;
    for (i=0;i<D;i++){
        if (depto[i]>p){
            printf ("El departamento %d supera la venta promedio con un importe total de: $ %.2f\n",i+1,depto[i]);
        }
    }
}
void mostrar (float depto[D]){
int i;
    for (i=0;i<D;i++){
        printf ("Depto %d importe: %.2f\n",i+1,depto[i]);
    }

}
int main(){
float arre[M][D],depto[D],p;
cerea(arre,depto);
carga(arre);
imp_cdep(arre,depto);
p=imp_prom(depto);
printf ("El departamento que tuvo menor importe de venta en base al semestre fue el: %d\n",menor_ve(depto));
printf("El importe promedio de venta del supermercado es de: $ %.2f\n",p);
item_d(depto,p);
//mostrar(depto);

}
