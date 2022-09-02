/*
Ejercicio 1: Leer un número y mostrar su cuadradao, repetir
el proceso hasta que se introduzca un número negativo.
*/
package Ciclos01;

import java.util.Scanner; //importamos paquete java.util.Scanner que trae la clase Scanner

public class Ciclos01 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero, cuadrado;
        System.out.println("Digite un número: ");
        numero = Integer.parseInt(entrada.nextLine());
        while(numero >= 0){ //Mientras el número sea igual a cero o positivo
            cuadrado = (int)Math.pow(numero, 2); /*utilizamos la clase Math con el 
            método pow() para realizar el cuadrado, (1er parámetro número a elevar,
            2do parámetro potencia). Le indicamos al inicio el tipo de dato a retornar (int)*/
            System.out.println("El numero "+numero+" elevado al cuadrado es: "+cuadrado);
            System.out.println("Digite otro número: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("El programa a finalizado por el ingreso de un número negativo.");
    }
}
