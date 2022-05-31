
package Ejercicio3;

import java.util.Scanner;

public class Ejercicio3 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite el alto del rectángulo: ");
        var alto = Float.parseFloat(entrada.nextLine());
        System.out.println("Digite el ancho del ractángulo: ");
        var ancho = Float.parseFloat(entrada.nextLine());
        var area = alto * ancho;
        var perimetro = (alto + ancho) * 2;
        System.out.println("El área del rectángulo es: "+ area);
        System.out.println("El perímetro del rectángulo es: "+ perimetro);
        
    }
    
}
