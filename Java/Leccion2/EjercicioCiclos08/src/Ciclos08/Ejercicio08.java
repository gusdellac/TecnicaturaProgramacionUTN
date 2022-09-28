/*
Ejercicio 8: Pedir un número N, y mostrar todos los números del 1 al N.
Clase JOptionPane
*/
package Ciclos08;

import javax.swing.JOptionPane;

public class Ejercicio08 {
    public static void main(String[] args) {
        int numero, contador = 1;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        while(contador <= numero){
            JOptionPane.showMessageDialog(null, contador+" ");
            contador++;
        }
    }
}
