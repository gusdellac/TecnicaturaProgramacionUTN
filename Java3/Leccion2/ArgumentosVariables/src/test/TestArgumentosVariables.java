
package test;

public class TestArgumentosVariables {
    public static void main(String[] args) {
        imprimirNumeros(3, 4, 5);
        imprimirNumeros(5, 9, 10);
        variosParametros("Gustavo", 20,25,30);
    }
    
    private static void variosParametros(String nombre, int ...numeros){ //el parametro que recibira argumentos variables
        //se coloca siempre al final de los demas parametros
        System.out.println("Nombre: "+nombre);
        imprimirNumeros(numeros);
    }
    
    private static void imprimirNumeros(int ...numeros){ //pasamos como parametro argumentos variables
        for (int i = 0; i < numeros.length; i++) {
            System.out.println("Elementos: "+numeros[i]);
        }
    }
}
