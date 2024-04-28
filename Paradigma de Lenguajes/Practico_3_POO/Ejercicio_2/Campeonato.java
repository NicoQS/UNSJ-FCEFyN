package Ejercicio_2;
import java.io.BufferedReader;
import java.io.FileReader;
//import java.io.IOException;
//import java.util.ArrayList;
//import java.util.List;
import java.util.*;
import java.io.*;

public class Campeonato {

	public static final String SEPARADOR = ",";

	public static List<Deportista> leerArchivo(String nombreArchivo) throws IOException {
		BufferedReader bufferLectura = null;
		List<Deportista> datos = new ArrayList<>();
		try {
			bufferLectura = new BufferedReader(new FileReader(nombreArchivo));
			String linea;
			while ((linea = bufferLectura.readLine()) != null) {
				// Sepapar la linea leída con el separador definido previamente
				String[] campos = linea.split(SEPARADOR);
				Deportista d = new Deportista(campos[0], campos[1]);
				datos.add(d);
			}
		} catch (IOException e) {
			System.out.println(e.getMessage());
		} finally {
			// Cierro el buffer de lectura
			if (bufferLectura != null) {
				bufferLectura.close();
			}
		}
		return datos;
	}

	public static List<IDeporte> creaEquipos(List<Deportista> datos, int cantidadJugadores) {
		List<IDeporte> equipos = new ArrayList<>();
		int i = 0;
		int j = 0;
		while (i < datos.size()){
			Equipo eq = new Equipo("Equipo " + (j+1));
			eq.conformar(datos.subList(i, i+cantidadJugadores));
			equipos.add(eq);
			i += cantidadJugadores;
			j++;
		}
		return equipos;
	}

	/**
	 * Crea los equipos con los datos pasados como parámetro
	 * 
	 * @param datos es una lista con todos los deportitas inscriptos
	 * @return una lista de Parejas formadas
	 */
	public static List<IDeporte> creaParejas(List<Deportista> datos) {
		List<IDeporte> parejas = new ArrayList<>();
		int i = 0;
		while (i < datos.size()){
			Pareja p = new Pareja();
			p.conformar(datos.subList(i, i+2));
			parejas.add(p);
			i += 2;
		}
		return parejas;
	}

	/**
	 * Numera cada integrante del equipo o de la pareja
	 * 
	 * @param datos
	 */
	public static void numerar(List<IDeporte> datos) {
		for (IDeporte iDeporte : datos) {
			iDeporte.numeroDeportista();
		}
	}

	/**
	 * Muestra los datos de cada equipo o de cada pareja
	 * 
	 * @param datos
	 */
	public static void mostrar(List<IDeporte> datos) {
		for (IDeporte iDeporte : datos) {
			iDeporte.mostrar();
		}
	}

	public static void main(String[] args) throws IOException {
		int cantidadJugadoresFutbol = 5;

		List<Deportista> datosFutbol = Campeonato.leerArchivo("C:\\Users\\Nicolas\\Documents\\FACULTAD\\A\u00D1O \u00B03\\1\u00B0 Semestre\\Paradigma de Lenguajes\\Practica\\Practica 3\\Ejercicio_2\\Datos\\inscriptosFutbol.csv");
		List<Deportista> datosPinPon = Campeonato.leerArchivo("C:\\Users\\Nicolas\\Documents\\FACULTAD\\A\u00D1O \u00B03\\1\u00B0 Semestre\\Paradigma de Lenguajes\\Practica\\Practica 3\\Ejercicio_2\\Datos\\inscriptosPinPon.csv");

		List<IDeporte> equiposFutbol = Campeonato.creaEquipos(datosFutbol, cantidadJugadoresFutbol);
		List<IDeporte> parejasPinPon = Campeonato.creaParejas(datosPinPon);

		numerar(equiposFutbol);
		numerar(parejasPinPon);
		System.out.println("----------------------\n");
		mostrar(equiposFutbol);
		mostrar(parejasPinPon);
	}

}