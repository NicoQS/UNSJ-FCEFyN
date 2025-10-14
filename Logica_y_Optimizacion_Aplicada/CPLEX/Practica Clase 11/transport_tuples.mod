// --------------------------------------------------------------------------
// Transporte en tuplas (compatible con Watson Studio Cloud)
// --------------------------------------------------------------------------

// ------------------------- Tipos de tupla -------------------------

tuple CapacityT {
  string Origin;
  string Destination;
  float  Capacity;
}

tuple SupplyT {
  string Product;
  string Origin;
  float  Supply;
}

tuple DemandT {
  string Product;
  string Destination;
  float  Demand;
}

tuple CostT {
  string Product;
  string Origin;
  string Destination;
  float  Cost;
}

// ------------------------- Datos externos -------------------------

// Cada CSV debe llamarse exactamente:
//   capacity.csv -> capacity
//   supply.csv   -> supply
//   demand.csv   -> demand
//   cost.csv     -> cost
{CapacityT} capacity = ...;
{SupplyT}   supply   = ...;
{DemandT}   demand   = ...;
{CostT}     cost     = ...;

// ------------------------ Variables ------------------------

dvar float+ Trans[cost];

// ----------------------- Funcion objetivo -----------------------

minimize
  sum(c in cost) c.Cost * Trans[c];

// --------------------- Restricciones ---------------------

subject to {

  // 1) Satisfaccion de oferta
  forall(s in supply)
    sum(c in cost
        : c.Product == s.Product
       && c.Origin  == s.Origin)
      Trans[c]
    == s.Supply;

  // 2) Satisfaccion de demanda
  forall(d in demand)
    sum(c in cost
        : c.Product     == d.Product
       && c.Destination == d.Destination)
      Trans[c]
    == d.Demand;

  // 3) No superar capacidad logistica
  forall(k in capacity)
    sum(c in cost
        : c.Origin      == k.Origin
       && c.Destination == k.Destination)
      Trans[c]
    <= k.Capacity;
}

// ----------------------- Salida -----------------------

tuple SolutionT {
  string Product;
  string Origin;
  string Destination;
  float  Transp;
}

{SolutionT} solution =
  { <c.Product, c.Origin, c.Destination, Trans[c]>
    | c in cost : Trans[c] > 0 };

execute {
  writeln("trans = ", Trans);
  writeln("solution = ", solution);
}
