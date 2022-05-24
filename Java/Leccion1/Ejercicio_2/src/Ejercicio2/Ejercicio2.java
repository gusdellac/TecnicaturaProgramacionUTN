
package Ejercicio2;

import java.util.Scanner;


public class Ejercicio2 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite las horas semanales trabajadas:\n");
        int horasSemanales = Integer.parseInt(entrada.nextLine());
        System.out.println("Digite el salario por hora: \n");
        float salarioHora = Float.parseFloat(entrada.nextLine());
        float salarioTotal = horasSemanales * salarioHora;
        System.out.println("\nEl salario del empleado es: US$ " + salarioTotal);
        
    }
    
}
