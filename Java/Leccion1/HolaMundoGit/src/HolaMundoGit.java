
import java.util.Scanner;


public class HolaMundoGit {

    public static void main(String[] args) {
        /*System.out.println("Hola mundo desde Java");
        
        int miVariable = 10; //Variable instanciada (definida) como int
        System.out.println(miVariable);
        miVariable = 5;
        System.out.println(miVariable);
        //miVariable no podra ser utilizada fuera de este método (alcance)
        //Tipo String , es un objeto no un tipo primitivo
        String miVariableCadena = "Hola mundo en cadena";
        System.out.println(miVariableCadena);
        miVariableCadena = "Sigamos creciendo en programación";
        System.out.println(miVariableCadena); //Ctrl + click sobre variable y 
        //nos muestra donde fue instanciada la variable y ver su tipo de dato
        */

        /* //Var - inferencia de datos en Java
        
        var miVariableEntera2 = 10;
        System.out.println("miVariableEntera2 = " + miVariableEntera2);
        //soutv + tab y genera el print con la sintaxis correcta para
        //imprimir el nombre de la variable y su valor.
        //Notar que se concatenan un string + un int
        var miVariableCadena2 = "Seguimos estudiando";
        System.out.println("miVariableCadena2 = " + miVariableCadena2);
        //Notar que se concatenan dos string
        
        
        //De esta forma solo imprimimos el valor de la variable
        var varEntera = 15;
        System.out.println(varEntera);
        var miString = "Hola mundo";
        System.out.println(miString);
        
        //Reglas para definir una variable en Java:
        //_miVar; $miVar; miVar; miVar2; (son formas correctas)
        
        //Concatenación
        
        var usuario = "Osvaldo";
        var titulo ="Ingeniero";
        var union = titulo + " " + usuario;
        System.out.println("union = " + union);
      
        //Click derecho + format ordena el código
        */
        /*var a = 8;
        var b = 4;
        var c = "Hola";
        System.out.println(a + b);
        System.out.println(c + a + b); //la prioridad es de izquierda a derecha
        //en este caso concatena la cadena con los números sin operarlos y queda
        //todo de tipo string

        System.out.println(c + (a + b)); //la prioridad es los paréntesis
        //realiza la suma de los números y luego concatena con el string
        //queda todo en tipo string

        //Caracteres especiales en Java
        var nombre = "Natalia";
        System.out.println("\nNueva linea: \n" + nombre); // \n salto de línea
        //alt + 92
        System.out.println("Tabulador: \t" + nombre);
        System.out.println("\t\t.:MENU:."); //Espacio igual a tabulador 
        System.out.println("Retroceso: \b\b" + nombre); //Caracter de retroceso
        System.out.println("Comillas simples: \'" + nombre + "\'");
        System.out.println("Comillas dobles: \"" + nombre + "\"");
        */
        
        //Clase Scanner
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite su nombre: ");
        
        /*Usamos ctrl + espacio para buscar el paquete.
        Sintaxis de creación de objeto. 
        Esta clase es necesario importarla. Se encuentra en otro
        paquete llamado java.util.scanner
        utilizamos este objeto para poder leer datos ingresados desde la 
        consola*/
        
        var usuario2 = entrada.nextLine(); //Llamamos al objeto más el método
        //nextLine()
        System.out.println("usuario2 = " + usuario2);
        System.out.println("Escriba su profesión: ");
        var titulo2 = entrada.nextLine();
        System.out.println("Resultado: "+titulo2+" "+usuario2);
        
        //Ejercicio Clase
        Scanner input = new Scanner(System.in); //La clase ya fue importada
        //por lo que no se visualizará la importación otra vez
        
        System.out.println("Ingrese el título del libro");
        var libro = input.nextLine();
        
        System.out.println("Ingrese el Autor");
        var autor = input.nextLine();
        
        System.out.println(libro+" fué escrito por "+autor);
        
        
        
        

    }

}
