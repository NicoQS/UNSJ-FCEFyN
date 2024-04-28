package Compras;
import java.util.*;

public class CarritoCompras {
	private List<Producto> carrito;

	public CarritoCompras(){
		this.carrito = new ArrayList<>();
	}

	public void agregarProducto(Producto p){
		this.carrito.add(p);
	}

	public double calcularTotal(){
		double total = 0;
		for (Producto p: this.carrito){
			total+=p.getPrecio();
		}
		return total;
	}

	public double calcularTotalStream(){
		return this.carrito
		.stream()
		.mapToDouble(Producto::getPrecio)
		.sum();
	}

	public void mostrarCarrito(){
		for (Producto p: this.carrito){
			System.out.println(p.toString());
		}
	}

	public static void main(String[] args){
		Producto producto1 = new Producto(1, "Smartphone", 500.0);
		Producto producto2 = new Producto(2, "Tablet", 300.0);
		Producto producto3 = new Producto(3, "Laptop", 1000.0);

		CarritoCompras carrito = new CarritoCompras();
		carrito.agregarProducto(producto1);
		carrito.agregarProducto(producto2);
		carrito.agregarProducto(producto3);

		carrito.mostrarCarrito();

		double total = carrito.calcularTotalStream();
		System.out.println("Total: $" + total);
}
}
