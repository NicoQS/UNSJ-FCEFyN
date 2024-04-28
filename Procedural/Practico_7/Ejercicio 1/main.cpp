#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "tipo.h"


void muestra_a(){
empresa em;
FILE *f;
	if ((f=fopen("EMPRESAS.dat","rb"))==NULL)
	printf("Ocurrio error\n");
rewind(f);
	fread(&em,sizeof(empresa),1,f);
	while(!feof(f)){
		printf("Nombre: %s - Codigo: %d - CUIT: %s\n",em.nombre,em.code,em.CUIT);
		fread(&em,sizeof(empresa),1,f);
	}
	fclose(f);	
}
void muestra_b(){
empleado empl;
FILE *f;
	if ((f=fopen("EMPLEADOS.dat","rb"))==NULL)
	printf("Ocurrio error\n");	
rewind(f);
	fread(&empl,sizeof(empleado),1,f);
	while(!feof(f)){
		printf("Nombre: %s - Sueldo: %f - Empresa: %d\n",empl.nom,empl.sueldo,empl.cod);
		fread(&empl,sizeof(empleado),1,f);
	}
	fclose(f);
}


int main(){
int op;
	do {
		system("cls");
		printf ("Ingrese una opcion\n");
    printf ("1: Crear archivo EMPRESAS.dat\n");
    printf ("2: Crear archivo EMPLEADOS.dat\n");
    printf("3: Listado ordenado por empresa con la liquidacion de haberes de cada empleado\n");
    printf("4: Salir\n");
    scanf("%d",&op);
    switch(op){
    	case 1:{
    		crear_empresas();
			break;
		}
		break;
    	case 2:{
    	 crear_empleados();
			break;
		}
		break;
    	case 3:{
    		listado();
    		system("pause");
			break;
		}
		break;
    	case 5:{
    		muestra_a();
    		system("pause");
			break;
		}
		break;
    	case 6:{
    		muestra_b();
    		system("pause");
			break;
		}
		break;
    	
		}
	}
	while(op!=4);


}
/*
Lote de prueba empresas
JUMBO
45-678689-89
Calle Aberastain 925
WALMART
76-124568-87
Calle Alberdi 766
HIPER
23-350984-56
Calle Solano 234
---------------------
Lote de prueba empleados
1200
Perez, P
37.567.967
33567.61
2
1200
Quiroga, S
38.685.876
35567.13
1
1200
Perez, K
34.589.456
32567.23
3
1201
Castro, M
39.567.452
38567.43
4
1201
Pastran, F
40.876.467
36567.67
5
1202
Guerra, R
35.576.234
40567.45
1
1202
Torres, L
27.346.564
42567.56
3
1202
Acosta, E
25.123.678
43567.45
2

*/