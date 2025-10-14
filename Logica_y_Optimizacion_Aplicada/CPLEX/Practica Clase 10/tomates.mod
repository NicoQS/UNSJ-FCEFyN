// Modelo base para el problema del granjero
dvar float+ x1; // Acres de tomates
dvar float+ x2; // Acres de pimientos
dvar float+ x3; // Acres de espinacas

maximize 6*x1 + 12*x2 + 10*x3; // Maximizar beneficio

subject to {
  C_Tierra: x1 + x2 + x3 <= 600;        // Restricción de tierra
  C_DiasHombre: 5*x1 + 8*x2 + 13*x3 <= 4000; // Restricción días hombre
  C_Presupuesto: 12*x1 + 18*x2 + 14*x3 <= 6000; // Restricción presupuesto
}

execute {
  writeln("Solución óptima:");
  writeln("Acres tomates (x1): " + x1);
  writeln("Acres pimientos (x2): " + x2);
  writeln("Acres espinacas (x3): " + x3);
  writeln("Beneficio total: $" + (6*x1 + 12*x2 + 10*x3));
  
  writeln("\nPrecios sombra:");
  writeln("Tierra (C_Tierra): " + C_Tierra.dual);
  writeln("Días hombre (C_DiasHombre): " + C_DiasHombre.dual);
  writeln("Presupuesto (C_Presupuesto): " + C_Presupuesto.dual);
  
  writeln("\nHolguras:");
  writeln("Tierra (C_Tierra): " + C_Tierra.slack);
  writeln("Días hombre (C_DiasHombre): " + C_DiasHombre.slack);
  writeln("Presupuesto (C_Presupuesto): " + C_Presupuesto.slack);
  
  writeln("\nCostos reducidos:");
  writeln("Tomates (x1): " + x1.reducedCost);
  writeln("Pimientos (x2): " + x2.reducedCost);
  writeln("Espinacas (x3): " + x3.reducedCost);
}