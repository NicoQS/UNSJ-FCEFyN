// Indices
{string} Programas = {"programaA","programaB"};

// Variables de decisión
dvar float+ programa[Programas];

// Función objetivo
maximize
	30000 * programa["programaA"] + programa["programaB"] * 10000;

// Restricciones
subject to {
    20*programa ["programaA"] + 10 * programa ["programaB"] == 80;
    1*programa ["programaA"] + 1 * programa ["programaB"] == 6;
};