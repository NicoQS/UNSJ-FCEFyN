package Gestor;

import java.util.Scanner;
import viajeroFrecuente.*;

/**
 *
 * @author lia-t-07
 */
public class Gestor {

    private viajeroFrecuente[] viajeros;
    private int cantidad;

    public Gestor() {
        Scanner sn = new Scanner(System.in);
        System.out.println("Escribe la cantidad de viajeros a registrar");
        int ct_viaj = sn.nextInt();
        this.viajeros = new viajeroFrecuente[ct_viaj];
        this.cantidad = 0;
    }

    public void crearViajero(viajeroFrecuente viajero) {
        this.viajeros[this.cantidad] = viajero;
        this.cantidad++;
    }

		// Item 2-a
    public void cargarViajero() {
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
        viajeroFrecuente viajero = new viajeroFrecuente(numV, dniV, nombreV, apellidoV, millasV);
        this.crearViajero(viajero);
    }

    public int buscarPorNumero(int numero) {
        for (int i = 0; i < this.cantidad; i++) {
            if (this.viajeros[i].getNum() == numero) {
                return i;
            }
        }
        return -1;
    }

		public int buscarPorDNI(String dni) {
				for (int i = 0; i < this.cantidad; i++) {
						if (this.viajeros[i].getDNI().equals(dni)) {
								return i;
						}
				}
				return -1;
		}

		// Item 2-b
    public void mostrarViajero(int numero) {
				int pos = this.buscarPorNumero(numero);
				if (pos == -1) {
					System.out.println("No se encontro el viajero");
					return;
				}
        System.out.println(this.viajeros[pos].toString());
    }

		// Item 2-c 3. Cantidad de millas dado un DNI
		public void mostrarCtMillas(String dni){
				int pos = this.buscarPorDNI(dni);
				if (pos == -1) {
					System.out.println("No se encontro el viajero");
					return;
				}
				System.out.println("El viajero tiene " + this.viajeros[pos].getMillas() + " millas");
		}

		// Item 2-d 4. Acumular Millas
		public void acumularMillas(String dni, int ctM){
			int pos = this.buscarPorDNI(dni);
			if (pos == -1){
				System.out.println("No se encontro el viajero");
				return;
			}
			System.out.println("Actualmente posee " + this.viajeros[pos].getMillas() + " millas\n ------");
			this.viajeros[pos].acumularMillas(ctM);
			System.out.println("Ahora el viajero tiene " + this.viajeros[pos].getMillas() + " millas nuevas");
		}
}
