#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "tipo.h"


void crear_empleados(){
empleado emp;
FILE *f;
	if ((f=fopen("EMPLEADOS.dat","wb"))==NULL)
	printf("Ocurrio error\n");
	printf("------------CARGA DE DATOS DE LOS EMPLEADOS------------\n");
	printf ("Ingrese el codigo de la empresa en que trabaja(De forma ordenada a partir de 1200): 0 para terminar\n");
	scanf("%d",&emp.cod);
	while(emp.cod!=0){
		printf("Ingrese el nombre del empleado\n");
		fflush(stdin);
		gets(emp.nom);
		printf("Ingrese el DNI del empleado\n");
		fflush(stdin);
		gets(emp.DNI);
		printf("Ingrese el sueldo basico\n");
		scanf("%f",&emp.sueldo);
		printf("Ingrese la antiguedad del empleado\n");
		scanf("%d",&emp.antig);
		fwrite(&emp,sizeof(empleado),1,f);
		printf ("Ingrese el codigo de la empresa en que trabaja(De forma ordenada): 0 para terminar\n");
		scanf("%d",&emp.cod);	
	}
	fclose(f);
}
