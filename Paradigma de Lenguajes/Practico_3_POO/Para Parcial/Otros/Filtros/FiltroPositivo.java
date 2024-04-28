package Otros.Filtros;


public class FiltroPositivo implements Filtro{
	@Override
	public boolean cumpleCondicion(Integer num){
		return num > 0;
	}
}