#ifndef tipo
#define tipo

typedef char cadena[30];
typedef struct{
	cadena nom;
	int cod;
	cadena DNI;
	float sueldo;
	int antig;
}empleado;
typedef struct{
	cadena nombre;
	int code;
	cadena CUIT;
	cadena direc;
}empresa;
void crear_empresas();
void crear_empleados();
void listado ();
#endif
