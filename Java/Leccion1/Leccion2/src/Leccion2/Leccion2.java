
package Leccion2;

import java.util.Scanner;

public class Leccion2 {
    public static void main(String[] args) {
        /*
        var condicion = true;
        if(condicion) {
            System.out.println("Condición Verdadera"); //condicional simple
        }
        else{
            System.out.println("Condición Falsa"); //condicional doble
        }
        
        var numero = 3;
        var numeroTexto = "Número desconocido";
        
        //Sentencia de control if else (si/sino)
        
        if(numero == 1){
            numeroTexto = "Número uno";
        }
        else if(numero == 2){
            numeroTexto = "Número dos";
        }
        else if(numero == 3){
            numeroTexto = "Número tres";
        }
        else if(numero == 4){
            numeroTexto = "Número cuatro";
        }
        else{
            numeroTexto = "Número no encontrado";
        }
        System.out.println("numeroTexto = " + numeroTexto);
        */
        
        //Sentencia de control switch (según)
        Scanner input = new Scanner(System.in);
        System.out.print("Digite un número del 1 al 4: ");
        var numero = Integer.parseInt(input.nextLine());
        var numeroTexto = "Valor desconocido";
        switch(numero){
            case 1:
                numeroTexto = "Número uno";
                break;
            case 2:
                numeroTexto = "Número dos";
                break;
            case 3:
                numeroTexto = "Número tres";
                break;
            case 4:
                numeroTexto = "Número cuatro";
                break;
            default:
                numeroTexto = "Caso no encontrado";
        }
        System.out.println("numeroTexto = " + numeroTexto);
    }
}
