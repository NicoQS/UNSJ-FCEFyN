package Ejercicio_4;

import java.util.*;

public class gestor {
	private List<viajero> viajeros = new ArrayList<viajero>();

	public gestor () {
	}
	public gestor (List<viajero> viajeros) {
		this.viajeros = viajeros;
	}

	public void agregarViajero (viajero v) {
		this.viajeros.add(v);
	}

	public void mostrar(){
		for (viajero v: this.viajeros){
			System.out.println(v.toString());
		}
	}

	public void mostrarOrdMillas(){
		List<viajero> viajerosOrdenados = this.viajeros.stream().sorted(Comparator.comparing(viajero::getMillas)).toList();

		for (viajero v: viajerosOrdenados){
			System.out.println(v.toString());
		}
	}

	public void nomConMasDe200Millas(){
		List<String> nombres = this.viajeros.stream().filter(v -> v.getMillas() > 200).map(viajero::getNyA).toList();
		for (String n: nombres){
			System.out.println(n);
		}
	}
	public void viajeroConMasMillas(){
		viajero v = this.viajeros.stream().max(Comparator.comparing(viajero::getMillas)).get();
		System.out.println(v.toString());
	}
}
