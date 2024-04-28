package Otros.Persona;
/*
Crea una clase "Persona" con los siguientes atributos: nombre, edad y ciudad. Implementa los métodos getter y setter correspondientes. Luego, crea una lista de objetos de tipo "Persona" y realiza las siguientes operaciones:

Agrega personas a la lista.
Busca una persona en la lista por su nombre.
Calcula el promedio de edad de las personas en la lista.
Muestra el nombre de las personas que viven en una ciudad específica. 

 */

public class Persona {
	private String nombre;
	private int edad;
	private String ciudad;
	public Persona(String nombre, int edad, String ciudad){
		this.nombre = nombre;
		this.edad = edad;
		this.ciudad = ciudad;
	}

	public String getNombre(){
		return this.nombre;
	}
	public int getEdad(){
		return this.edad;
	}
	public String getCiudad(){
		return this.ciudad;
	}
	public void setNombre(String nombre){
		this.nombre = nombre;
	}
	public void setEdad(int edad){
		this.edad = edad;
	}
	public void setCiudad(String ciudad){
		this.ciudad = ciudad;
	}
}
