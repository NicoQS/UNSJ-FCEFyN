// Declaración de índices
{string}Productos =...;   //{"amoniaco", "cloruro_amonico"};
{string}Componentes= ...; //{"nitrogeno", "hidrogeno", "oxigeno"};
// Declaración de datos

float demanda[Productos][Componentes] = ...;
float beneficio[Productos] = ...;
float stock[Componentes] = ...;
// Variables de decisión
dvar float+  produccion[Productos];
// Función objetivo
maximize
sum(p in Productos) beneficio[p] * produccion[p];
// Restricciones
subject to {
forall(c in Componentes)
sum(p in Productos) demanda[p][c] * produccion[p] <= stock[c];
// 1era iteracion de forall
//1era iteracion stock nitrogeno -->demanda[amoniaco][nitrogeno]*produccion[amoniaco]+ demanda[cloruro_amonico][nitrogeno]*produccion[cloruro_amonico]<=stock[nitrogeno]
//2era iteracion stock hidrogeno -->demanda[amoniaco][hidrogeno]*produccion[amoniaco] + demanda[cloruro_amonico][hidrogeno]*produccion[cloruro_amonico]<=stock[hidrogeno]
//3era iteracion stock oxigeno   -->demanda[amoniaco][oxigeno]*produccion[amoniaco] + demanda[cloruro_amonico][oxigeno]*produccion[cloruro_amonico]<=stock[oxigeno]




};

