#include <stdio.h>
#define N 3

typedef struct{
float precio;
int ct_u;
int codigo;
}industria;

void inicia (industria ind[N]){
int i,cod;
    for (i=0;i<N;i++){
        printf ("Ingrese codigo de producto(100-169)\n");
        scanf("%d",&cod);
        ind[i].codigo=cod;
        printf("Ingrese el precio unitario del producto con el codigo %d\n",cod);
        scanf("%f",&ind[i].precio);
        ind[i].ct_u=0;
    }
}
int busqueda (industria ind[N],int cod){
int i=0;
    while ((i<N) && (ind[i].codigo!=cod)){
        i++;
    }
    if (i<N){
        return (i);
    }
    else {return (-1);}
}
void carga (industria ind[N]){
int cod,cant,b;
    printf ("Ingrese el codigo de un producto: 0 para terminar(VENTAS)\n");
    scanf("%d",&cod);
    while (cod!=0){
        b=busqueda(ind,cod);
        if (b!=-1){
            printf ("Ingrese la cantidad de unidades a vender\n");
            scanf ("%d",&cant);
            ind[b].ct_u+=cant;
        }
        else {printf("Codigo de producto incorrecto\n");}
    printf ("Ingrese el codigo de un producto: 0 para terminar\n");
    scanf("%d",&cod);
    }
}
void mostrar_a (industria ind[N]){
int i;
    for (i=0;i<N;i++){
        printf ("\nEl total de unidades vendidas del producto %d es de: %d\n",ind[i].codigo,ind[i].ct_u);
    }

}
int maxim (industria ind[N]){
int i,cd;
float max=(ind[0].ct_u*ind[0].precio);
    for (i=0;i<N;i++){
        if ((ind[i].ct_u*ind[i].precio)>max){
            max=(ind[i].ct_u*ind[i].precio);
            cd=i;
        }
    }
    return (cd);
}

int busca (industria ind[N],int code){
int i=0;
    while ((i<N) && (ind[i].codigo!=code)){
        i++;
    }
    if (i<N){
        return (i);
    }
}
void mostrar_c (industria ind[N]){
int code,b;
    printf ("\nIngrese el codigo de un producto para determinar la cantidad de unidades vendidas\n");
    scanf ("%d",&code);
    b=busca(ind,code);
    printf ("\nLa cantidad de unidades vendidas del codigo %d, es: %d\n",code,ind[b].ct_u);
}
void mostrar_d (industria ind[N]){
int i,cont=0;
    for (i=0;i<N;i++){
        if ((ind[i].ct_u>=2) && (ind[i].ct_u<=5)){
            cont++;
        }
    }
    printf ("\nLa cantidad de productos que se vendieron entre 20 y 50 unidades fue de: %d\n",cont);
}

int main(){
industria ind[N];
int c;
inicia(ind);
carga(ind);
mostrar_a(ind);
c=maxim(ind);
printf ("\nEl codigo de producto que recaudo un mayor importe es el %d\n",ind[c].codigo);
mostrar_c(ind);
mostrar_d(ind);

}
