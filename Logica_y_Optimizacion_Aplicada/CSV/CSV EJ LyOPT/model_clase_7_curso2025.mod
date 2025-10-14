{string} Components = { "nitrogen", "hydrogen", "chlorine" };

tuple Tproducto {
  string name;
  };
{Tproducto} Productos2 = ...;

float Demand[Productos2][Components] = [ [1, 3, 0], [1, 4, 1] ];
float Profit[Productos2] = [30, 40];
float Stock[Components] = [50, 180, 40];

dvar float+ Production[Productos2];


maximize
  sum( p in Productos2 ) 
    Profit[p] * Production[p];
subject to {
  forall( c in Components )
    ct:
      sum( p in Productos2 ) 
        Demand[p][c] * Production[p] <= Stock[c];
}
