#include <stdio.h>
#define N 3
#include <string.h>
typedef struct{
char nombre[30];
int stock;
float precio;
}local;

void inicia (local lo[N]){
int i;
    for (i=0;i<N;i++){
        printf ("Ingrese el nombre del producto %d\n",i+1);
        fflush(stdin);
        gets(lo[i].nombre);
        printf ("Ingrese el stock del producto %d\n",i+1);
        scanf("%d",&lo[i].stock);
        printf ("Ingrese el precio unitario del producto %d\n",i+1);
        scanf("%f",&lo[i].precio);
    }

}

int busqueda (local lo[N], char nom[30]){
int i=0;
    while ((i<N) && (strcmp(lo[i].nombre,nom))!=0){
        i++;
    }
    if (i<N){
        return (i);
    }
    else {return (-1);

    }
}

void carga (local lo[N],float *monto){
char nom[30];
int cant,b;
    printf ("Ingrese el nombre del articulo a vender:FIN para terminar\n");
    fflush(stdin);
    gets(nom);
    while (strcmp(nom,"FIN")!=0){
        b=busqueda(lo,nom);
            if (b!=-1){
                printf ("Ingrese la cantidad de unidades a vender\n");
                scanf("%d",&cant);
                lo[b].stock-=cant;
                *monto+=(lo[b].precio*cant);
            }
            else {printf("Nombre de articulo invalido\n");}
    printf ("Ingrese el nombre del articulo a vender:FIN para terminar\n");
    fflush(stdin);
    gets(nom);
    }

}

void stock_nul(local lo[N]){
int i;
    for (i=0;i<N;i++){
        if (lo[i].stock==0){
            printf ("El articulo %s es uno de los que quedo con stock nulo\n",lo[i].nombre);
        }
    }
}
void indicar_stock (local lo[N]){
int codigo;
    printf ("Ingrese el codigo de un articulo para observar su stock\n");
    scanf("%d",&codigo);
    printf ("El stock que posee el articulo de codigo %d es de: %d",codigo,lo[codigo-1].stock);
}
int item_4 (local lo[N],local sub[N]){
int i,j=0;
float max=lo[0].stock;
    for (i=0;i<N;i++){
        if ((lo[i].stock>max)&&(j<20)){
            max=lo[i].stock;
            strcpy(sub[j].nombre,lo[i].nombre);
            j++;
        }
    }
return (j);
}
void mostrar_4 (local sub[N],int s){
int i;
    printf ("\n--20 ARTICULOS QUE QUEDARON CON MAYOR STOCK--\n");
    for (i=0;i<s;i++){
        printf ("\nNombre: %s\n",sub[i].nombre);
    }
}

int main(){
local lo[N],sub[N];
int s;
float monto=0;
inicia(lo);
carga(lo,&monto);
stock_nul(lo);
indicar_stock(lo);
s=item_4(lo,sub);
mostrar_4(sub,s);
printf ("El monto total obtenido de la ventas de productos es de: %.2f\n",monto);
}
