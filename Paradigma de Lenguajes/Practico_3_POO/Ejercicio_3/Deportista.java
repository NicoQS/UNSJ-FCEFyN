package Ejercicio_3;

public class Deportista {
	private static Integer count = 1;
	private String nombre;
	private String DNI;
	private Integer numeroJugador;

	public Deportista(String nom, String dni) {
		this.nombre = nom;
		this.DNI = dni;
		this.numeroJugador = Deportista.count;
		Deportista.count++;
	}

	public String getNombre() {
		return this.nombre;
	}

	public String getDni() {
		return this.DNI;
	}

	public Integer getNumeroDeportista() {
		return this.numeroJugador;
	}
}
