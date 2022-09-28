/*
Ejercicio 8: Pedir un número N, y mostrar todos los números del 1 al N.
*/
package Ciclos08;

import java.util.Scanner;

public class Ciclos08 {
    public static void main(String[] args) {
        int numero, contador = 1;
        Scanner input = new Scanner(System.in);
        System.out.print("Digite un número: ");
        numero = Integer.parseInt(input.nextLine());
        while(contador <= numero){
            System.out.print(contador+" ");
            contador++;
        }
    }
}
