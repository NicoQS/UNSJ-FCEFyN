package Otros.Filtros;


public class FiltroPar implements Filtro{
	@Override
	public boolean cumpleCondicion(Integer num){
		return num % 2 == 0;
	}
}