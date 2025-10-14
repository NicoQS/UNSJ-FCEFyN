{string} Programas = ...;
{string} Tipos = ...;

// Datos
float demanda[Programas][Tipos] = ...;
float beneficio[Programas] = ...;
float requerimiento[Tipos] = ...;

// Variables de decisión
dvar float+ produccion[Programas];

// Función objetivo
maximize
	sum(p in Programas) beneficio[p] * produccion[p];
	
// Restricciones
subject to {
	forall(c in Tipos)
		sum(p in Programas) demanda[p][c] * produccion[p] == requerimiento[c];

};