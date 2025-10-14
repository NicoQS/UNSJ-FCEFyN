using CP;
range r=1..3;
range r2=1..8;
range r3=1..1;  // Para convertir x en arreglo

dvar int x[r3] in r2;  // x como arreglo
dvar int y[r] in r;

// ALGORITMO 1: Estrategia "Dominio Más Pequeño Primero"
execute ALGORITMO_1 {
    writeln("=== ALGORITMO 1: DOMINIO MÁS PEQUEÑO + VALOR MÁS PEQUEÑO ===");
    var f = cp.factory;
    
    // Para x: seleccionar por índice, valor más pequeño
    var phaseX = f.searchPhase(x, 
                              f.selectSmallest(f.varIndex(x)),
                              f.selectSmallest(f.value()));
    
    // Para y: variable con dominio más pequeño, valor más pequeño
    var phaseY = f.searchPhase(y, 
                              f.selectSmallest(f.domainSize()),  // Dominio más pequeño
                              f.selectSmallest(f.value()));      // Valor más pequeño
    
    cp.setSearchPhases(phaseX, phaseY);
    writeln("Estrategia: Dominio más pequeño + valor más pequeño");
}

subject to {
    forall(i in r) {
        x[1] != y[i];
    }
}

main {
    writeln("EJECUTANDO ALGORITMO 1...");
    writeln();
    
    thisOplModel.generate();
    
    // Medir tiempo de inicio
    var startTime = new Date();
    
    if (cp.solve()) {
        var endTime = new Date();
        var elapsedTime = endTime.getTime() - startTime.getTime();
        
        writeln("=== RESULTADOS ALGORITMO 1 ===");
        writeln("Solución encontrada:");
        writeln("x[1] = " + x[1]);
        writeln("y = [" + y[1] + ", " + y[2] + ", " + y[3] + "]");
        writeln("Tiempo transcurrido: " + elapsedTime + " ms");
        
        // Estadísticas del motor
        writeln("\n=== ESTADÍSTICAS DEL MOTOR ===");
        writeln("Número de branches: " + cp.info.numberOfBranches);
        writeln("Número de fails: " + cp.info.numberOfFails);
        writeln("Número de choice points: " + cp.info.numberOfChoicePoints);
        writeln("Tiempo de resolución: " + cp.info.solveTime + " s");
        writeln("Memoria utilizada: " + cp.info.memoryUsage + " MB");
    } else {
        writeln("No se encontró solución");
    }
}

using CP;
range r=1..3;
range r2=1..8;
range r3=1..1;

dvar int x[r3] in r2;
dvar int y[r] in r;

// ALGORITMO 2: Estrategia "Dominio Más Grande + Valor Más Grande"
execute ALGORITMO_2 {
    writeln("=== ALGORITMO 2: DOMINIO MÁS GRANDE + VALOR MÁS GRANDE ===");
    var f = cp.factory;
    
    // Para x: seleccionar por índice, valor más grande
    var phaseX = f.searchPhase(x, 
                              f.selectSmallest(f.varIndex(x)),
                              f.selectLargest(f.value()));       // Valor más grande
    
    // Para y: variable con dominio más grande, valor más grande
    var phaseY = f.searchPhase(y, 
                              f.selectLargest(f.domainSize()),   // Dominio más grande
                              f.selectLargest(f.value()));       // Valor más grande
    
    cp.setSearchPhases(phaseX, phaseY);
    writeln("Estrategia: Dominio más grande + valor más grande");
}

subject to {
    forall(i in r) {
        x[1] != y[i];
    }
}

main {
    writeln("EJECUTANDO ALGORITMO 2...");
    writeln();
    
    thisOplModel.generate();
    
    var startTime = new Date();
    
    if (cp.solve()) {
        var endTime = new Date();
        var elapsedTime = endTime.getTime() - startTime.getTime();
        
        writeln("=== RESULTADOS ALGORITMO 2 ===");
        writeln("Solución encontrada:");
        writeln("x[1] = " + x[1]);
        writeln("y = [" + y[1] + ", " + y[2] + ", " + y[3] + "]");
        writeln("Tiempo transcurrido: " + elapsedTime + " ms");
        
        // Estadísticas del motor
        writeln("\n=== ESTADÍSTICAS DEL MOTOR ===");
        writeln("Número de branches: " + cp.info.numberOfBranches);
        writeln("Número de fails: " + cp.info.numberOfFails);
        writeln("Número de choice points: " + cp.info.numberOfChoicePoints);
        writeln("Tiempo de resolución: " + cp.info.solveTime + " s");
        writeln("Memoria utilizada: " + cp.info.memoryUsage + " MB");
    } else {
        writeln("No se encontró solución");
    }
}

using CP;
range r=1..3;
range r2=1..8;
range r3=1..1;

dvar int x[r3] in r2;
dvar int y[r] in r;

// ALGORITMO 3: Estrategia "Aleatoria + Impacto"
execute ALGORITMO_3 {
    writeln("=== ALGORITMO 3: SELECCIÓN ALEATORIA + IMPACTO ===");
    var f = cp.factory;
    
    // Para x: seleccionar por índice, valor aleatorio
    var phaseX = f.searchPhase(x, 
                              f.selectSmallest(f.varIndex(x)),
                              f.selectRandomValue());            // Valor aleatorio
    
    // Para y: selección aleatoria de variable, valor por impacto
    var phaseY = f.searchPhase(y, 
                              f.selectRandomVar(),               // Variable aleatoria
                              f.selectSmallest(f.valueImpact())); // Valor con menor impacto
    
    cp.setSearchPhases(phaseX, phaseY);
    writeln("Estrategia: Variable aleatoria + valor por impacto");
}

subject to {
    forall(i in r) {
        x[1] != y[i];
    }
}

main {
    writeln("EJECUTANDO ALGORITMO 3...");
    writeln();
    
    thisOplModel.generate();
    
    var startTime = new Date();
    
    if (cp.solve()) {
        var endTime = new Date();
        var elapsedTime = endTime.getTime() - startTime.getTime();
        
        writeln("=== RESULTADOS ALGORITMO 3 ===");
        writeln("Solución encontrada:");
        writeln("x[1] = " + x[1]);
        writeln("y = [" + y[1] + ", " + y[2] + ", " + y[3] + "]");
        writeln("Tiempo transcurrido: " + elapsedTime + " ms");
        
        // Estadísticas del motor
        writeln("\n=== ESTADÍSTICAS DEL MOTOR ===");
        writeln("Número de branches: " + cp.info.numberOfBranches);
        writeln("Número de fails: " + cp.info.numberOfFails);
        writeln("Número de choice points: " + cp.info.numberOfChoicePoints);
        writeln("Tiempo de resolución: " + cp.info.solveTime + " s");
        writeln("Memoria utilizada: " + cp.info.memoryUsage + " MB");
    } else {
        writeln("No se encontró solución");
    }
}

/*
Se puede determinar cuál es más veloz usando las estadísticas que arroja el motor CP:

Métricas Clave del Motor:
- cp.info.numberOfBranches - Ramas exploradas
- cp.info.numberOfFails - Fallos/retrocesos  
- cp.info.numberOfChoicePoints - Puntos de decisión
- cp.info.solveTime - Tiempo de resolución del motor
- Tiempo total de ejecución (medido con new Date())

Criterio de Velocidad:
El algoritmo más veloz tiene:
- Menor tiempo de ejecución
- Menos branches (exploración más directa)
- Menos fails (menos backtracking)
- Menos choice points (decisiones más eficientes)

Interpretación Rápida:
- Branches bajos = Encuentra solución sin explorar mucho
- Fails bajos = Pocas decisiones incorrectas  
- Tiempo bajo = Ejecución más eficiente

Conclusión: Las estadísticas del motor CP proporcionan métricas objetivas y precisas para comparar la eficiencia de diferentes estrategias de búsqueda.

*/