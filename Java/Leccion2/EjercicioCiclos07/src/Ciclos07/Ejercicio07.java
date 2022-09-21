
package Ciclos07;

import javax.swing.JOptionPane;

public class Ejercicio07 {
    public static void main(String[] args) {
        int numero, conteo = 0, suma = 0;
        float promedio = 0;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        while(numero >= 0){
            suma += numero;
            conteo++;
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro número: "));
        }
        if(conteo == 0){
            JOptionPane.showMessageDialog(null, "Error, la división entre cero es cero");
        }
        else{
            promedio = (float)suma/conteo;
            JOptionPane.showMessageDialog(null, "\nEl promedio es: "+promedio);
        }
    }
}
