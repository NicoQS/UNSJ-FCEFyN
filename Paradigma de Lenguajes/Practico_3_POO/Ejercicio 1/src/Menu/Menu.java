package Menu;

import Gestor.*;
import java.util.InputMismatchException;
import java.util.Scanner;

/**
 *
 * @author lia-t-07
 */
public class Menu {

    private Gestor gestorViajeros;

    public Menu() {
        this.gestorViajeros = new Gestor();
    }

    private void muestra() {
        System.out.println("1. Cargar viajero");
        System.out.println("2. Mostrar viajero dado un numero");
        System.out.println("3. Cantidad de millas dado un DNI");
        System.out.println("4. Acumular Millas");
        System.out.println("5. Canjear millas");
        System.out.println("6. Mejor viajero");
        System.out.println("7. Salir");
    }

    public void opciones() {
        Scanner sn = new Scanner(System.in);
        boolean salir = false;
        int opcion; //Guardaremos la opcion del usuario

        while (!salir) {

            this.muestra();
            try {

                System.out.println("Escribe una de las opciones");
                opcion = sn.nextInt();

                switch (opcion) {
                    case 1:
                        System.out.println("Has seleccionado la opcion 1");
                        this.gestorViajeros.cargarViajero();
                        break;
                    case 2:
                        System.out.println("Has seleccionado la opcion 2");
												System.out.println("Ingrese el numero de viajero");
												int num = sn.nextInt();
												this.gestorViajeros.mostrarViajero(num);
                        break;
                    case 3:
                        System.out.println("Has seleccionado la opcion 3");
												System.out.println("Ingrese el DNI");
												String dni = sn.next();
												this.gestorViajeros.mostrarCtMillas(dni);
                        break;
                    case 4:
                        System.out.println("Has seleccionado la opcion 4");
												System.out.println("Ingrese el DNI del viajero");
												String dniV = sn.next();
												System.out.println("Ingrese la cantidad de millas a acumular");
												int millas = sn.nextInt();
												this.gestorViajeros.acumularMillas(dniV, millas);
                        break;
                    case 5:
                        salir = true;
                        break;
                    case 6:
                        salir = true;
                        break;
                    case 7:
                        salir = true;
                        break;
                    default:
                        System.out.println("Solo números entre 1 y 4");
                }
            } catch (InputMismatchException e) {
                System.out.println("Debes insertar un número");
                sn.next();
            }
            this.muestra();
        }
    }
}
