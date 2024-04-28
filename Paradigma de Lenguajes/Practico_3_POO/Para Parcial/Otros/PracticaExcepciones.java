package Otros;

import java.util.Scanner;

public class PracticaExcepciones {
	

	public static void main(String[] args) throws NegativoExcep{
		Scanner in = new Scanner(System.in);
		System.out.println("Ingrese un entero positivo");
		int num = in.nextInt();
		if (num < 0){
			try{
				in.close();
				throw new NegativoExcep();
			}catch(NegativoExcep e){
				System.out.println("ERROR: " + e.getMessage());
			}
		}
	}

}

