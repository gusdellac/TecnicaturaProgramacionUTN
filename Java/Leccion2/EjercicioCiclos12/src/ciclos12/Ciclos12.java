/*
 Ejercicio 12: Pedir un número y calcular su factorial.
 Hacerlo con Scanner
 */
package ciclos12;

import java.util.Scanner;

public class Ciclos12 {
    public static void main(String[] args) {
        int numero, factorial = 1;
        Scanner input = new Scanner(System.in);
        do{
            System.out.println("Digite un número: ");
            numero = Integer.parseInt(input.nextLine());
            if(numero < 0){
                System.out.println("No se puede calcular el factorial de "
                        + "un número negativo.");
            }    
        }while(numero < 0);
       
        for(int i = 1; i <= numero; i++){
            factorial *= i;
        }
        System.out.println("El factorial de "+numero+" es: "+factorial);
        
    }    
}
