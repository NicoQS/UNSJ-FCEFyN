package Otros;
public class NegativoExcep extends Exception{
	
	public NegativoExcep(){
		super("No se permiten numeros negativos");
	}
	public NegativoExcep(String mensaje){
		super(mensaje);
	}
	public NegativoExcep(String mensaje, Throwable causa){
		super(mensaje, causa);
	}
}
