#include <stdio.h>
#include <string.h>
#define P 2
#define S 2
#define T 2

typedef struct{
char s;
char nombre[50];
float precio;
}seguros;


int menu()
{
	int d;
	printf("\nElija una opcion: \n");
    printf("1 - Cargar ventas \n");
    printf("2 - Ingrese un tipo de seguro para observar en que sector se vende mas y cuantos promotores tiene ese sector \n");
    printf("3 - A partir de un numero de sector se muestra el seguro mas vendido \n");
    printf("4 - Nombre e importe total para cada seguro \n");
    printf("0 - salir \n");
    scanf("%d",&d);
    return d;
}
void cerea (int arre[S][T]){
int i,j;
    for (i=0;i<S;i++){
        for (j=0;j<T;j++){
            arre[i][j]=0;
        }
    }

}
void inicia (seguros seg[S]){
int i;
    for (i=0;i<S;i++){
        printf ("Ingrese el caracter del tipo de seguro %d\n",i+1);
        scanf(" %c",&seg[i].s);
        printf ("Ingrese el nombre del tipo de seguro %d\n",i+1);
        fflush(stdin);
        gets(seg[i].nombre);
        printf ("Ingrese el precio del tipo de seguro %d\n",i+1);
        scanf("%f",&seg[i].precio);
    }
}
void inicia_2 (int cod_sec[P]){
int i;
    for (i=0;i<P;i++){
        printf ("Ingrese el codigo de sector del promotor %d\n",i+1);
        scanf("%d",&cod_sec[i]);
    }
}

int busqueda (int cod_sec[P],int code){
int i=0;
    while ((i<P)&&(cod_sec[i]!=code)){
        i++;
    }
    if (i<P){
        return i;
    }
    else return -1;
}
int busca (seguros seg[S],char tipo){
int i=0;
    while ((i<S)&&(seg[i].s!=tipo)){
        i++;
    }
    if (i<S){
        return i;
    }
    else return -1;
}
void carga (int arre[S][T],int cod_sec[P],seguros seg[S]){
int code,b,bt;
char tipo;
    printf ("Ingrese el numero de promotor(30-37)\n");
    scanf("%d",&code);
    while (code!=0){
        b=busqueda(cod_sec,code);
            if (b!=-1){
                printf ("Ingrese el tipo de seguro A-C\n");
                scanf(" %c",&tipo);
                bt=busca(seg,tipo);
                arre[bt][b]++;
            }
            else printf ("Numero de promotor erroneo, ingrese nuevamente\n");
    printf ("Ingrese el numero de promotor(30-37)\n");
    scanf("%d",&code); 
        }   
}
int mas_ven (int arre[S]){
int i,pos;
int max=-1;
    for (i=0;i<T;i++){
        if (arre[i]>max){
            max=arre[i];
            pos=i;
        }
    }
return pos;
}
void item_b_c(int arre[S][T],int cod_sec[P],seguros seg[S]){
char tipo;
int i,b,pos,mx,cont=0;
    printf ("\nIngrese un tipo de seguro para determinar que sector lo vende mas\n");
    scanf (" %c",&tipo);
    b=busca(seg,tipo);
    mx=mas_ven(arre[b]);
    printf ("\nEl tipo de seguro %c se vende mas en el sector %d\n",tipo,cod_sec[mx]);
    for (i=0;i<P;i++){
        if (cod_sec[mx]==cod_sec[i]){
            cont++;
        }
    }
    printf ("\nLa cantidad de promotores que tiene el sector %d es: %d\n",cod_sec[mx],cont);
}
int mas_seg (int arre[S][T],int sec){
int i,p=0;
int max=-1;
    for (i=0;i<S;i++){
        if(arre[i][sec]>max){
            max=arre[i][sec];
            p=i;
        }
    }
    return (p);
}

void item_d (int arre[S][T],seguros seg[S]){
int sec;
int pos;
    printf ("\nIngrese un numero de sector para determinar cual es el seguro que mas se consume\n");
    scanf("%d",&sec);
    pos=mas_seg(arre,sec);
    printf ("\nDado el numero de sector %d, el seguro mas vendido es el %c\n",sec,seg[pos].s);
}
int imp_total (int arre[S]){
int i;
int acum;
    for (i=0;i<T;i++){
        acum+=arre[i];
    }
    return acum;
}

void item_e (int arre[S][T],seguros seg[S]){
int i;
    for (i=0;i<S;i++){
        printf ("Para el seguro %c con el nombre %s, su importe total es %.2f\n",seg[i].s,seg[i].nombre,(imp_total(arre[i])*(seg[i].precio)));
    }
}
void muestra (int arre[S][T]){
int i,j;
    for (i=0;i<S;i++){
        for (j=0;j<T;j++){
            printf ("%d",arre[i][j]);
        }
        printf ("\n");
    }

}
int main()
{
seguros seg[S];
int cod_sec[P];
int arre[S][T];
int op;
cerea(arre);
inicia(seg);
inicia_2(cod_sec);
	do
	{
		op=menu();
		switch(op)
		{
			case 0: break;
			case 1:{
				carga(arre,cod_sec,seg);
				break;
                }
			break;
			case 2: {
                muestra(arre);
				item_b_c(arre,cod_sec,seg);
				break;
			}
			case 3: {
			    item_d(arre,seg);
			    break;
			}
			case 4: {
			   item_e(arre,seg);
			    break;
			}
		}
	}
	while(op!=0);
}