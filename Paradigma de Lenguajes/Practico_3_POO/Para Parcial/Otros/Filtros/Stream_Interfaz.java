package Otros.Filtros;

import java.util.*;


public class Stream_Interfaz {
	

	public static void main(String[] args){
		List<Integer> numeros = Arrays.asList(1,2,3,4,5,6);
		FiltroPositivo fp = new FiltroPositivo();
		FiltroPar fpar = new FiltroPar();
		List<Integer> filtrados = numeros.stream().filter(n -> fp.cumpleCondicion(n) && fpar.cumpleCondicion(n)).toList();
		System.out.println(filtrados);
	}

}



