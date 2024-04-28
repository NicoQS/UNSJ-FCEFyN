#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct{
    char *tip_mag;
    int ano,mes,dia,hora;
    float lat,log,prof,mag;
}terremoto;

char* leerString(FILE* archivo){
	char str[200];
 	fgets(str, 200, archivo);
	int len = strlen(str);

	if(str[len - 1] == '\n') str[len - 1] = '\0';

	char* string = (char*) malloc(sizeof(char) * len);
	strcpy(string, str); 

	return string;
}

float conversor (float MB, float MS){
    if ((MB>3.5)&&(MB<3.6)){
        return 0.85*MB+1.03;
    }
    else if((MS>3.0)&&(MS<6.1)){
        return 0.67*MS+2.07;
    }
    else if((MS>6.2)&&(MS<8.2)){
        return 0.99*MS+0.08;
    }
}

void guardar_terre(FILE *unif,terremoto *t,int &ID){
    fprintf(unif,"ID: %d\nAno: %d\nMes: %d\nDia: %d\nHora: %d\nLat: %f\nLong: %f\nProf: %f\nMagnitud: %f\nTipo de Magnitud: %s\n",ID++,t->ano,t->mes,t->dia,t->hora,t->lat,t->log,t->prof,t->mag,t->tip_mag);
}

void procesa1(FILE *unif,int &ID){
FILE *catalogo;
catalogo=fopen("catalogo1.txt","r");
terremoto *t;
t=(terremoto*)malloc(sizeof(terremoto));
    while (!feof(catalogo)){
        float magMB,magMS;
        char pa[30];
        leerString(catalogo);
        fscanf(catalogo,"Pais: %s\nAno: %d\nMes: %d\nDia: %d\nHora: %d\nLat: %f\nLong: %f\nProf: %f\nMagnitud MB: %f\nMagnitud MS: %f\n",&pa,&t->ano,&t->mes,&t->dia,&t->hora,&t->lat,&t->log,&t->prof,&magMB,&magMS);
        t->mag=conversor(magMB,magMS);
        t->tip_mag="mw";
        guardar_terre(unif,t,ID);
    }
    fclose(catalogo);
}

void procesa2(FILE *unif,int &ID){
FILE *catalogo;
catalogo=fopen("catalogo2.txt","r");
terremoto *t;
t=(terremoto*)malloc(sizeof(terremoto));
    while(!feof(catalogo)){
        fscanf(catalogo,"Ano: %d\nMes: %d\nDia: %d\nHora: %d\nLat: %f\nLong: %f\nProf: %f\nMagnitud: %f\nTipo de magnitud: %s\n",&t->ano,&t->mes,&t->dia,&t->hora,&t->lat,&t->log,&t->prof,&t->mag,&t->tip_mag);
        
        guardar_terre(unif,t,ID);
        }
        fclose (catalogo);
}

int main(){
FILE *unifc;
int ID=0;
unifc=fopen("catalogounificado.txt","w");
procesa1(unifc,ID);
procesa2(unifc,ID);
fclose(unifc);

}