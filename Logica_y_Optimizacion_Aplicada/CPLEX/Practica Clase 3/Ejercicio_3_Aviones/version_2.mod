// Indices
{string} Aviones = {"avionA","avionB"};

// Variables de decisión
dvar float+ avion[Aviones];

// Función objetivo
maximize
	30000 * avion["avionA"] + avion["avionB"] * 20000;

// Restricciones
subject to {
    avion ["avionA"] >= avion ["avionB"]+1;
	avion ["avionA"] <= 120;	
	avion ["avionA"] + avion ["avionB"] >= 61;
	avion ["avionA"] + avion ["avionB"] <= 199;
};