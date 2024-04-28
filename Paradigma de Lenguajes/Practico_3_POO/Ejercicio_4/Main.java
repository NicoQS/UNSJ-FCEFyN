package Ejercicio_4;

import java.util.InputMismatchException;
import java.util.Scanner;

public class Main {
		public static void main(String[] args) {
				Scanner sn = new Scanner(System.in);
				gestor G = new gestor();
        boolean salir = false;
        int opcion; //Guardaremos la opcion del usuario

        while (!salir) {
						System.out.println("Opciones:");
						System.out.println("0. Salir");
						System.out.println("1. Registrar un nuevo viajero");
						System.out.println("2. Mostrar datos de viajero (ordenados por millas)");
						System.out.println("3. Mostrar nombres de viajeros con mas de 200 millas");
						System.out.println("4. Obtener viajero con mas millas");
            try {

                System.out.println("Escribe una de las opciones");
                opcion = sn.nextInt();

                switch (opcion) {
                    case 1:
                        System.out.println("Has seleccionado la opcion 1");
												Scanner in = new Scanner(System.in);
												System.out.println("Ingrese el numero de viajero");
												int numV = in.nextInt();
												System.out.println("Ingrese el DNI");
												String dniV = in.next();
												System.out.println("Ingrese el nombre");
												String nombreV = in.next();
												System.out.println("Ingrese el apellido");
												String apellidoV = in.next();
												System.out.println("Ingrese la cantidad de millas");
												Integer millasV = in.nextInt();
												viajero v = new viajero(numV, dniV, nombreV, apellidoV, millasV);
                        G.agregarViajero(v);
                        break;
                    case 2:
                        G.mostrarOrdMillas();
                        break;
                    case 3:
                        G.nomConMasDe200Millas();
                        break;
                    case 4:
                        G.viajeroConMasMillas();
                        break;
                    case 0:
												salir = true;
												break;
                    default:
                        System.out.println("Solo números entre 1 y 4");
                }
            } catch (InputMismatchException e) {
                System.out.println("Debes insertar un número");
                sn.next();
            }
						System.out.println("Opciones:");
						System.out.println("0. Salir");
						System.out.println("1. Registrar un nuevo viajero");
						System.out.println("2. Mostrar datos de viajero (ordenados por millas)");
						System.out.println("3. Mostrar nombres de viajeros con mas de 200 millas");
						System.out.println("4. Obtener viajero con mas millas");
        }
				sn.close();
		}
}
