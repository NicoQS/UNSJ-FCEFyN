{string} Productos = {"productoA", "productoB"};
{string} Componentes = {"proteinas", "grasas", "azucares"};

// Datos
float demanda[Productos][Componentes] = [[0.3,0.01,0.1],[0.05,0.07,0.1]];
float beneficio[Productos] = [0.6, 0.2];
float requerimiento[Componentes] = [25,6,30];

// Variables de decisión
dvar float+ producto[Productos];

// Función objetivo
minimize
	sum(p in Productos) beneficio[p] * producto[p];


// Restricciones
subject to {
	forall(c in Componentes)
		sum(p in Productos) demanda[p][c] * producto[p] >= requerimiento[c];

};