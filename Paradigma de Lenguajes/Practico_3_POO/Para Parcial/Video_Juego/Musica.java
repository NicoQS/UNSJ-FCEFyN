package Video_Juego;

public class Musica implements Reproducible{
	private String cancion;

	public Musica(String cancion){
		this.cancion = cancion;
	}
	@Override
	public void reproducirSonido(){
		System.out.println("Reproduciendo la cancion: " + this.cancion);
	}
}
