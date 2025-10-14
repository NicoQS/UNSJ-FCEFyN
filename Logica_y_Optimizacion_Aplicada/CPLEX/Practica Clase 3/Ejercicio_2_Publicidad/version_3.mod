{string} Programas = {"programaA", "programaB"};
{string} Tipos = {"variedad", "publicidad"};

// Datos
float demanda[Programas][Tipos] = [[20,1],[10,1]];
float beneficio[Programas] = [30000, 10000];
float requerimiento[Tipos] = [80, 6];

// Variables de decisión
dvar float+ producto[Programas];

// Función objetivo
maximize
	sum(p in Programas) beneficio[p] * producto[p];


// Restricciones
subject to {
	forall(c in Tipos)
		sum(p in Programas) demanda[p][c] * producto[p] == requerimiento[c];

};