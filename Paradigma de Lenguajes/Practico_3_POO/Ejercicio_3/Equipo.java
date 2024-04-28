package Ejercicio_3;

import java.util.List;

public class Equipo implements IDeporte{

	private String nombre;
	private List<Deportista> jugadores;

	public Equipo(String nombre){
		this.nombre = nombre;
	}

	@Override
	public boolean conformar(List<Deportista> integrantes) {
			if (integrantes.size() >= CANTIDAD_MINIMA) {
				this.jugadores = integrantes;
				return true;
			}
			// Excepciones
			throw new RuntimeException("No se puede conformar un equipo con menos de " + CANTIDAD_MINIMA + " jugadores");

	}

	@Override
	public void mostrar() {
			System.out.println("Equipo: " + this.nombre);
			for (Deportista deportista : this.jugadores) {
					System.out.println(deportista.getNombre());
			}
	}

	@Override
	public void numeroDeportista() {
			System.out.println("Numeros de deportistas del equipo " + this.nombre + ":");
			for (Deportista deportista : this.jugadores) {
					System.out.println(deportista.getNumeroDeportista());
			}
	}
}
