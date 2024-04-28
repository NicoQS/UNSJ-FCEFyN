package viajeroFrecuente;

public class viajeroFrecuente {

    private int numero;
    private String dni;
    private String nombre;
    private String apellido;
    private Integer millas;

    public viajeroFrecuente(int numero, String dni, String nombre, String apellido, Integer millas) {
        this.numero = numero;
        this.dni = dni;
        this.nombre = nombre;
        this.apellido = apellido;
        this.millas = millas;
    }

    @Override
    public String toString() {
        return "Numero: " + this.numero + "\nDNI: " + this.dni + "\nNombre: " + this.nombre + "\nApellido: " + this.apellido + "\nMillas: " + this.millas;
    }

    public int getNum() {
        return this.numero;
    }

    public String getDNI() {
        return this.dni;
    }

    public Integer getMillas() {
        return this.millas;
    }

    public String getNyA() {
        return this.nombre + " " + this.apellido;
    }

    public Integer acumularMillas(int millasN) {
        this.millas += millasN;
        return this.millas;
    }

    public Integer canjearMillas(Integer millasC) throws Exception {
        if (millasC >= this.millas) {
            throw new Exception("Error en la operacion");
        }
        this.millas -= millasC;

        return this.millas;
    }
}
