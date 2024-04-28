package Otros.Persona;

import java.util.*;

public class Gestor {
	private List<Persona> personas;

	public Gestor(){
		this.personas = new ArrayList<>();
	}
	public Gestor(List<Persona> personas){
		this.personas = personas;
	}

	public void agregarPersona(Persona p){
		this.personas.add(p);
	}

	public Persona buscarPorNombre(String nombre){
		int i = 0;
		Persona encontrado = null;
		while (i<this.personas.size() && !this.personas.get(i).getNombre().equals(nombre)){
			i++;
		}
		if (i<this.personas.size()){
			encontrado = this.personas.get(i);
		}
		return encontrado;
	}
	public Persona buscarPorNombreStream(String nombre){
		return this.personas
		.stream()
		.filter(p -> p.getNombre().equals(nombre))
		.findFirst()
		.orElse(null);
	}
	public double promedioEdad(){
		double acum = 0;
		for (Persona p: this.personas){
			acum += p.getEdad();
		}
		return acum/this.personas.size();
	}
	public double promedioEdadStream(){
		return this.personas
		.stream()
		.mapToInt(Persona::getEdad)
		.average()
		.orElse(-1);
	}
	public void nombrePersonasCiudad (String ciudad){
		for (Persona p: this.personas){
			if (p.getCiudad().equals(ciudad)){
				System.out.println(p.getNombre());
			}
		}
	}
	
}
