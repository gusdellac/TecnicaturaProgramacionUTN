
package Ejercicio4;

import java.util.Scanner;


public class Ejercicio4 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Digite un número: ");
        var numero1 = Float.parseFloat(input.nextLine());
        System.out.print("Digite otro número: ");
        var numero2 = Float.parseFloat(input.nextLine());
        System.out.print("El número mayor es: ");
        System.out.println(numero1 > numero2? numero1 : (numero2 != numero1)? numero2 : "Los números son iguales");
           
    }
    
}
