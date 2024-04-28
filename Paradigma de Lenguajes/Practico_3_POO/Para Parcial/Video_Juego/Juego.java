package Video_Juego;

import java.util.*;

public class Juego {
	public static void main(String[] args){
		Musica m = new Musica("Cancion 1");
		EfectoSonido e = new EfectoSonido("Efecto 1");
		List<Reproducible> lista = Arrays.asList(m, e);

		for (Reproducible r : lista){
			r.reproducirSonido();
		}
	}
}
