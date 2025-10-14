/*********************************************
 * Modelo de selección óptima de proyectos
 * Variables de decisión enteras
 *********************************************/
 
dvar int+ x1; // Proyecto P1
dvar int+ x2; // Proyecto P2  
dvar int+ x3; // Proyecto P3
dvar int+ x4; // Proyecto P4
dvar int+ x5; // Proyecto P5

maximize
    200000 * x1 + 400000 * x2 + 200000 * x3 + 150000 * x4 + 300000 * x5;
        
subject to
{
  // Restricción de presupuesto Año 1
  50000 * x1 + 40000 * x2 + 30000 * x3 + 70000 * x4 + 80000 * x5 <= 250000;
  
  // Restricción de presupuesto Año 2
  10000 * x1 + 70000 * x2 + 90000 * x3 + 40000 * x4 + 60000 * x5 <= 250000;
  
  // Restricción de presupuesto Año 3
  80000 * x1 + 100000 * x2 + 20000 * x3 + 10000 * x4 + 100000 * x5 <= 250000;
};

execute salida {
  if (cplex.getCplexStatus()>1){
    writeln("\t\tSolucion 1");
    writeln("Proyecto\tRecomienda Invertir");
    writeln("P1\t\t" + (x1 > 0 ? "Si" : "No"));
    writeln("P2\t\t" + (x2 > 0 ? "Si" : "No"));
    writeln("P3\t\t" + (x3 > 0 ? "Si" : "No"));
    writeln("P4\t\t" + (x4 > 0 ? "Si" : "No"));
    writeln("P5\t\t" + (x5 > 0 ? "Si" : "No"));
  }
}