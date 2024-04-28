#include <stdio.h>
#include <string.h>
#define P 3
#define N 3
/*Una tienda de ropa comercializa 50 productos diferentes. Por cada producto se conoce: código (número entero
que varía entre 1 y 50), precio de costo y stock.
La tienda hace compras a 22 proveedores, de los cuales se conoce: Nombre y Número de Proveedor (es un
numero entre 1000 y 1022).
Se pide redactar un algoritmo en C que, usando estructuras de datos óptimas y subprogramas eficientes,
permita:
a) Almacenar en estructuras de datos adecuadas la información de los Producto y de los Proveedores.
b) Procesar las compras realizadas a los Proveedores, sabiendo que por cada compra se conoce el Número de
Proveedor, Código de Producto y Cantidad de unidades compradas. Con la información de cada compra
se debe actualizar el stock del producto y contar para cada proveedor la compra realizada.
c) Informar cuánto dinero hay invertido en cada producto.
d) Generar una nueva estructura de datos que contenga todos los datos de aquellos Proveedores a quienes se
les haya realizado más de 10 compras.
e) Mostrar la estructura de datos generada en el inciso d) ordenada alfabéticamente por Nombre de proveedor.
f) Ingresar por teclado un Nombre de proveedor e informar su Número y cantidad de compras realizadas.
Nota: Utilizar la estructura de datos generada en el inciso d)*/

typedef struct{
int   stock;
float precio;
}productos;

typedef struct{
char nombre[30];
int num;
int cont;
}proveedor;

void inicia1 (productos prod[P]){
int i;
    for (i=0;i<P;i++){
        printf ("\nIngrese el precio y stock del producto %d\n",i+1);
        scanf("%f",&prod[i].precio);
        scanf("%d",&prod[i].stock);
    }

}
int validar (){
int num;
	printf("Ingrese el numero del proveedor\n");
	scanf("%d",&num);
	while ((num<1000)|| (num>1022)){
	printf("Ingrese nuevamente el numero del proveedor\n");
	scanf("%d",&num);
	}
	return (num);
}
void inicia2 (proveedor prov[N]){
int i, num;
    for (i=0;i<N;i++){
        prov[i].num=validar();
        printf ("\nIngrese el nombre del proveedor %d\n",prov[i].num);
        fflush(stdin);
        gets(prov[i].nombre);
        prov[i].cont=0;
       // prov[i].num=i+1000;
    }

}

/*void mostrar1 (productos prod[P]){
int i;
    for (i=0;i<P;i++){
        printf("\nProducto: %d :Precio:%.2f-Stock:%d\n",i+1,prod[i].precio,prod[i].stock);
    }
}
void mostrar2 (proveedor prov[N]){
int i;
    for (i=0;i<N;i++){
        printf("\nProveedor: %d :Nombre:%s\n",prov[i].num,prov[i].nombre);
    }
}
*/
int busqueda (proveedor prov[N], int nm){
int i=0;
    while ((i<N) && (prov[i].num!=nm)){
        i++;
    }
    if (i<N){
        return (i);
    }
    else {
        return (-1);
    }
}


void compras (productos prod[P],proveedor prov[N]){
int nm, codp,cant,pos;
    fflush(stdin);
    printf ("Ingrese el numero del Proveedor: 0 para finalizar\n");
    scanf ("%d",&nm);
    while (nm!=0){
        pos=busqueda(prov,nm);
        if (pos!=-1){
                prov[pos].cont++;
                printf("Ingrese el codigo de producto\n");
                scanf("%d",&codp);
                printf("Ingrese la cantidad de unidades a comprar\n");
                scanf("%d",&cant);
                prod[codp-1].stock=prod[codp-1].stock+cant;
        }
        else {
            printf ("Numero de proveedor erroneo, ingresar nuevamente\n");
        }
        fflush(stdin);
        printf ("\nIngrese el numero del Proveedor: 0 para finalizar\n");
    scanf ("%d",&nm);
    }
printf("\n");
}
void itemc (productos prod[P]){
int i;
    for (i=0;i<P;i++){
        printf("El dinero invertido en el producto %d es: %.2f\n",i+1,(prod[i].precio*prod[i].stock));
    }
}

int mas_10c(proveedor prov[N], proveedor provmas10[N]){
int i, j;
j=0;
    for (i=0;i<N;i++){
        if(prov[i].cont>1){
            provmas10[j]=prov[i];
                    j++;
        }
    }
    return(j);

}
void ordenar(proveedor provmas10[N],int mas10 ){            //metodo burbuja mejorado
	int k = 1, i,cota = mas10 - 1;
    proveedor aux;
	while(k != -1){
		k = -1;

		for(i = 0; i < cota; i++){
			if(strcmp(provmas10[i].nombre,provmas10[i+1].nombre)>0){           //ascendente
				aux=provmas10[i];
				provmas10[i]= provmas10[i + 1];
				provmas10[i + 1]= aux;
				k = i;
			}
		}

		cota = k;
	}
}
void item_e (proveedor provmas10[N], int mas10){
int i;
    printf("\nNombres de proveedores ordenados alfabeticamente a quienes se le realizaron mas de 10 compras\n");
    for (i=0;i<mas10;i++){
        printf("\n Proveedor: %s - Numero: %d - Cantidad de compras:%d \n",provmas10[i].nombre,provmas10[i].num,provmas10[i].cont);
    }
printf("\n");
}
int busca(proveedor provmas10[N],int mas10, char nom[30]){
int inf,sup,medio;
inf=0;
sup=mas10-1;
medio=(inf+sup)/2;
    while ((inf<=sup)&& (strcmp(provmas10[medio].nombre,nom))!=0){
        if (strcmp(provmas10[medio].nombre,nom)>0)
		{
            sup=medio-1;
        }

        else{
	    	inf=medio+1;
            }
            medio=(inf+sup)/2;
	}
    if (inf<=sup){
        return(medio);
    }
    else {return(-1);}

}
int main(){
productos prod[P];
proveedor prov[N], provmas10[N];
int mas10, b;
char nom[30];
inicia1(prod);
inicia2(prov);
//mostrar1(prod);
//mostrar2(prov);
compras(prod,prov);
itemc(prod);
mas10=mas_10c(prov,provmas10);
ordenar(provmas10,mas10);
item_e(provmas10,mas10);
printf("\nIngrese el nombre de un proveedor con mas de 10 ventas para ver su informacion\n");
fflush(stdin);
gets(nom);
b=busca(provmas10,mas10,nom);
    if (b!=-1){
        printf("\nDatos del nombre ingresado- Numero:%d - Cantidad de compras realizadas:%d\n",provmas10[b].num,provmas10[b].cont);
    }
    else{printf("Nombre incorrecto");
        }
}
