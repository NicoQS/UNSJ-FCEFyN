// Declaración de índices
//{string}Productos =...;
tuple Tproducts {
  string name;
  };
// <comp1, comp2, comp3,...>
{Tproducts} Productos = ...;
 // Declaración de índices

{string}Componentes= ...;
// Declaración de datos

float demanda[Productos][Componentes] = ...;
float beneficio[Productos] = ...;
float stock[Componentes] = ...;
// Variables de decisión
dvar float+  produccion[Productos];
// Función objetivo
maximize
sum(p in Productos) beneficio[p] * produccion[p];
// Restricciones
subject to {
forall(c in Componentes)
sum(p in Productos) demanda[p][c] * produccion[p] <= stock[c];

};
 
 tuple TSolucion {
  float valor;
  };
 
 execute {
  for (var p in Productos) 
        writeln(p, ": ", produccion[p]);
	
}