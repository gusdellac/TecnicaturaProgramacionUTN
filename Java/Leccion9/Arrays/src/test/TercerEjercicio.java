/*
Ejercicio 3: Leer 5 números por teclado, almacenarlos en un arreglo
y a continuación realizar la media de los números positivos, la
media de los negativos y contar el número de ceros
*/
package test;

import java.util.Scanner;

public class TercerEjercicio {
    public static void main(String[] args) {
        int numeros[] = new int [5];
        int sumaNumerosPositivos = 0, cantidadNumerosPositivos = 0;
        int sumaNumerosNegativos = 0, cantidadNumerosNegativos = 0;
        int cantidadCeros = 0;
        double mediaPositivos;
        double mediaNegativos;
        Scanner input = new Scanner(System.in);
        for (int i = 0; i < numeros.length; i++) {
            System.out.println("Digite un número: ");
            numeros[i] = Integer.parseInt(input.nextLine());
        }
        
        for(int numero: numeros){
            if (numero > 0){
                sumaNumerosPositivos += numero;
                cantidadNumerosPositivos++;
            } else if (numero < 0){
                sumaNumerosNegativos += numero;
                cantidadNumerosNegativos++;
            } else {
                cantidadCeros++;
            }
            
        }
        
        if (cantidadNumerosPositivos == 0){
            System.out.println("No se ingresaron numeros positivos.");
        } else {
            mediaPositivos = (double)sumaNumerosPositivos/
                    (double) cantidadNumerosPositivos;
            System.out.println("Media de números positivos ingresados: "+
                    mediaPositivos);
        }
        
        if(cantidadNumerosNegativos == 0){
            System.out.println("No se ingresaron números negativos.");
        }else{
            mediaNegativos = (double)sumaNumerosNegativos/
                    (double) cantidadNumerosNegativos;
            System.out.println("Media de números negativos ingresados: "+
                    mediaNegativos);
        }
        
        System.out.println("Cantidad de ceros ingresados: "+cantidadCeros);
        
       
    }
}
