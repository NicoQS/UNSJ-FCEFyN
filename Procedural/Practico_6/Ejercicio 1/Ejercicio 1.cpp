#include <stdio.h>
#include <stdlib.h>

typedef struct{
char voc;
int ct;
}vocal;

int menu(){
int d;
    printf ("-MENU DE OPCIONES-\n");
    printf ("1: LECTURA PARA UN ARCHIVO .CPP\n");
    printf ("2: LECTURA PARA UN ARCHIVO .DAT\n");
    printf ("3: LECTURA PARA UN ARCHIVO .TXT\n");
    printf ("4: PARA SALIR\n");
    scanf("%d",&d);
    return d;
}
void carga(vocal vc[]){
int i;
    for (i=0;i<5;i++){
        printf ("Ingrese la vocal %d\n",i+1);
        scanf(" %c",&vc[i].voc);
        vc[i].ct=0;
    }
}

void calcula (FILE *f,vocal vc[]){
char c;
    while(feof(f)==0){
        c=fgetc(f);
        switch (c)
        {
        case 'a':{
            vc[0].ct++;
        }
        break;
        case 'e':{
            vc[1].ct++;
        }
        break;
        case 'i':{
            vc[2].ct++;
        }
        break;
        case 'o':{
            vc[3].ct++;
        }
        break;
        case 'u':{
            vc[4].ct++;
        }
        break;
        }
    }
}

int maximo (vocal vc[],int &p){
int i,mx=-1;
    for (i=0;i<5;i++){
        if (vc[i].ct>mx){
            mx=vc[i].ct;
            p=i;
        }
    }
    return mx;
}

int main(){
FILE *f;
vocal vc[5];
int op;
int max,p;
carga(vc);
    do{
        system("cls");
        op=menu();
        switch(op){
            case 1:{
            f=fopen("Ejer1.txt","r");
            if (f==NULL){
                printf ("Ocurrio un error al abrir el archivo\n");
            }
            calcula(f,vc);
            max=maximo(vc,p);
            printf ("Del archivo leido la vocal con mas frecuencia es la [%c] con una cantidad de %d caracteres\n",vc[p].voc,max);
            fclose(f);
            system("pause");
            break;
            }
            break;
            case 2:{
            f=fopen("Ejer1.txt","rb");
            if (f==NULL){
                printf ("Ocurrio un error al abrir el archivo\n");
            }
            calcula(f,vc);
            max=maximo(vc,p);
            printf ("Del archivo leido la vocal con mas frecuencia es la [%c] con una cantidad de %d caracteres\n",vc[p].voc,max);
            fclose(f);
            system("pause");
            break;
            }
            break;
            case 3:{
            f=fopen("Ejer1.txt","r");
            if (f==NULL){
                printf ("Ocurrio un error al abrir el archivo\n");
            }
            calcula(f,vc);
            max=maximo(vc,p);
            printf ("Del archivo leido la vocal con mas frecuencia es la [%c] con una cantidad de %d caracteres\n",vc[p].voc,max);
            fclose(f);
            system("pause");  
            break;
            }
            break;
        }

    }
    while(op!=4);


}