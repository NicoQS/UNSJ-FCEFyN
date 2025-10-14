// Declaración de índices
//{string}Productos =...;
tuple Tproducts {
  string name;
  };
{Tproducts} Productos = ...;

//{string}Componentes= ...;
tuple TComponents {
  string name;
}; 

{TComponents} Componentes =...;

//float demanda[Productos][Componentes] = ...;

tuple TDemada
{
  key string p; // producto;
  key string c; //componente;
   float d; //demanda;
};

{TDemada} Demanda=...;

//Demanda = { <amoniaco,nitrogeno,1>,
//			 <amoniaco,hidrogeno,3>,
//			 <amoniaco,oxigeno,0>,
//			 <cloruro_amonico,nitrogeno,1>,
//			 <cloruro_amonico,hidrogeno,4>,
//			 <cloruro_amonico,oxigeno,1>
//			 };
// indice del arreglo demand
tuple TProdComp
{
  key string p; // producto;
  key string c; //componente;
   
};
// Carga valores en el indice de arreglo demand
{TProdComp} ProdComp = {<p.name,c.name>  | p in Productos, c in Componentes} ;
// ProdComp -->{<amoniaco, nitrogeno>, <amoniaco, hidrogeno>,<amoniaco, oxigeno>,
//              <cloruro_amonico, nitrogeno>, <cloruro_amonico, hidrogeno>,<cloruro_amonico, oxigeno>
//              }
float demand [ProdComp] =[<D.p, D.c> : D.d | D in Demanda];
// demand -->          [1,                    3,                     0,                    1, 4, 1];
// indice ProdComp-->  <amoniaco, nitrogeno> <amoniaco, hidrogeno> <amoniaco, oxigeno> ...
//float array1[ind1][ind2][ind3][ind4][ind5]; // array1[1][1][1][1][1] --> 20;  array1[1][1][1][2][3] --> 30
tuple Tbeneficio  {
  key string producto;
  float value;
  };
{Tbeneficio} Beneficio = ...;
float beneficio[Productos] =[<B.producto> : B.value | B in Beneficio];  

tuple Tstock  {
  key string componente;
  float value;
  };
{Tstock} Stock = ...;
float stock[Componentes] =[<S.componente> : S.value |S in Stock];  

//float stock[Componentes] = ...;
// Variables de decisi�n
dvar float+  produccion[Productos];
// Funci�n objetivo
maximize
sum(p in Productos) beneficio[p] * produccion[p];
// Restricciones
//subject to {
//forall(c in Componentes)
//sum(p in Productos) demanda[p][c] * produccion[p] <= stock[c];
subject to {
forall(c in Componentes)
sum(p in Productos)  demand[<p.name,c.name>] * produccion[p] <= stock[c];

};




tuple TSolucion {
  string name;
  float cantProd;
 }
 tuple TmaxBeneficio{
   float maxBeneficio;
 }

{TmaxBeneficio} maxB;

{TSolucion} solucion;

execute {
  solucion.clear();
  for (var p in Productos) 
  {  writeln(p, ": ", produccion[p]);
	 solucion.addOnly(p, produccion[p]);
     }
  maxB.addOnly(cplex.getObjValue()); 
}
