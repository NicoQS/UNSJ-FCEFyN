{string} Componentes = ...;

tuple TProductos {
	string name;
}; 

{TProductos} Productos = ...;

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

tuple TSolucion {
	string name;
	float cantProd;
};

{ TSolucion } solucion; 

tuple TBMin {
	float beneficioMin;
};

{TBMin} Bmin;

execute {

	writeln ("f0: ", cplex.getObjValue());
	Bmin.addOnly(cplex.getObjValue());
	solucion.clear();
	for (var p in Productos){
		writeln(p, ": ", produccion[p]);
		solucion.addOnly(p, produccion[p]);
	}

};