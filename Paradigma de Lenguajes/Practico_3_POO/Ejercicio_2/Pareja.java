package Ejercicio_2;

import java.util.List;

public class Pareja implements IDeporte {

    private Deportista deportista1;
    private Deportista deportista2;

    @Override
    public boolean conformar(List<Deportista> integrantes) {
        if (integrantes.size() == CANTIDAD_MINIMA) {
					this.deportista1 = integrantes.get(0);
        	this.deportista2 = integrantes.get(1);
        	return true;
				}
				return false;
    }

    @Override
    public void mostrar() {
        System.out.println("Pareja: " + this.deportista1.getNombre() + " y " + this.deportista2.getNombre());
    }

    @Override
    public void numeroDeportista() {
        System.out.println("Numero de deportista: " + this.deportista1.getNumeroDeportista() + " y " + this.deportista2.getNumeroDeportista());
    }
}