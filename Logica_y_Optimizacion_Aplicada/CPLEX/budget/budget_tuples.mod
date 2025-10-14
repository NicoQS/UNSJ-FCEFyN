// budget_tuples.mod

// Parámetros de dimensión
int T              = ...;  
int NbMustTakeOne  = ...;
range Periods      = 1..T;

// --- Definición de tuplas -----------------------------------------

// Cada proyecto lleva su nombre, su coste de instalación por período y su reward por período
tuple Project {
  string name;
  float setupCost[Periods];
  float reward[Periods];
}

// Grupo “debe tomar uno”: asocia cada proyecto a un índice de grupo
tuple MustTake {
  int   group;
  string project;
}

// --- Datos --------------------------------------------------------

{Project}   Projects     =...;
{MustTake}  MustTakeOne  =...;

float Rate          = ...;
float MinBal[Periods] = ...;
float InitBal       = ...;

// --- Variables de decisión ---------------------------------------

dvar float      Bal[0..T];                          // saldo
dvar boolean    doProj[Projects][Periods];          // arranca proyecto p en t
dvar boolean    SelectedProj[Projects][Periods];    // p seleccionado hasta t

// --- Objetivo ----------------------------------------------------

dexpr float Objective =
  Bal[T] / pow(1+Rate, T) - Bal[0];

maximize Objective;

// --- Restricciones ----------------------------------------------

subject to {

  // 1) Saldo inicial
  Bal[0] == InitBal;

  // 2) Flujo de caja en cada período
  forall(t in Periods)
    Bal[t] == (1+Rate) * (
                  Bal[t-1]
                  // costes de nuevos proyectos
                - sum(p in Projects) p.setupCost[t] * doProj[p][t]
                  // reward de proyectos activos
                + sum(p in Projects) p.reward[t]   * SelectedProj[p][t]
              );

  // 3) Saldo mínimo por período
  forall(t in Periods)
    Bal[t] >= MinBal[t];

  // 4) Definir SelectedProj en función de doProj
  forall(p in Projects, t in Periods)
    SelectedProj[p][t] == sum(s in 1..t-1) doProj[p][s];

  // 5) Cada proyecto, a lo sumo una vez
  forall(p in Projects)
    SelectedProj[p][T] <= 1;

  // 6) “Must‐take‐one” por grupo
  forall(g in 1..NbMustTakeOne)
    sum(p in Projects, m in MustTakeOne:
          m.group == g && m.project == p.name
        )
      SelectedProj[p][T]
    == 1;
}
// Bloque de salida en consola
execute result {
  // Solo si hubo solución óptima
  if (cplex.getCplexStatus()==1) {
    writeln("=== RESULTADOS DE CAPITAL BUDGETING ===");
    writeln(" Estado CPLEX: ", cplex.getCplexStatus());
    writeln(" Valor objetivo (NPV): ", Objective.solutionValue);
    writeln();

    // 1) Proyectos iniciados
    writeln("Proyectos seleccionados:");
    for (var p in Projects) {
      var first = true;
      for (var t in Periods) {
        if (doProj[p][t].solutionValue > 0.5) {
          if (first) {
            write("  - ", p.name, " en periodo(s): ");
            first = false;
          }
          write(t, " ");
        }
      }
      if (!first) writeln("");
    }
    writeln();

    // 2) Saldos período a período
    writeln("Saldo al final de cada periodo:");
    for (var t = 0; t <= T; t++) {
      writeln("  Bal[", t, "] = ", Bal[t].solutionValue);
    }
    writeln("=======================================");
  }
  else {
    writeln("No se encontró solución óptima. Estado CPLEX: ", cplex.getCplexStatus());
  }
}