
package Ejercicio7;

import java.util.Scanner;

public class Ejercicio7 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        final int salarioConstante = 1000;
        System.out.print("Digite cantidad vehículos vendidos: ");
        int autosVendidos = Integer.parseInt(input.nextLine());
        System.out.print("Digite el precio: ");
        float precioAuto = Float.parseFloat(input.nextLine());
        float totalAutosVendidos = autosVendidos * precioAuto;
        float salarioEmpleado = salarioConstante + (autosVendidos * 150) + (totalAutosVendidos * 0.05f);
        System.out.println("Salario mensual del vendedor: " + salarioEmpleado);
    }
    
}
