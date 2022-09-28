/*
Ejercicio 9: Pedir el día, mes y año de una fecha e indicar si la fecha es correcta.
Suponiendo que todos los meses son de 30 días
*/
package Ciclos09;

import java.util.Scanner;

public class Ciclos09 {
    public static void main(String[] args) {
        int dia, mes, anio;
        boolean fechaCorrecta = false;
        Scanner input = new Scanner(System.in);
        System.out.print("Ingrese el día: ");
        dia = Integer.parseInt(input.nextLine());
        System.out.print("Ingrese el mes: ");
        mes = Integer.parseInt(input.nextLine());
        System.out.print("Ingrese el año: ");
        anio = Integer.parseInt(input.nextLine());
        
        if((dia >= 1 && dia <= 30)&&(mes >= 1 && mes <= 12)&&(anio >= 1 && dia <= 2022)){
            fechaCorrecta = true;
        }
        if(fechaCorrecta){
            System.out.println("La fecha: "+dia+"/"+mes+"/"+anio+"\nEs correcta!!!");
        }
        else{
            System.out.println("La fecha: "+dia+"/"+mes+"/"+anio+"\nEs incorrecta!!!");
        }
    }
}
