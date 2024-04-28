package Biblioteca;

import java.util.*;

public class Biblioteca {
	private List<Libro> librosDisponibles;
	private List<Libro> librosPrestados;

	public Biblioteca(){
		this.librosDisponibles = new ArrayList<Libro>();
		this.librosPrestados = new ArrayList<Libro>();
	}

	public void agregarLibro(Libro L){
		this.librosDisponibles.add(L);
	}

	public void agregarLibroPrestado(Libro L){
		this.librosPrestados.add(L);
	}
	public Libro buscar(String titulo){
		int i = 0;
		Libro l = null;
		while (i<this.librosDisponibles.size() && l == null){
			if (this.librosDisponibles.get(i).getTitulo().equals(titulo)){
				l = this.librosDisponibles.get(i);
			}
			i++;
		}
		return l;
	}
	public Libro buscarLibroPorTitulo(String titulo){
		return this.librosDisponibles
		.stream()
		.filter(l -> l.getTitulo().equals(titulo))
		.findFirst()
		.orElse(null);
	}

	public Libro prestarLibro(String titulo) throws LibroNoDisponible{
		Libro l = this.buscar(titulo);
		if (l == null){
			throw new LibroNoDisponible("El libro no se encuentra disponible");
		}
		this.librosDisponibles.remove(l);
		this.librosPrestados.add(l);
		return l;
	}

	public void devolverLibro(Libro l){
		this.librosPrestados.remove(l);
		this.librosDisponibles.add(l);
	}

	public void mostrarLibrosDisponibles(){
		for (Libro l: this.librosDisponibles){
			System.out.println(l.toString());
		}
	}
	
	

	
	
	
	public static void main(String[] args){
		Biblioteca b = new Biblioteca();
		Libro l1 = new Libro("Libro 1", "Autor 1", 2000);
		Libro l2 = new Libro("Libro 2", "Autor 2", 2001);
		Libro l3 = new Libro("Libro 3", "Autor 3", 2002);
		Libro l4 = new Libro("Libro 4", "Autor 4", 2003);
		b.agregarLibro(l1);
		b.agregarLibro(l2);
		b.agregarLibro(l3);
		b.agregarLibro(l4);
		System.out.println(b.buscarLibroPorTitulo("Libro 1"));
		try {
			Libro p1 = b.prestarLibro("Libro 1");
			// b.prestarLibro("Libro 5");
			Libro p3 = b.prestarLibro("Libro 2");
			b.mostrarLibrosDisponibles();
			System.out.println("-------");
			b.devolverLibro(p1);
			b.devolverLibro(p3);
			b.mostrarLibrosDisponibles();
		} catch (LibroNoDisponible e){
			System.out.println("Error: " + e.getMessage());
		}
		
	}	
}
