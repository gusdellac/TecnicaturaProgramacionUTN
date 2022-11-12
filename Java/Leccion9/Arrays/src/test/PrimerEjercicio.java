/*
Ejercicio1: Leer 5 números, guardarlos en un arreglo y mostrarlos en el
mismo orden introducidos
*/
package test;

import java.util.Scanner;

public class PrimerEjercicio {
    public static void main(String[] args) {
        int numeros[] = new int [5];
        
        Scanner input = new Scanner(System.in);
        for (int i = 0; i < numeros.length; i++) {
            System.out.println("Digite un número: ");
            numeros[i] = Integer.parseInt(input.nextLine());
        }
        
        System.out.println("Números ingresados en el array numeros[]");
        for(int numero: numeros){
            System.out.println(numero);
        }
        
        
        
    }
}
