{string} Aviones = {"avionA", "avionB"};
{string} Ganancias = {"gananciaA", "gananciaB"};

// Datos
float demanda[Aviones][Ganancias] = [[900,30000],[700,1]];
float beneficio[Aviones] = [30000, 20000];
float requerimiento[Ganancias] = [900, 700];

// Variables de decisión
dvar float+ producto[Aviones];

// Función objetivo
maximize
	sum(p in Aviones) beneficio[p] * producto[p];


// Restricciones
subject to {
	forall(c in Ganancias)
		sum(p in Aviones) demanda[p][c] * producto[p] == requerimiento[c];

};