#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "tipo.h"



static float calculo(float sueldo){
float c;
c=(sueldo*11/100)+(sueldo*3/100)+3.80;
return c;
}


void listado (){
FILE *f_empr,*f_emple;
empresa m;
empleado p;
float total_hab,total_desc,renum;
if ((f_empr=fopen("EMPRESAS.dat","rb"))==NULL)
	printf("Ocurrio un error al intentar abrir EMPRESAS.dat\n");
if ((f_emple=fopen("EMPLEADOS.dat","rb"))==NULL)
printf("Ocurrio error al intentar abrir EMPLEADOS.dat\n");

printf("-------------LISTADO ORDENADO DE EMPRESAS-------------\n");

	rewind(f_empr);
	fread(&m,sizeof(empresa),1,f_empr);
	while (!feof(f_empr)){
		printf("[Empresa: %s - Codigo: %d]\n\n",m.nombre,m.code);
		total_hab=0;
		total_desc=0;
		rewind(f_emple);
		fread(&p,sizeof(empleado),1,f_emple);
		printf("Nombre del empleado\tRenumeracion\n");
		while (!feof(f_emple)){
			if (m.code==p.cod){
				renum=p.sueldo-calculo(p.sueldo);
				total_hab+=renum;
				total_desc+=calculo(p.sueldo);
				printf("%s\t\t$ %.2f\n",p.nom,renum);
			}
			fread(&p,sizeof(empleado),1,f_emple);
		}
		printf ("\nTotal Pagado en concepto de haberes: %.2f\n",total_hab);
		printf ("Total Pagado en concepto de descuentos: %.2f\n",total_desc);
		printf("\n");
		fread(&m,sizeof(empresa),1,f_empr);
	}
	fclose(f_empr);
	fclose(f_emple);		
}