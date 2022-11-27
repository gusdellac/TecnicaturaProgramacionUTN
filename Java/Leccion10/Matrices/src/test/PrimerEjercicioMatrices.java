/*
Ejercicio 3 : Crear y cargar una matriz de tamaño 3x3, transponerla y mostrarla
 */
package test;

import java.util.Scanner;

public class PrimerEjercicioMatrices {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        int matriz[][] = new int[3][3];
        
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {
                System.out.print("Digite un número ["+i+"]["+j+"]: ");
                matriz[i][j] = Integer.parseInt(input.nextLine());
            }
        }
        
        System.out.println("Matriz original: ");
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {
                System.out.print(matriz[i][j]+" ");
            }
            System.out.println();
        }
     
        
        System.out.println("Matriz transpuesta: ");
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {
                System.out.print(matriz[j][i]+" ");
            }
            System.out.println();
        }
    }
   
}
