
package Ciclos02;

import javax.swing.JOptionPane;

public class Ejercicio02claseJOptionPane {
    public static void main(String[] args) {
        var number = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        while(number != 0){
            if(number > 0){
                JOptionPane.showMessageDialog(null, "El número "+number+" es POSITIVO!!");
            }
            else{
                JOptionPane.showMessageDialog(null, "El número "+number+" es NEGATIVO!!");
            }
            number = Integer.parseInt(JOptionPane.showInputDialog("Digite otro número: "));
        }
        JOptionPane.showMessageDialog(null, "El número "+number+" finaliza el programa.");
    }
}
