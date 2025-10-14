// DADO
using CP;
range r=1..3;
range r2=1..8;

//dvar int x in r2;

dvar int x in r2;
dvar int y[r] in r;

subject to {
	forall(i in r) {
		x != y[i];
	}
}

// ITEM A
using CP;
range r=1..3;
range r2=1..8;
range r3=1..1;  // Rango para convertir x en arreglo

dvar int x[r3] in r2;  // x ahora es un arreglo de una sola posición
dvar int y[r] in r;

subject to {
	forall(i in r) {
		x[1] != y[i];  // Accedemos al único elemento del arreglo x
	}
}

// ITEM B
using CP;
range r=1..3;
range r2=1..8;
range r3=1..1;  // Rango para convertir x en arreglo

dvar int x[r3] in r2;  // x ahora es un arreglo de una sola posición
dvar int y[r] in r;

subject to {
	forall(i in r) {
		x[1] != y[i];  // Accedemos al único elemento del arreglo x
	}
}

// Postprocessing para encontrar e imprimir todas las soluciones
main {
    thisOplModel.generate();
    cp.startNewSearch();
    var cont = 0;
    
    writeln("=== BÚSQUEDA DE TODAS LAS SOLUCIONES ===");
    writeln();
    
    while (cp.next()) {
        cont++;
        thisOplModel.postProcess();
        writeln("Solución " + cont + ": x[1] = " + x[1] + ", y = [" + 
                y[1] + ", " + y[2] + ", " + y[3] + "]");
    }
    
    cp.endSearch();
    writeln();
    writeln("=== RESUMEN ===");
    writeln("Total de soluciones encontradas: " + cont);
}

// ITEM C
using CP;
range r=1..3;
range r2=1..8;
range r3=1..1;

dvar int x[r3] in r2;
dvar int y[r] in r;

// Preprocessing: Definir rutina de búsqueda personalizada
execute {
    var f = cp.factory;
    
    // Fase 1: Para x - instanciar con el valor más pequeño
    var phaseX = f.searchPhase(x, 
                              f.selectSmallest(f.varIndex(x)),    // Seleccionar variable x
                              f.selectSmallest(f.value()));       // Seleccionar valor más pequeño
    
    // Fase 2: Para y - seleccionar variable con índice más pequeño y valor más pequeño
    var phaseY = f.searchPhase(y, 
                              f.selectSmallest(f.varIndex(y)),    // Variable con índice más pequeño (y[1], y[2], y[3])
                              f.selectSmallest(f.value()));       // Valor más pequeño del dominio
    
    // Establecer las fases de búsqueda: primero x, luego y
    cp.setSearchPhases(phaseX, phaseY);
    
    writeln("=== ESTRATEGIA DE BÚSQUEDA CONFIGURADA ===");
    writeln("1. Variable x: instanciar con valor más pequeño");
    writeln("2. Arreglo y: seleccionar variable con índice más pequeño, valor más pequeño");
    writeln("3. Orden de instanciación: x[1] -> y[1] -> y[2] -> y[3]");
    writeln();
}

subject to {
	forall(i in r) {
		x[1] != y[i];
	}
}

main {
    thisOplModel.generate();
    cp.startNewSearch();
    var cont = 0;
    
    writeln("=== BÚSQUEDA CON ESTRATEGIA PERSONALIZADA ===");
    writeln();
    
    while (cp.next()) {
        cont++;
        thisOplModel.postProcess();
        
        // Formato de salida similar al mostrado en la imagen
        write("Solution:" + cont + " -> ");
        write("x: [" + x[1] + "] ");
        write("y: [" + y[1] + " " + y[2] + " " + y[3] + "]");
        writeln();
    }
    
    cp.endSearch();
    writeln();
    writeln("=== RESUMEN ===");
    writeln("Total de soluciones encontradas: " + cont);
    writeln("Estrategia aplicada:");
    writeln("  - x instanciada con valores en orden ascendente");
    writeln("  - y instanciada por índice (y[1] primero, luego y[2], luego y[3])");
    writeln("  - Cada y[i] toma el valor más pequeño disponible");
}