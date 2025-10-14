using CP;

int cantTrabajadoresDisponibles = ...;
{string} TaskNames = ...;
int Duration [t in TaskNames] = ...;

tuple Precedence {
   string pre;
   string post;
};
{Precedence} Precedences = ...;

dvar interval tarea[t in TaskNames] size Duration[t];

// ==========================================================================
// 1. MODELO BASE CON ENTREGAS INCREMENTADAS
// ==========================================================================

// Modelo original con entregas incrementadas (de 6000 a 10000)
cumulFunction cantTrabajadoresEnElTiempo = sum(t in TaskNames) pulse(tarea[t],1);

cumulFunction flujoDeCajaIncrementado = 
  sum (p in 0..5) step(30*p, 10000) - sum( t in TaskNames) stepAtStart(tarea[t], 200*Duration[t]);
  // Incrementar entregas de 6000 a 10000 mejora la disponibilidad de efectivo
  // Resultado esperado: Reducción del makespan debido a menos restricciones de flujo de caja

// ==========================================================================
// 2. MODELO PARA ANALIZAR TRABAJADORES NECESARIOS PARA MAMPOSTERÍA EN PARALELO
// ==========================================================================

// Para determinar cuántos trabajadores se necesitan para mampostería en paralelo
// Necesitamos conocer qué tareas pueden ejecutarse simultáneamente con mampostería
cumulFunction trabajadoresParaParalelismo = sum(t in TaskNames) pulse(tarea[t],1);

// Si queremos que mampostería se ejecute en paralelo con otras tareas:
// - Identificar qué tareas pueden ser simultáneas según precedencias
// - Sumar trabajadores requeridos por esas tareas
// - Ejemplo: si mampostería + 2 tareas más pueden ser paralelas, necesitamos 3 trabajadores mínimo

// ==========================================================================
// 3. RESTRICCIÓN DE UN SOLO TRABAJADOR ENTRE TIEMPO 90-100
// ==========================================================================

// Función cumulative para restricción temporal específica
cumulFunction trabajadoresRestringidos = sum(t in TaskNames) pulse(tarea[t],1);

// Función auxiliar para el período 90-100
cumulFunction trabajadoresPeriodo90_100 = sum(t in TaskNames) 
  pulse(maxl(90, startOf(tarea[t])), minl(100, endOf(tarea[t])), 1);

// ==========================================================================
// 4. MODELO CON RECURSOS INFINITOS
// ==========================================================================

// Para recursos infinitos, eliminamos restricciones de trabajadores y dinero
// Solo quedan las restricciones de precedencia
// Resultado esperado: Makespan mínimo determinado únicamente por el camino crítico

// ==========================================================================
// 5. MODELO CON 2 OPERARIOS POR TAREA
// ==========================================================================

cumulFunction cantTrabajadores2Operarios = sum(t in TaskNames) pulse(tarea[t],2);
// Cada tarea ahora requiere 2 trabajadores en lugar de 1

cumulFunction flujoDeCaja2Operarios = 
  sum (p in 0..5) step(30*p, 6000) - sum( t in TaskNames) stepAtStart(tarea[t], 400*Duration[t]);
  // Duplicamos el costo diario de 200 a 400 pesos por día

// ==========================================================================
// FUNCIÓN OBJETIVO
// ==========================================================================
minimize endOf(tarea["moving"]);

// ==========================================================================
// RESTRICCIONES - SELECCIONAR SEGÚN EL ESCENARIO
// ==========================================================================

subject to {
   // Restricciones de precedencia (siempre activas)
   forall(p in Precedences)
      endBeforeStart(tarea[p.pre], tarea[p.post]);

   // ESCENARIO 1: Entregas incrementadas
   // cantTrabajadoresEnElTiempo <= cantTrabajadoresDisponibles;
   // flujoDeCajaIncrementado >= 0;

   // ESCENARIO 2: Análisis de paralelismo (ajustar cantTrabajadoresDisponibles según análisis)
   // trabajadoresParaParalelismo <= cantTrabajadoresDisponibles;
   // flujoDeCaja >= 0;

   // ESCENARIO 3: Un trabajador entre tiempo 90-100
   cantTrabajadoresEnElTiempo <= cantTrabajadoresDisponibles;
   flujoDeCaja >= 0;
   // Restricción adicional para período específico
   forall(t in 90..100) 
     trabajadoresRestringidos <= 1; // Solo 1 trabajador disponible en este período

   // ESCENARIO 4: Recursos infinitos (comentar todas las restricciones de recursos)
   // Solo precedencias activas

   // ESCENARIO 5: 2 operarios por tarea
   // cantTrabajadores2Operarios <= cantTrabajadoresDisponibles * 2; // Ajustar disponibilidad
   // flujoDeCaja2Operarios >= 0;
}

// ==========================================================================
// SCRIPTS DE ANÁLISIS Y DISPLAY
// ==========================================================================

execute display_analysis {
  writeln("=== ANÁLISIS DE SCHEDULING ===");
  writeln("Makespan final: ", endOf(tarea["moving"]));
  writeln("Número de segmentos de trabajadores: ", cantTrabajadoresEnElTiempo.getNumberOfSegments());
}

execute display_cantTrabajadoresEnElTiempo {
 writeln("=== USO DE TRABAJADORES EN EL TIEMPO ===");
 writeln("Number of Segments of cantTrabajadoresEnElTiempo = ",cantTrabajadoresEnElTiempo.getNumberOfSegments());
 for(var i=0;i<cantTrabajadoresEnElTiempo.getNumberOfSegments();i++) {
   write(cantTrabajadoresEnElTiempo.getSegmentStart(i)," -> ",cantTrabajadoresEnElTiempo.getSegmentEnd(i));
   writeln(" : ",cantTrabajadoresEnElTiempo.getSegmentValue(i)); 
 }   
}

execute display_cash_flow {
 writeln("=== FLUJO DE CAJA ===");
 writeln("Number of Segments of flujoDeCaja = ",flujoDeCaja.getNumberOfSegments());
 for(var i=0;i<flujoDeCaja.getNumberOfSegments();i++) {
   write(flujoDeCaja.getSegmentStart(i)," -> ",flujoDeCaja.getSegmentEnd(i));
   writeln(" : ",flujoDeCaja.getSegmentValue(i)); 
 }   
}

execute display_task_schedule {
 writeln("=== CRONOGRAMA DE TAREAS ===");
 for(var t in TaskNames) {
   writeln("Tarea: ", t, " | Inicio: ", startOf(tarea[t]), " | Fin: ", endOf(tarea[t]), " | Duración: ", Duration[t]);
 }
}

// ==========================================================================
// ANÁLISIS DE SENSIBILIDAD - COMENTARIOS PARA CADA ESCENARIO
// ==========================================================================

/*
RESPUESTAS A LAS PREGUNTAS:

1. INCREMENTO DE ENTREGAS:
   - Cambiar step(30*p, 6000) por step(30*p, MONTO_MAYOR)
   - Efecto: Menor restricción de flujo de caja → Posible reducción del makespan
   - Las tareas pueden iniciarse más temprano al tener más dinero disponible

2. TRABAJADORES PARA MAMPOSTERÍA EN PARALELO:
   - Analizar qué tareas pueden ejecutarse simultáneamente con mampostería
   - Si mampostería puede ser paralela con N tareas más, necesitamos N+1 trabajadores
   - Ejemplo: mampostería + pintura + techado = 3 trabajadores mínimo

3. UN OPERARIO ENTRE TIEMPO 90-100:
   - Agregar restricción: forall(t in 90..100) trabajadoresEnTiempo <= 1
   - Usar función cumulative específica para ese período
   - Impacto: Posible aumento del makespan si hay conflictos en ese período

4. RECURSOS INFINITOS:
   - Comentar todas las restricciones de trabajadores y dinero
   - Solo mantener restricciones de precedencia
   - Resultado: Makespan = longitud del camino crítico (mínimo teórico)

5. DOS OPERARIOS POR TAREA:
   - Cambiar pulse(tarea[t],1) por pulse(tarea[t],2)
   - Duplicar costos: stepAtStart(tarea[t], 400*Duration[t])
   - Ajustar disponibilidad de trabajadores proporcionalmente
   - Efecto: Mayor uso de recursos → Posible aumento del makespan
*/