
package Ejercicio6;

import java.util.Scanner;

public class Ejercicio6 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Digite los dolares que posee Guillermo: US$ ");
        float dolaresGuillermo = Float.parseFloat(input.nextLine());
        float dolaresLuis = dolaresGuillermo/2;
        float dolaresJuan = (dolaresGuillermo + dolaresLuis)/2;
        float sumaDolares = dolaresGuillermo + dolaresLuis + dolaresJuan;
        System.out.println("La sumatoria de los dolares de Guillermo,Luis y Juan es: US$ " + sumaDolares);
    }
    
}
