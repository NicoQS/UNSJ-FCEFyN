dvar float+ avionA;
dvar float+ avionB;

// Función objetivo
maximize
  	30000 * avionA + avionB * 20000;

// Restricciones
subject to
{
	avionA >= avionB+1;
	avionA <= 120;	
	avionA + avionB >= 61;
	avionA + avionB <= 199;
};