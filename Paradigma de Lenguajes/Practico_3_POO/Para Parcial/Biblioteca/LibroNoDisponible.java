package Biblioteca;

public class LibroNoDisponible extends Exception{
	public LibroNoDisponible(String mensaje){
		super(mensaje);
	}
}
