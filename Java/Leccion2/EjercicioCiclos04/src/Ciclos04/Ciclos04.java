/*
Ejercicio 4: Pedir números hasta que se teclee uno negativo y mostrar 
cuántos números se ha introducido.
Lo hacemos primero con clase Scanner y luego con clas JOptionPane
*/
package Ciclos04;

import java.util.Scanner;

public class Ciclos04 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero, conteo = 0;
        System.out.println("Digite un número: ");
        numero = Integer.parseInt(entrada.nextLine());
        while(numero >= 0){
            System.out.println("El número "+numero+" es POSITIVO");
            conteo++;
            System.out.println("Digite otro número: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("A ingresado "+conteo+" números que no son  negativos");
    }
}
