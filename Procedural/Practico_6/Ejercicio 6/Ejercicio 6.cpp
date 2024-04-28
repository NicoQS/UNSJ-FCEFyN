#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define N 3
typedef char cadena[30];
typedef struct{
cadena nom;
cadena empre;
cadena dni;
cadena CUIT;
float sueldo;
}empleado;

typedef struct{
cadena nom_emp;
int tot;
float total_pag;
}empresa;

int menu(){
int d;
    printf ("Ingrese una opcion\n");
    printf ("1:Crear archivo EMPLEADOS.dat\n");
    printf ("2: Listado ordenado por empresa con la informacion de cada empleado\n");
    printf("3: Generar archivo EMPRESAS.dat con su informacion\n");
    printf("4: Mostrar archivo de empresas\n");
    printf("5: Salir\n");
    scanf("%d",&d);
    return d;
}

void crear_emp(FILE *f){
empleado emp;
    if ((f=fopen("EMPLEADOS.dat","wb"))==NULL)
    printf ("Ocurrio un error\n");    
    printf ("Ingrese el nombre de la empresa en que trabaja, de forma ordenada[CARREFOUR-JUMBO-WALMART]: FIN PARA TERMINAR)\n");
    fflush(stdin);
    gets(emp.empre);
    while (stricmp(emp.empre,"FIN")!=0){
        fseek(f,0,SEEK_END);
        printf ("Ingrese el nombre del empleado\n");
        fflush(stdin);
        gets(emp.nom);
        printf ("Ingrese su DNI\n");
        fflush(stdin);
        gets(emp.dni);
        printf ("Ingrese el CUIT\n");
        fflush(stdin);
        gets(emp.CUIT);
        printf ("Ingrese el sueldo neto\n");
        scanf("%f",&emp.sueldo);
        fwrite(&emp,sizeof(empleado),1,f);
        printf ("Ingrese el nombre de la empresa en que trabaja, de forma ordenada[CARREFOUR-JUMBO-WALMART]: FIN PARA TERMINAR)\n");
        fflush(stdin);
        gets(emp.empre);
    }
    fclose(f);
}
void inicia (empresa empr[N]){
int i;
        strcpy(empr[0].nom_emp,"CARREFOUR");
        strcpy(empr[1].nom_emp,"JUMBO SA");
        strcpy(empr[2].nom_emp,"WALMART");
    for (i=0;i<N;i++){
        empr[i].tot=0;
        empr[i].total_pag=0;
    }
}
void calcula(FILE *f,empresa empr[N]){
int i;
empleado em;
if ((f=fopen("EMPLEADOS.dat","rb"))==NULL)
    printf ("Ocurrio un error\n");
    for (i=0;i<N;i++){
        rewind(f);
        fread(&em,sizeof(empleado),1,f);
        while (!feof(f)){
            if (stricmp(em.empre,empr[i].nom_emp)==0){
                empr[i].tot+=1;
                empr[i].total_pag+=em.sueldo;
            }
            fread(&em,sizeof(empleado),1,f);
        }
    }
    fclose(f);
}
/*
void listar(FILE *f){
empleado emp[8];
if ((f=fopen("EMPLEADOS.dat","rb"))==NULL)
    printf ("Ocurrio un error\n");
    fread(emp,sizeof(empleado),8,f);
fclose(f);
int i;
    for (i=0;i<8;i++){
        printf ("Nombre: %s\n",emp[i].nom);
        printf ("DNI: %s\n",emp[i].dni);
        printf ("Sueldo: %.2f\n",emp[i].sueldo);
        printf ("\n");
    }
}
*/
void listar_a (FILE *f,empresa empr[N]){
int i,j,nro_reg;
fpos_t x;
empleado em;
    if ((f=fopen("EMPLEADOS.dat","rb"))==NULL)
    printf ("Ocurrio un error\n");
//fseek(f,0,SEEK_END);
//fgetpos(f,&x);
//nro_reg=x/sizeof(empleado);
//printf ("Numero de empleados %d\n",nro_reg);
//em=(empleado*)malloc(sizeof(empleado)*nro_reg);
//fread(em,sizeof(empleado),nro_reg,f);
   printf("\n******************* LISTADO DE LIQUIDACION *********************\n\n"); 
    for (i=0;i<N;i++){
        j=1;
        printf ("[Lista de empleados de %s]\n\n",empr[i].nom_emp);
        printf ("\tDNI\t        Nombre\t        Sueldo\n");
         rewind(f);
         fread(&em,sizeof(empleado),1,f);
        while (!feof(f)){
            if (stricmp(em.empre,empr[i].nom_emp)==0){
                printf("%d\t%s\t%s\t%.2f\n",j++,em.dni,em.nom,em.sueldo);
            }
            fread(&em,sizeof(empleado),1,f);
        }
        printf("\n");
        printf ("\nEl total pagado por %s es $ %.2f\n\n",empr[i].nom_emp,empr[i].total_pag);
    }
    fclose(f);
}
void crear_empresa(empresa empr[N]){
FILE *ep;
    if ((ep=fopen("EMPRESAS.dat","wb"))==NULL)
    printf ("Ocurrio un error\n");
    fwrite(empr,sizeof(empresa),N,ep);
fclose(ep);
}
void listar_empresas(){
FILE *ep;
empresa emp;
if ((ep=fopen("EMPRESAS.dat","rb"))==NULL)
    printf ("Ocurrio un error\n");
rewind(ep);
    fread(&emp,sizeof(empresa),1,ep);
    while (!feof(ep)){
        printf ("Nombre: %s\n",emp.nom_emp);
        printf ("Total de empleados: %d\n",emp.tot);
        printf ("Total pagado: %.2f\n",emp.total_pag);
        printf("\n");
        fread(&emp,sizeof(empresa),1,ep);
    }
fclose(ep);
}

int main(){
FILE *f;
empresa empr[N];
int op;

    do{ 
        system("cls");
        op=menu();
        switch(op){
            case 1:{
                crear_emp(f);
            }
            break;
            case 2:{
                inicia(empr);
                calcula(f,empr);
                listar_a(f,empr);
               //  listar(f);
                system("pause");
            }
            break;
            case 3:{
                crear_empresa(empr);
            }
            break;
            case 4:{
                printf ("--LISTADO DE EMPRESAS--\n\n");
                listar_empresas();
                system("pause");
            }
            break;
        }
    }
    while(op!=5);
}
/*
Lote de prueba
CARREFOUR
Perez, P
37.567.967
87-37567967-6
33567.65
CARREFOUR
Quiroga, S
38.685.876
67-38685876-5
35567.65
CARREFOUR
Perez, K
34.589.456
57-34589456-8
32567.65
JUMBO SA
Castro, M
39.567.452
45-39567452-7
38567.65
JUMBO SA
Pastran, F
40.876.467
57-40876467-3
36567.65
WALMART
Guerra, R
35.576.234
67-35.576.234-9
40567.65
WALMART
Torres, L
27.346.564
45-27346564-9
42567.65
WALMART
Acosta, E
25.123.678
29-25123678-3
43567.65
*/