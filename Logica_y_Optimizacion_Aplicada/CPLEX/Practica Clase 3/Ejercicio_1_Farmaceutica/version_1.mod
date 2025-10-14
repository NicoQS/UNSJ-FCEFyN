// Variables de decisión
dvar float+ productosA;
dvar float+ productosB;

// Función objetivo
minimize
  	0.6 * productosA + productosB * 0.2;

// Restricciones
subject to
{
	0.3*productosA + 0.05*productosB >= 25;
	0.01*productosA + 0.07*productosB >= 6;
	0.1*productosA + 0.1*productosB >= 30;
};