
package Ejercicio5;

import java.util.Scanner;

public class Ejercicio5 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Ingrese 3 calificaciones: ");
        float calificacion1 = Float.parseFloat(input.nextLine());
        float calificacion2 = Float.parseFloat(input.nextLine());
        float calificacion3 = Float.parseFloat(input.nextLine());
        
        float suma = calificacion1 + calificacion2 + calificacion3;
        System.out.println("La sumatoria de todas las calificaciones es: "+ suma);
        
    }
    
}
