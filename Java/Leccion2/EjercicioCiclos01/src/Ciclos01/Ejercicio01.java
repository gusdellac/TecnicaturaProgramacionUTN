/*
Ejercicio 1: Leer un número y mostrar su cuadradao, repetir
el proceso hasta que se introduzca un número negativo.
*/

package Ciclos01;

import javax.swing.JOptionPane; //importamos paquete javax.swing.JOptionPane que trae la clase JOptionPane. 

public class Ejercicio01 {
    public static void main(String[] args) {
        int numero, cuadrado;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: ")); /*Utilizamos la clase JOptionPane con el método
        showInputDialog() para habilitar el ingreso de un dato por el usuario. Argumento del método es un string con un mje que se va a exhibir*/
        
        while(numero >= 0){ //Mientras el número sea igual a cero o positivo
            cuadrado = (int)Math.pow(numero, 2); /*utilizamos la clase Math con el 
            método pow() para realizar el cuadrado, (1er parámetro número a elevar,
            2do parámetro potencia). Le indicamos al inicio el tipo de dato a retornar (int)*/
            System.out.println("El numero "+numero+" elevado al cuadrado es: "+cuadrado);
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro número: "));
        }
        System.out.println("El programa a finalizado por el ingreso de un número negativo.");
    }
}
