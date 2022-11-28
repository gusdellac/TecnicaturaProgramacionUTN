
package ar.com.codesystem.ventas.test;

import ar.com.codesystem.ventas.*;

public class VentasTest {
    public static void main(String[] args) {
        Producto producto1 = new Producto("Pantalon", 9500.00);
        Producto producto2 = new Producto("Campera", 29900.00);
        Producto producto3 = new Producto("sueter", 4000);
        Producto producto4 = new Producto("Jean", 10000);
        Producto producto5 = new Producto("Remera", 3000);
        Producto producto6 = new Producto("Gorra", 2500);
        
        Orden orden1 = new Orden();
        orden1.agregarProducto(producto1);
        orden1.agregarProducto(producto2);
        orden1.calcularTotal();
        orden1.mostrarOrden();
        
        Orden orden2 = new Orden();
        orden2.agregarProducto(producto3);
        orden2.agregarProducto(producto4);
        orden2.calcularTotal();
        orden2.mostrarOrden();
        
        Orden orden3 = new Orden();
        orden3.agregarProducto(producto5);
        orden3.agregarProducto(producto6);
        orden3.calcularTotal();
        orden3.mostrarOrden();
        
        
        
    }
    
    
}
