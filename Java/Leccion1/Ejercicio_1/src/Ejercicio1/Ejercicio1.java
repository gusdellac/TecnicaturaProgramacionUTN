//Tienda de libros
package Ejercicio1;

import java.util.Scanner;

public class Ejercicio1 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner (System.in);
        System.out.println("Digite el nombre del libro");
        String nombreLibro = entrada.nextLine();
        System.out.println("Digite el id del libro");
        int idLibro = Integer.parseInt(entrada.nextLine());
        System.out.println("Digite el precio del libro");
        double precioLibro = Float.parseFloat(entrada.nextLine());
        String envio = "";
        //Envío gratuito a partir de $ 2000
        if (precioLibro >= 2000){
            envio = "Envío gratuito";
        }else{
            envio = "Envío pago";
        }
        System.out.println("\nNombre libro: "+nombreLibro + "\nID libro: #"+idLibro + "\nPrecio libro: $ "+precioLibro + "\nTipo de envío: "+envio);
    }
}
