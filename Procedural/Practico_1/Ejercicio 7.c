#include <stdio.h>
#define F 30
#define M 80
/*Un laboratorio abastece a 30 farmacias de la provincia (las farmacias están codificadas con número entre 1 y
30). Dicho laboratorio comercializa 80 medicamentos (con código desde 100 hasta 179).
En forma ordenada por las farmacias se ingresan las ventas realizadas. Por cada venta se ingresa: código de
medicamento y cantidad de unidades, finalizando con código de medicamento igual a 0 (cero)
a) Realizar la carga de la tabla.
b) Calcular y mostrar total de unidades vendidas de cada uno de los medicamentos.
c) Dado el código de una farmacia, indicar código de medicamento más vendido.
*/
void cerea (int arre[F][M], int medi[M]){
int i,j;
    for (i=0;i<F;i++){
        for (j=0;j<M;j++){
            arre[i][j]=0;
            medi[j]=0;
        }
    }
}

void carga (int arre[F][M]){
int i, codigo,cant;
    for (i=0;i<F;i++){
        printf("Carga de las ventas de la farmacia: %d\n",i+1);
        printf("\nIngrese el codigo de un medicamento: 0 para pasar a la siguiente farmacia o terminar\n");
        scanf("%d",&codigo);
        while (codigo!=0){
        printf("Ingrese la cantidad de medicamentos a comprar\n");
        scanf("%d",&cant);
        arre[i][codigo-100]+=cant;
        printf("\nIngrese el codigo de un medicamento: 0 para pasar a la siguiente farmacia o terminar\n");
        scanf("%d",&codigo);
        }
    }
}
void item_b(int arre[F][M], int medi[M]){
int i,j;
    for (i=0;i<F;i++){ //tambien se puede recorrer por columas a filas for (M) y luego el For (F)
        for (j=0;j<M;j++){
            medi[j]+=arre[i][j];
        }
    }

}
void mostrar_b (int medi[M]){
int i;
    for (i=0;i<M;i++){
        printf("\n--El total de unidades vendidas en el medicamento %d es: %d--\n",i+100,medi[i]);
    }
}
/*
int MedicamentoMV(int arre[M]){
    int j,maximo,indicador;
    maximo=a[0];
        for(j=1;j<M;j++){
            if(maximo<a[j]){
                maximo=arre[j];
                indicador=j;
            }
        }
    return(indicador);
}*/
int mas_ven (int arre[F][M],int cod_farm){
int i=cod_farm-1,j,cod;
int max=arre[i][0];
    for (j=1;j<M;j++){
        if (arre[i][j]>max){
            max=arre[i][j];
            cod=j;
        }
    }
    return(cod+100);
}
void item_c(int arre[F][M]){
int cod_farm,mas;
    printf("\nIngrese el codigo de una farmacia: 0 para finalizar\n");
    scanf("%d",&cod_farm);
    while (cod_farm!=0){
    mas=mas_ven(arre,cod_farm); // mas_ven(arre[cod_farm-1])
    printf("\nEn la farmacia %d el medicamento mas vendido es el de codigo: %d\n",cod_farm,mas);
    printf("Ingrese el codigo de una farmacia: 0 para finalizar\n");
    scanf("%d",&cod_farm);
    }
}
int main(){
int arre[F][M], medi[M];
cerea(arre,medi);
carga(arre);
item_b(arre,medi);
mostrar_b(medi);
item_c(arre);
}





