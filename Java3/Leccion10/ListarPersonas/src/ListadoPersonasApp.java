import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class ListadoPersonasApp {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        //Definimos la lista fuera del ciclo while
        List<Persona> personas = new ArrayList<>();
        //Empezamos con el menu
        var salir = false;
        while(!salir){
            mostrarMenu();
            try{
                salir = ejecutarOperacion(entrada, personas);
            }
            catch(Exception e){
                System.out.println("Ocurrio un error: "+e.getMessage());
            }
            System.out.println();
        } //fin ciclo while
    } //fin metodo main

    private static void mostrarMenu(){
        //mostramos las opciones
        System.out.print("""
                    ******* Listado de Personas ******* 
                    1. Agregar
                    2. Listar
                    3. Salir
                    """);
        System.out.print("Digite una de las opciones: ");
    }// fin metodo mostrarMenu()

    private static boolean ejecutarOperacion(Scanner entrada, List<Persona> personas){
        var opcion = Integer.parseInt(entrada.nextLine());
        var salir = false;
        //Revisamos la opcion digitada a traves de un switch
        switch (opcion){
            case 1 -> { //agregar una persona a la lista
                System.out.print("Digite el nombre: ");
                var nombre = entrada.nextLine();
                System.out.print("Digite el telefono: ");
                var tel = entrada.nextLine();
                System.out.print("Digite el correo: ");
                var email = entrada.nextLine();
                //creamos el objeto persona
                Persona persona = new Persona(nombre, tel, email);
                //agregamos la persona a la lista
                personas.add(persona);
                System.out.println("La lista tiene: "+personas.size()+" elementos");
            }//fin caso1

            case 2 -> { //listar a las personas
                System.out.println("Listado de personas: ");
                //mejoras con lambda y el metodo de referencia
                //personas.forEach((persona) -> System.out.println(persona)); //forEach con expresion lamda
                personas.forEach(System.out::println); //forEach con metodo de referencia?
            }//fin caso2

            case 3 -> {// salir del ciclo
                System.out.println("Hasta pronto!!");
                salir = true;
            }//fin del caso 3
            default -> System.out.println("Opcion incorrecta: "+opcion);

        }//fin switch
        return salir;
    }//fin metodo ejecutarOperacion()
}//fin de la calse ListadoPersonasApp
