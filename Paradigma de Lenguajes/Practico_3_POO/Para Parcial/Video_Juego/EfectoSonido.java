package Video_Juego;

public class EfectoSonido implements Reproducible{
	private String efecto;

	public EfectoSonido(String efecto){
		this.efecto = efecto;
	}
	@Override
	public void reproducirSonido(){
		System.out.println("Reproduciendo el efecto de sonido: " + this.efecto);
	}
}
