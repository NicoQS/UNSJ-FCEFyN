// budget_tuples_with_csv.mod

// ------------------------------------------------------------
//  Importación de datos desde CSV:
//    • parameters.csv  → dataset "parameters"
//    • MinBal.csv      → dataset "MinBal"
//    • Projects.csv    → dataset "Projects"
//    • MustTakeOne.csv → dataset "MustTakeOne"
// ------------------------------------------------------------

// 1) Parámetros escalares
tuple ParamRow { 
  string Parameter; 
  float Value; 
}
{ParamRow} parameters = ...;

int T             = ftoi(sum(r in parameters: r.Parameter=="T") r.Value);
int NbMustTakeOne = ftoi(sum(r in parameters: r.Parameter=="NbMustTakeOne") r.Value);
float Rate        = sum(r in parameters: r.Parameter=="Rate") r.Value;
float InitBal     = sum(r in parameters: r.Parameter=="InitBal") r.Value;

// 2) Definir rango
range Periods = 1..T;

// 3) MinBal
tuple MinBalRow { 
  int Period; 
  int MinBal; 
}
{MinBalRow} MinBal = ...;

float MinBalArr[t in Periods] =
  sum(m in MinBal: m.Period==t) m.MinBal;

// 4) Proyectos (NOTA: el dataset debe llamarse "Projects", igual que el archivo)
tuple ProjectRow {
  string name;
  int setupCost_1; 
  int setupCost_2; 
  int setupCost_3;
  int reward_1;  
  int reward_2;  
  int reward_3;
}
{ProjectRow} Projects = ...;

// 5) Must-take-one
tuple MustTakeRow { 
  int group; 
  string project; 
}
{MustTakeRow} MustTakeOne = ...;

// 6) Variables de decisión
dvar float   Bal[0..T];
dvar boolean doProj[Projects][Periods];
dvar boolean SelectedProj[Projects][Periods];

// 7) Objetivo
maximize 
  Bal[T] / pow(1+Rate, T) - Bal[0];

// 8) Restricciones
subject to {

  // Saldo inicial
  Bal[0] == InitBal;

  // Flujo de caja
  forall(t in Periods)
    CtBalance: 
    Bal[t] ==
      (1+Rate) * (
        Bal[t-1]
        - sum(p in Projects) 
            (t==1 ? p.setupCost_1 : (t==2 ? p.setupCost_2 : p.setupCost_3)) * doProj[p][t]
        + sum(p in Projects) 
            (t==1 ? p.reward_1 : (t==2 ? p.reward_2 : p.reward_3)) * SelectedProj[p][t]
      );

  // Mínimo saldo
  forall(t in Periods)
    CtMinBal:
    Bal[t] >= MinBalArr[t];

  // SelectedProj en función de doProj
  forall(p in Projects, t in Periods)
    CtSelected:
    SelectedProj[p][t] == (t==1 ? 0 : sum(s in 1..t-1) doProj[p][s]);

  // Cada proyecto, a lo sumo una vez
  forall(p in Projects)
    CtOnce:
    sum(t in Periods) doProj[p][t] <= 1;

  // Must‐take‐one por grupo
  forall(g in 1..NbMustTakeOne)
    CtMustTake:
    sum(p in Projects, m in MustTakeOne:
          m.group==g && m.project==p.name)
      SelectedProj[p][T]
    == 1;
}

// 9) Salida de resultados
execute {
  if (cplex.getCplexStatus() == 1) {
    writeln("=== RESULTADOS DE CAPITAL BUDGETING ===");
    writeln("NPV = ", cplex.getObjValue());
    writeln();

    writeln("Proyectos seleccionados:");
    for(var p in Projects) {
      var selected = false;
      for(var t in Periods) {
        if(doProj[p][t].solutionValue > 0.5) {
          if(!selected) {
            write("  - ", p.name, " en periodo(s): ");
            selected = true;
          }
          write(t, " ");
        }
      }
      if(selected) writeln("");
    }
    writeln();

    writeln("Saldo al final de cada periodo:");
    for(var t = 0; t <= T; t++) {
      writeln("  Bal[", t, "] = ", Bal[t].solutionValue);
    }
  }
  else {
    writeln("No se encontró solución óptima. Estado CPLEX: ",
            cplex.getCplexStatus());
  }
}