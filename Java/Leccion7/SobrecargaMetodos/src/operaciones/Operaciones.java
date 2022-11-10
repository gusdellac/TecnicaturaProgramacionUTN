
package operaciones;

public class Operaciones {
    
    //método sumar 1
    public static int sumar(int a, int b){
        System.out.println("Método para sumar enteros");
        return a + b;
    }
    
    //método sumar 2
    public static double sumar(double a, double b){ //sobrecarga de método
        //no puede cambiar el modificador de acceso public
        System.out.println("Método para sumar double");
        return a + b;
    }
}
