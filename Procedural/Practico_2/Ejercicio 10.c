#include <stdio.h>
#include <string.h>
#define P 3
#define C 2

typedef struct{
char nombre[30];
float precio;
int cant_tot;
}prendas;
typedef struct{
int CUIL;
char nom[30];
float imp_tot;
}comercio;

void cerear (int tabla[C][P]){
int i,j;
    for (i=0;i<C;i++){
        for (j=0;j<P;j++){
            tabla[i][j]=0;
        }
    }
}

void inicia1 (prendas pren[P]){
int i;
    for (i=0;i<P;i++){
        printf ("\nIngrese el nombre de la prenda %d\n",i+1);
        fflush(stdin);
        gets(pren[i].nombre);
        printf ("\nIngrese el precio unitario de la prenda %d\n",i+1);
        scanf("%f",&pren[i].precio);
        pren[i].cant_tot=0;
    }
}
void ordenar(prendas pren[P]){            //metodo burbuja mejorado
	int k = 1, i,cota = P-1;
    prendas aux;
	while(k != -1){
		k = -1;

		for(i = 0; i < cota; i++){
			if((strcmp(pren[i].nombre,pren[i+1].nombre)>0)){           //ascendente
				aux=pren[i];
				pren[i]= pren[i + 1];
				pren[i + 1]= aux;
				k = i;
			}
		}

		cota = k;
	}
}
void inicia2 (comercio com[C]){
int i;
    for (i=0;i<C;i++){
        printf ("\nIngrese el nombre del comercio %d\n",i+1);
        fflush(stdin);
        gets(com[i].nom);
        printf ("\nIngrese el cuil del comercio %d\n",i+1);
        scanf("%d",&com[i].CUIL);
        com[i].imp_tot=0;
    }
}
int menu()
{
	int d;
	printf("\nElija una opcion: \n");
    printf("1 - Cargar ventas \n");
    printf("2 - Mostrar por cada comercio CUIL, Nombre e importe total a pagar \n");
    printf("3 - Listado de cada producto, con nombre y cantidad de unidades vendidas \n");
    printf("4 - 5 productos que mas se vendieron \n");
    printf("0 - salir \n");
    scanf("%d",&d);
    return d;
}
int validar (){
int num;
    printf("Ingrese el codigo de comercio que se realizo la venta(60-94): 0 para terminar\n");
    scanf("%d",&num);
    while ((num<60) && (num>94)&& (num!=0)){
        printf("\nNumero incorrecto ingrese nuevamente\n");
    }
    return(num);
}
int busca(prendas pren[P],char nm[30]){
int inf,sup,medio;
inf=0;
sup=P-1;
medio=(inf+sup)/2;
    while ((inf<=sup)&& (strcmp(pren[medio].nombre,nm))!=0){
        if (strcmp(pren[medio].nombre,nm)>0)
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

void carga (int tabla[C][P],prendas pren[P]){
int cod,cant,b;
char nm[30];
        cod=validar();
        while (cod!=0){
            printf("Ingrese el nombre de la prenda a vender\n");
            fflush(stdin);
            gets(nm);
            b=busca(pren,nm);
            if (b!=-1){
                printf("Ingrese la cantidad de unidades a vender\n");
                scanf("%d",&cant);
                tabla[cod-60][b]+=cant;
            }
            else {printf("Nombre ingresado incorrecto\n");}
        cod=validar();
        }
}

void calc_imp(int tabla [C][P],comercio com[C],prendas pren[P]){
int i,j;
    for (i=0;i<C;i++){
        for (j=0;j<P;j++){
            com[i].imp_tot+=(tabla[i][j]*pren[j].precio);
        }
    }
}
void item_b (comercio com[C]){
int i;
    for (i=0;i<C;i++){
        printf ("\n Comercio %d - CUIL:%d - Nombre: %s - Importe total a pagar: %.2f\n",i+1,com[i].CUIL,com[i].nom,com[i].imp_tot);
    }
}
void cant_uni(int tabla[C][P],prendas pren[P]){
int i,j;
    for (i=0;i<C;i++){
        for (j=0;j<P;j++){
            pren[j].cant_tot+=tabla[i][j];
        }
    }

}
void orden(prendas pren[P]){            //metodo burbuja mejorado
	int k = 1, i,cota = P-1;
    prendas aux;
	while(k != -1){
		k = -1;

		for(i = 0; i < cota; i++){
			if(pren[i].cant_tot<pren[i+1].cant_tot){           //descendente
				aux=pren[i];
				pren[i]= pren[i + 1];
				pren[i + 1]= aux;
				k = i;
			}
		}

		cota = k;
	}
}

void item_c (prendas pren[P]){
int i;
    printf ("\n --Listado ordenado descendentemente por cantidad de unidades--\n ");
    for (i=0;i<P;i++){
        printf ("\n Prenda: %s - Cantidad de unidades vendidas: %d\n",pren[i].nombre,pren[i].cant_tot);
    }
}

int main()
{
int tabla[C][P];
prendas pren[P];
comercio com[C];
cerear(tabla);
inicia1(pren);
ordenar(pren);
inicia2(com);
int op;
	do
	{
		op=menu();
		switch(op)
		{
			case 0: break;
			case 1:{
				carga(tabla,pren);
				break;
                }
			break;
			case 2: {
			    calc_imp(tabla,com,pren);
                item_b(com);
				break;
			}
			case 3: {
			    cant_uni(tabla,pren);
			    orden(pren);
                item_c(pren);
			    break;
			}
			case 4: {
			 //   item_e();
			    break;
			}
		}
	}
	while(op!=0);
}
