// --------------------------------------------------------------------------
// Licensed Materials - Property of IBM
//
// 5725-A06 5725-A29 5724-Y48 5724-Y49 5724-Y54 5724-Y55
// Copyright IBM Corporation 1998, 2013. All Rights Reserved.
//
// Note to U.S. Government Users Restricted Rights:
// Use, duplication or disclosure restricted by GSA ADP Schedule
// Contract with IBM Corp.
// --------------------------------------------------------------------------

/* ------------------------------------------------------------

Problem Description
-------------------

This is a problem of building five houses in different locations. The
masonry, roofing, painting, etc. must be scheduled. Some tasks must
necessarily take place before others and these requirements are
expressed through precedence constraints.

There are two workers, and each task requires a specific worker.  The
time required for the workers to travel between houses must be taken
into account.  

Moreover, there are tardiness costs associated with some tasks as well
as a cost associated with the length of time it takes to build each
house.  The objective is to minimize these costs.

------------------------------------------------------------ */

using CP;

// Conjuntos de datos
range Houses = 0..NbHouses-1;
{string} WorkerNames = ...;  
{string} TaskNames   = ...;

// Parámetros
int    NbHouses      = ...;
int    Duration [t in TaskNames] = ...;
string Worker   [t in TaskNames] = ...;
int    ReleaseDate[h in Houses] = ...;
int    DueDate[h in Houses] = ...;
float  Weight[h in Houses] = ...;

tuple Precedence {
   string pre;
   string post;
};

{Precedence} Precedences = ...;

// Step 3: Crear las variables de intervalo para las casas
dvar interval houses[h in Houses] in ReleaseDate[h]..(maxint div 2)-1;

// Step 4: Crear las variables de intervalo para las tareas
dvar interval itvs[h in Houses][t in TaskNames] size Duration[t];

// Step 7: Crear los tiempos de transición
tuple triplet { int loc1; int loc2; int value; };
{triplet} transitionTimes = { <i,j, ftoi(abs(i-j))> | i in Houses, j in Houses };

// Step 8: Crear las variables de secuencia
dvar sequence workers[w in WorkerNames] in
                     all(h in Houses, t in TaskNames: Worker[t]==w) itvs[h][t] types
                     all(h in Houses, t in TaskNames: Worker[t]==w) h;

// Step 10: Agregar el objetivo
minimize sum(h in Houses)
         (Weight[h] * maxl(0, endOf(houses[h])-DueDate[h]) + lengthOf(houses[h]));

subject to {
   // Step 5: Agregar las restricciones de precedencia
   forall(h in Houses)
      forall(p in Precedences)
         endBeforeStart(itvs[h][p.pre], itvs[h][p.post]);

   // Step 6: Agregar las restricciones de duración de la casa
   forall(h in Houses)
      span(houses[h], all(t in TaskNames) itvs[h][t]);

   // Step 9: Agregar las restricciones de no solapamiento
   forall(w in WorkerNames)
      noOverlap(workers[w], transitionTimes);
}

execute {
   cp.param.FailLimit = 20000;
}