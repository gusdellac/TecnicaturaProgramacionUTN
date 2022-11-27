/*
Ejercicio 5: Crear y cargar una matriz de tamaño n x m, mostrar la suma de cada
fila y de cada columna.
*/
package test;

import java.util.Scanner;

public class TercerEjercicioMatrices {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int filas, columnas, sumaFilas = 0, sumaColumnas = 0;
        System.out.print("Digite el número de filas de la matriz: ");
        filas = input.nextInt();
        System.out.print("Digite el número de columnas de la matriz: ");
        columnas = input.nextInt();
        int matriz[][] = new int [filas][columnas];
        System.out.println("Ingrese los elementos de la matriz: ");
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {
                System.out.print("matriz ["+i+"]"+"["+j+"]: ");
                matriz[i][j] = input.nextInt();
            }
        }
        System.out.println("Matriz ingresada: ");
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {
                System.out.print(matriz[i][j]+ " "); 
            }
            System.out.println();
        }
        System.out.println("Suma de filas y columnas: ");
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {
                sumaFilas += matriz[i][j];
            }
            System.out.println("Suma fila " + (i+1) + ": " + sumaFilas);
            sumaFilas = 0;
        }
        
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {
                sumaColumnas += matriz[j][i];
            }
            System.out.println("Suma columna " + (i+1) + ": " + sumaColumnas);
            sumaColumnas = 0;
        }
        
    }
}
