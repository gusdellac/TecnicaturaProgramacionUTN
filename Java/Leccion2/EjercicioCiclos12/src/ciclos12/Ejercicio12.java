/*
 Ejercicio 12: Pedir un número y calcular su factorial.
 Hacerlo con JOptionPane
 */

package ciclos12;

import javax.swing.JOptionPane;

public class Ejercicio12 {
    public static void main(String[] args) {
        int numero, factorial = 1;
        do{
            System.out.println("Digite un número: ");
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite "
                    + "un número: "));
            if(numero < 0){
                JOptionPane.showMessageDialog(null, "No se puede calcular "
                        + "el factorial de un número negativo.");
            }    
        }while(numero < 0);
        
        for(int i = 1; i <= numero; i++){
            factorial *= i;
        }
        JOptionPane.showMessageDialog(null, "El factorial de "+numero+" es:"
                + " "+factorial);
  
    }
}
