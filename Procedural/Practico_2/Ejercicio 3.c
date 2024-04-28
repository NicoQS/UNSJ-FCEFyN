#include <stdio.h>
#include <string.h>
#define F 2
#define M 3

/*Un laboratorio abastece a 30 farmacias de la provincia. Dicho laboratorio comercializa 80 medicamentos (1..80) de los
que se debe registrar: Código de medicamento, nombre y precio unitario.
Se ingresan las ventas realizadas ordenada por farmacia. Por cada venta a una farmacia se ingresa: código de
medicamento y cantidad de unidades, finalizando con código de medicamento igual a 0 (cero)
a) Calcular y mostrar total de unidades vendidas de cada uno de los medicamentos.
b) Escribir el/los códigos/s del/los medicamento/s por el que se recaudó mayor importe.
c) Indicar la cantidad de unidades vendidas para un código de medicamento ingresado por teclado.
d) Dado el nombre de un medicamento indicar el importe total recaudado.
e) Indicar la cantidad de unidades vendida a cada farmacia y el importe total que pagó cada una.
*/
typedef struct{
char nom[30];
float precio;
int suma;
}medic;
typedef struct{
int acum;
float importe;
}farmac;
void cerea(int arre[F][M], farmac far[F]){
int i,j;
    for (i=0;i<F;i++){
        far[i].acum=0;
        far[i].importe=0;
        for (j=0;j<M;j++){
            arre[i][j]=0;
        }
    }
}
void inicia1 (medic md[M]){
int i;
    for (i=0;i<M;i++){
        printf("\nIngrese el nombre del medicamento: %d\n",i+1);
        fflush(stdin);
        gets(md[i].nom);
        printf("\nIngrese el precio unitario del medicamento: %d\n",i+1);
        scanf("%f",&md[i].precio);
        md[i].suma=0;
    }
}

void carga (int arre[F][M]){
int i,cod,cant;
    for (i=0;i<F;i++){
        printf("\nIngrese las ventas de la farmacia %d: 0 para terminar o pasar a la farmacia siguiente\n",i+1);
        printf("\nIngrese codigo de medicamento\n");
        scanf("%d",&cod);
        while (cod!=0){
            printf("Ingrese la cantidad de unidades a comprar\n");
            scanf("%d",&cant);
            arre[i][cod-1]+=cant;
        printf("\nIngrese codigo de medicamento\n");
        scanf("%d",&cod);
        }
    }
}

void farm_e (int arre[F][M],farmac far[F],medic md[M]){
int i,j;
    for (i=0;i<F;i++){
        for (j=0;j<M;j++){
            far[i].acum+=arre[i][j];
            far[i].importe+=(arre[i][j]*md[j].precio);
        }
    }
}
void item_a (int arre[F][M], medic md[M]){
int i,j;
    for (i=0;i<F;i++){
       for (j=0;j<M;j++){
            md[j].suma+=arre[i][j];
       }
    }
}
void mostrar_a (medic md[M]){
int i;
    for (i=0;i<M;i++){
        printf("\n--El total de unidades vendidas en el medicamento %d es: %d--\n",i+1,md[i].suma);
    }
}

float mayor (medic md[M]){
int i;
float max_imp=(md[0].precio*md[0].suma);
    for (i=1;i<M;i++){
        if ((md[i].precio*md[i].suma)>max_imp){
            max_imp=(md[i].precio*md[i].suma);
        }
    }
    return (max_imp);
}
void mostrar_b (medic md[M]){
int i;
    for (i=0;i<M;i++){
        if ((md[i].precio*md[i].suma)==mayor(md)){
            printf("\nEl medicamento con el codigo %d es uno de los que recaudo un mayor importe\n",i+1);
        }
    }
}
void mostrar_c (medic md[M]){
int code;
    printf("\nIngrese el codigo de un medicamento para observar la cantidad de unidades vendidas: 0 para terminar\n");
    scanf("%d",&code);
    while (code!=0){
        printf("\nLa cantidad de unidades vendidas en el medicamento %d es de: %d\n",code,md[code-1].suma);
        printf("\nIngrese el codigo de un medicamento para observar la cantidad de unidades vendidas: 0 para terminar\n");
    scanf("%d",&code);
    }
}
int busqueda (medic md[M],char nombre[30]){
int i=0;
    while ((i<M)&&(strcmp(md[i].nom,nombre))!=0){
        i++;
    }
    if (i<M){
        return (i);
    }
    else{
        return (-1);
    }
}
void mostrar_d (medic md[M]){
char nombre[30];
int pos;
    printf("\nIngrese el nombre de un medicamento para observar el importe total recaudado: FIN para terminar\n");
    fflush(stdin);
    gets(nombre);
    while (strcmp(nombre,"FIN")!=0){
    pos=busqueda(md,nombre);
        if (pos!=-1){
             printf("\nEl importe total recaudado en el medicamento %s es de: %.2f\n",nombre,(md[pos].precio*md[pos].suma));
        }
        else {
            printf("\nEl nombre ingresado es incorrecto\n");
        }
    printf("Ingrese el nombre de un medicamento para observar el importe total recaudado: FIN para terminar\n");
    fflush(stdin);
    gets(nombre);
    }
}
void mostrar_e (farmac far[F]){
int i;
    for (i=0;i<F;i++){
        printf ("\nLa cantidad de unidades vendidas a la farmacia %d fue de %d y el importe total que pago es de %.2f\n",i+1,far[i].acum,far[i].importe);
    }
}
int main(){
int arre[F][M];
medic md[M];
farmac far[F];
cerea(arre,far);
inicia1(md);
carga(arre);
farm_e(arre,far,md);
item_a(arre,md);
mostrar_a(md);
mostrar_b(md);
mostrar_c(md);
mostrar_d(md);
mostrar_e(far);
getchar();
}
