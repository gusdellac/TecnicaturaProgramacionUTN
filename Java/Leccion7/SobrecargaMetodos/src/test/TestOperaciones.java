
package test;

import operaciones.Operaciones;

public class TestOperaciones {
    public static void main(String[] args) {
        
        //llama al método para sumar int
        var resultado = Operaciones.sumar(7, 9);
        System.out.println("resultado = " + resultado);
        
        //llama al método para sumar double
        var resultado2 = Operaciones.sumar(2.5, 5.5);
        System.out.println("resultado2 = " + resultado2);
        
        //llama al método para sumar double
        //al colocar un dato de tipo long, buscó el método con un tipo de dato
        //compatible a long / long (64 bits) double (64 bits) int (32 bits)
        var resultado3 = Operaciones.sumar(8, 6L);
        System.out.println("resultado3 = " + resultado3);
    }
}
