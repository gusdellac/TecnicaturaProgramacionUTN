import java.util.Scanner;

public class CalculadoraUTN {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        while (true){
            System.out.println("****** Aplicacion Calculadora *******");
            mostrarMenu();
            try {
                int operacion = Integer.parseInt(entrada.nextLine());

                if(operacion >= 1 && operacion <= 4){
                    ejecutarOperacion(operacion, entrada);
                } //fin del if
                else if (operacion == 5){
                    System.out.println("Hasta pronto...");
                    break; //Rompe el ciclo y sale
                }
                else {
                    System.out.println("Opcion erronea: "+operacion);
                }
                System.out.println();
            } //fin try
            catch(Exception e){
                System.out.println("Ocurrió un error: "+e.getMessage());
                System.out.println();
            } //fin catch

        } //fin while

    } //fin main

    private static void mostrarMenu(){
        //Mostramos el menu
        System.out.println("""
                1. Suma
                2. Resta
                3. Division
                4. Multiplicacion
                5. Salir
                """);
        System.out.print("Operacion a realizar? ");
    } //fin metodo mostrarMenu()

    private static void ejecutarOperacion(int operacion, Scanner entrada){
        double resultado;
        double operando1;
        double operando2;

        System.out.print("Digite el valor para el operando1: ");
        operando1 = Double.parseDouble(entrada.nextLine());
        System.out.print("Digite el valor para el operando2: ");
        operando2 = Double.parseDouble(entrada.nextLine());

        switch (operacion){
            case 1 -> { //suma
                resultado = operando1 + operando2;
                System.out.println("Resultado de la suma: "+resultado);
            }
            case 2 -> { //resta
                resultado = operando1 - operando2;
                System.out.println("Resultado de la resta: "+resultado);
            }
            case 3 -> { //division
                resultado = operando1 / operando2;
                System.out.println("Resultado de la division: "+resultado);
            }
            case 4 -> { //multiplicacion
                resultado = operando1 * operando2;
                System.out.println("Resultado de la multiplicacion: "+resultado);
            }
            default -> System.out.println("Opcion erronea: "+operacion);
        } //fin switch
    } //fin metodo ejecutarOperacion()
} //fin clase
