/*
Ejercicio 2: Leer 5 números, guardarlos en un arreglo y mostrarlos
en el orden inverso al introducido
*/
package test;

import java.util.Scanner;

public class SegundoEjercicio {
    public static void main(String[] args) {
        int numeros[] = new int [5];
        
        Scanner input = new Scanner(System.in);
        for (int i = 0; i < numeros.length; i++) {
            System.out.println("Digite un número: ");
            numeros[i] = Integer.parseInt(input.nextLine());
        }
        
        System.out.println("Números ingresados en el array numeros[] en orden"
                + " inverso");
        for (int i = numeros.length - 1 ; i >= 0 ; i--) {
            System.out.println(numeros[i]);
        }
    }
}
