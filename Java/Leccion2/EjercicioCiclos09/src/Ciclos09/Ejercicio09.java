
package Ciclos09;

import javax.swing.JOptionPane;

public class Ejercicio09 {
    public static void main(String[] args) {
        int dia, mes, anio;
        boolean fechaCorrecta = false;
        dia = Integer.parseInt(JOptionPane.showInputDialog("Digite el día: "));
        mes = Integer.parseInt(JOptionPane.showInputDialog("Digite el mes: "));
        anio = Integer.parseInt(JOptionPane.showInputDialog("Digite el anio: "));
       
        if((dia >= 1 && dia <= 30)&&(mes >= 1 && mes <= 12)&&(anio >= 1 && dia <= 2022)){
            fechaCorrecta = true;
        }
        if(fechaCorrecta){
            JOptionPane.showMessageDialog(null, 
            "La fecha: "+dia+"/"+mes+"/"+anio+"\nEs correcta!!!");
        }
        else{
            JOptionPane.showMessageDialog(null, 
            "La fecha: "+dia+"/"+mes+"/"+anio+"\nEs incorrecta!!!");
        }
    }
}
