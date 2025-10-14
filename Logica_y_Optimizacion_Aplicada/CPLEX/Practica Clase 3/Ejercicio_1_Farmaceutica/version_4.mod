{string} Productos = ...;
{string} Componentes = ...;

// Datos
float demanda[Productos][Componentes] = ...;
float beneficio[Productos] = ...;
float requerimiento[Componentes] = ...;

// Variables de decisión
dvar float+ produccion[Productos];

// Función objetivo
minimize
	sum(p in Productos) beneficio[p] * produccion[p];
	
// Restricciones
subject to {
	forall(c in Componentes)
		sum(p in Productos) demanda[p][c] * produccion[p] >= requerimiento[c];

};