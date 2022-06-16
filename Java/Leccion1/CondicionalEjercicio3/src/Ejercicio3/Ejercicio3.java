
package Ejercicio3;

import java.util.Scanner;

public class Ejercicio3 {
    public static void main(String[] args) {
        
        //Con if/ else
        System.out.println("Sentencia if/else");
        Scanner entrada = new Scanner(System.in);
        System.out.print("Digite un número entero entre 0 y 10: ");
        var calificacion = Integer.parseInt(entrada.nextLine());
        if (calificacion >= 9 && calificacion <= 10){
            System.out.println("A");
        }
        else if (calificacion >= 8 && calificacion < 9) {
            System.out.println("B");
        }
        else if (calificacion >= 7 && calificacion < 8) {
            System.out.println("C");
        }
        else if (calificacion >= 6 && calificacion < 7) {
            System.out.println("D");
        }
        else if (calificacion >= 0 && calificacion < 6) {
            System.out.println("F");
        }
        else {
            System.out.println("Fuera de rango");
        }
        
        //Con switch
        var notaSegunCalificacion = "Calificacion fuera de rango";
        System.out.println("\nSentencia switch");
        System.out.println("Digite un número entero entre 0 y 10: ");
        calificacion = Integer.parseInt(entrada.nextLine());
        switch(calificacion){
            case 10: case 9:
                notaSegunCalificacion = "A";
                break;
            case 8:
                notaSegunCalificacion = "B";
                break;
            case 7:
                notaSegunCalificacion = "C";
                break;
            case 6:
                notaSegunCalificacion = "D";
                break;
            case 5: case 4: case 3: case 2: case 1:
                notaSegunCalificacion = "F";
                break;   
        }
        System.out.println("Su calificación es: " + notaSegunCalificacion);
        
        
    }
    
}
