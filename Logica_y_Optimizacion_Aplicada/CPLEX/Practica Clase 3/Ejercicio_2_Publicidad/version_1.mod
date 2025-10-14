// Variables de decisión
dvar float+ programaA;
dvar float+ programaB;

// Función objetivo
maximize
  	30000 * programaA + programaB * 10000;

// Restricciones
subject to
{
	20*programaA + 10*programaB == 80;
	1*programaA + 1*programaB == 6;
};