package Biblioteca;

public class Libro {
	
	private String titulo;
	private String autor;
	private Integer anioPublic;

	public Libro(String titulo, String autor, Integer anio){
		this.titulo = titulo;
		this.autor = autor;
		this.anioPublic = anio;
	}

	public String getTitulo(){
		return this.titulo;
	}
	
	public String getAutor(){
		return this.autor;
	}

	public Integer getAnio(){
		return this.anioPublic;
	}
	
	@Override
	public String toString(){
		return this.titulo + " - " + this.autor + " - " + this.anioPublic;
	}
}
