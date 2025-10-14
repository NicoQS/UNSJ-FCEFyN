// Indices
{string} Productos = {"productoA","productoB"};


// Variables de decisión
dvar float+ producto[Productos];

// Función objetivo
minimize
	0.6 * producto["productoA"] + producto["productoB"] * 0.2;

// Restricciones
subject to {
    0.3*producto ["productoA"] + 0.05 * producto ["productoB"] >= 25;
    0.01*producto ["productoA"] + 0.07 * producto ["productoB"] >= 6;
    0.10*producto ["productoA"] + 0.1* producto ["productoB"] >= 30;
};