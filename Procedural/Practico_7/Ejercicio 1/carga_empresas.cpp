#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "tipo.h"

void crear_empresas(){
empresa empre;
fpos_t x;
FILE *f;
	if ((f=fopen("EMPRESAS.dat","wb"))==NULL)
	printf("Ocurrio error\n");

	printf("-------------CARGA DE DATOS DE LAS EMPRESAS-------------\n");
	printf ("Ingrese el nombre de la empresa: FIN para terminar\n");
	fflush(stdin);
	gets(empre.nombre);
	while(stricmp(empre.nombre,"FIN")!=0){
		fseek(f,0,SEEK_END);
		fgetpos(f,&x);
		empre.code=(int)(x/sizeof(empresa))+1200;
		printf("Ingrese el CUIT de la empresa\n");
		fflush(stdin);
		gets(empre.CUIT);
		printf("Ingrese la direccion de la empresa\n");
		fflush(stdin);
		gets(empre.direc);
		fwrite(&empre,sizeof(empresa),1,f);
		printf ("Ingrese el nombre de la empresa: FIN para terminar\n");
		fflush(stdin);
		gets(empre.nombre);
	}
	fclose(f);
}
