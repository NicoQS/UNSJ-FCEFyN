#include <stdio.h>
#define M 6
#define D 8


void cerea (float arre[M][D]){
int i,j;
    for (i=0;i<M;i++){
        for (j=0;j<D;j++){
            arre[i][j]=0;
        }
    }

}

int validar (){
int num;
    printf("Ingrese el mes que se realizo la venta(1-12): 0 para terminar\n");
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
/*
void mostrar (float arre[12][8]){
int i,j;
    printf("\t\t\tDepartamentos\n\t  [ 1 \t 2\t 3\t 4\t 5\t 6\t 7\t 8]\n\n");
    for (i=0;i<12;i++){
        printf("{Mes %d}  ",i+1);
        for (j=0;j<8;j++){
            printf(" %.2f\t",arre[i][j]);
        }
        printf("\n");
    }
    printf("    \t\t\t[Importe total]\t");
}
*/
int menor_vent (float arre[M][D],int ms){
int i=ms-1,j=0,dep;
float min=arre[i][0];
    for (j=1;j<D;j++){
        if (arre[i][j]<min){
            min=arre[i][j];
            dep=j;
        }
    }
    return (dep+1);
}

int item_b (float arre[M][D]){
int ms, menos;
    printf("Ingrese un mes para determinar el departamento que menos vendio, luego 0 para terminar y ver el departamento\n");
    scanf("%d",&ms);
    while (ms!=0){
    menos=menor_vent(arre,ms);
    printf("Ingrese un mes para determinar el departamento que menos vendio, luego 0 para terminar y ver el departamento\n");
    scanf("%d",&ms);
    }
    return(menos);
}

float imp_prom (float arre[M][D]){
int i, j;
float suma=0;
    for (i=0;i<M;i++){
        for (j=0;j<D;j++){
            suma+=arre[i][j];
        }
    }
    return (suma/M*D);
}

void supera (float arre[M][D]){
int mes,dep;
    printf("Ingrese un mes y departamento para determinar si supera el importe promedio: 0 para finalizar\n");
    scanf("%d",&mes);
    while (mes!=0){ // no es necesario se puede acceder directamente
        printf("Ingrese el departamento\n");
        scanf("%d",&dep);
        if (arre[mes-1][dep-1]>imp_prom(arre)){
            printf("En el mes %d, el departamento %d supera el importe promedio\n",mes,dep);
        }
        else {printf("En el mes %d, el departamento %d no supero el importe promedio\n",mes,dep);
        }
    printf("Ingrese un mes para determinar si supera el importe promedio: 0 para finalizar\n");
    scanf("%d",&mes);
    }
}
int main(){
float arre[M][D];
cerea(arre);
carga(arre);
//mostrar(arre);
printf("\nEl departamento que menos vendio es el: %d\n",item_b(arre));
printf("El importe promedio de venta del supermecado es de: %.2f\n",imp_prom(arre));
supera(arre);
}
