// Variables de decisión
dvar float+ amoniaco;
dvar float+ cloruro_amonico;

// Función objetivo
maximize 40*amoniaco+50*cloruro_amonico;
// Restricciones
subject to
{
amoniaco+cloruro_amonico <= 50; // stock nitrogeno
3*amoniaco+4*cloruro_amonico <= 180; // stock hidrogeno
0*amoniaco+cloruro_amonico <= 40; // stock oxigeno
};