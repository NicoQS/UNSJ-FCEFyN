#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define E 2
#define M 2
#define A 2

void cerea (int arre[E][M][A]){
int i,j,k;
    for (i=0;i<E;i++){
         for (j=0;j<M;j++){
            for (k=0;k<A;k++){
                arre[i][j][k]=0;
            }
         }
    }
}

int menu()
{
	int d;
	printf("\nElija una opcion: \n");
    printf("1 - Carga aleatoria de lluvias \n");
    printf("2 - Mostrar Estado, Mes y Anio que registro mas lluvias \n");
    printf("3 - Mostrar Estado, Mes y Anio que registro menos lluvias \n");
    printf("4 - Mostrar el total de lluvias para cada estado \n");
    printf("5 - Estado que registro mayor cantidad de lluvias en base al total  \n");
    printf("6 - Estado que registro menor cantidad de lluvias en base al total \n");
    printf("0 - salir \n");
    scanf("%d",&d);
    return d;
}

void carga (int arre[E][M][A]){
int i,j,k;
    srand(time(NULL));
    for (i=0;i<E;i++){
        for (j=0;j<M;j++){
            for (k=0;k<A;k++){
            arre[i][j][k]=rand()%12+1;
            }
        }
    }
}
void mostrar (int arre[E][M][A]){
int i,j,k;
    for (i=0;i<E;i++){
        printf ("--Lluvias en el Estado %d--\n",i+1);
         for (j=0;j<M;j++){
            for (k=0;k<A;k++){
                printf ("En el mes %d anio %d es: %d\n",j+1,k+1,arre[i][j][k]);
            }
         //   printf("\n");
         }
     printf("\n");
    }
}
/*
void item_a (int arre[E][M][A]){
int i,j;
    for (i=0;i<E;i++){
        printf ("--Lluvias en el Estado %d--\n",i+1);
        for(j=0;j<M;j++){
            printf ("Mes %d anio %d: %d\n",j+1,2,arre[i][j][2]);
        }
        printf("\n");
    }
}
*/
void item_a(int arre[E][M][A]){
    for (int i = 0; i < E; i++) //Estados
    {
        printf("Estado %d en el anio 2 \n",i+1);
        for (int j = 0; j < M; j++)//Meses
        {
            printf("Mes %d --> [%d]",j+1,arre[i][j][1]);
        printf("\n");
        }
    }
}
int item_b(int arre[E][M][A],int *ms,int *anio){
int i,j,k,ps;
int max=-1;
    for (i=0;i<E;i++){
        for (j=0;j<M;j++){
            for (k=0;k<A;k++){
                if (arre[i][j][k]>max){
                    max=arre[i][j][k];
                    ps=i;
                    *ms=j;
                    *anio=k;
                }
            }
        }
    }
    return (ps);
}
int item_c(int arre[E][M][A],int *msm,int *aniom){
int i,j,k,ps;
int min=9999;
    for (i=0;i<E;i++){
        for (j=0;j<M;j++){
            for (k=0;k<A;k++){
                if (arre[i][j][k]<min){
                    min=arre[i][j][k];
                    ps=i;
                    *msm=j;
                    *aniom=k;
                }
            }
        }
    }
    return (ps);
}
int calculo (int arre[E][M]){
int i,j,acum=0;
    for (i=0;i<M;i++){
        for (j=0;j<A;j++)
        {
            acum+=arre[i][j];
        }      
    }
    return acum;
}

void item_d (int arre[E][M][A]){
int i;
    for (i=0;i<E;i++){
        printf ("\nPara el estado %d el total de lluvias registrados es de: %d\n\n",i+1,calculo(arre[i]));
    }
}

int mayor_est (int arre[E][M][A],int *pos){
int acum,i,j,k;
int max=-1;
    for (i=0;i<E;i++){
        acum=0;
        for(j=0;j<M;j++){
            for(k=0;k<A;k++){
                acum+=arre[i][j][k];
            }
        }
        if (acum>max){
            max=acum;
            *pos=i;
        }
    }
    return max;
}
int manor_est (int arre[E][M][A],int *pos){
int acum,i,j,k;
int min=9999999;
    for (i=0;i<E;i++){
        acum=0;
        for(j=0;j<M;j++){
            for(k=0;k<A;k++){
                acum+=arre[i][j][k];
            }
        }
        if (acum<min){
            min=acum;
            *pos=i;
        }
    }
    return min;
}

int main (){
int arre[E][M][A];
int ms,anio,ubi,ubim;
int msm,aniom;
//cerea(arre);
int op;
    do
        {
		op=menu();
		switch(op)
		{
			case 0: break;
			case 1:{
				carga(arre);
                mostrar(arre);
                item_a(arre);
                system("pause");break;
			}
			break;
			case 2: {
                int pos=item_b(arre,&ms,&anio);
				printf ("\nEl estado %d en el mes %d en el anio %d registro mas lluvias\n\n",pos+1,ms+1,anio+1);
                system("pause");break;
			}
            break;
			case 3: {
				int men=item_c(arre,&msm,&aniom);
                printf ("\nEl estado %d en el mes %d  en el anio %d registro menos lluvias\n\n",men+1,msm+1,aniom+1);
                system("pause");break;
			}
            break;
			case 4: {
			item_d(arre);
            system("pause");break;
			}
            break;
			case 5: {
				printf ("\nEl estado que registro mayor cantidad de lluvias en base al total es el %d con: %d lluvias\n\n",ubi+1,mayor_est(arre,&ubi));
                system("pause");break;
			}
			case 6: {
				printf ("\nEl estado que registro menor cantidad de lluvias en base al total es el %d con: %d lluvias\n\n",ubim+1,manor_est(arre,&ubim));
                system("pause");break;
                }
                break;
            }
        }
	while(op!=0);
}