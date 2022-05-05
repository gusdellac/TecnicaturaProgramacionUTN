
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
        /*
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite su nombre: ");
        
        /*Usamos ctrl + espacio para buscar el paquete.
        Sintaxis de creación de objeto. 
        Esta clase es necesario importarla. Se encuentra en otro
        paquete llamado java.util.scanner
        utilizamos este objeto para poder leer datos ingresados desde la 
        consola
        
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
        */
        
        /*
        byte numEnteroByte = 127;//definimos un tipo de dato byte
        //colocando byte + variable definida. El (byte) obliga al compilador a que 
        //convierta el dato asignado a tipo byte. Si el valor asignado supera el máximo
        //o mínimo permitido se generará pérdida de precisión
        System.out.println("numEnteroByte = " + numEnteroByte);
        System.out.println("valor mínimo del Byte:" + Byte.MIN_VALUE);//-128
        System.out.println("valor máximo del Byte:" + Byte.MAX_VALUE);//127
        //Byte.MIN_VALUE para poder evaluar los mínimos y maximos del tipo de dato
        //es necesario que utilicemos la clase Byte
        
        short numEnteroShort = 32767;
        System.out.println("numEnteroShort = " + numEnteroShort);
        System.out.println("Valor mínimo del Short:" + Short.MIN_VALUE); //-32768
        System.out.println("Valor máximo del Short:" + Short.MAX_VALUE); //32767
        
        int numEnteroInt = 2147483647;
        System.out.println("numEnteroInt = " + numEnteroInt);
        System.out.println("Valor mínimo del int:" + Integer.MIN_VALUE); //-2147483648
        System.out.println("Valor máximo del int:" + Integer.MAX_VALUE); //2147483647
        //java por defecto trabajo con los números enteros int de 32 bits
        
        long numEnteroLong = 9223372036854775807L; //Java por defecto asigna el máximo de números enteros
        //a los int, por lo que al asignar un número tipo long es necesario colocar
        //la L al final del número.
        System.out.println("numEnteroLong = " + numEnteroLong);
        System.out.println("Valor mínimo del long:" + Long.MIN_VALUE); //-9223372036854775808
        System.out.println("Valor mínimo del long:" + Long.MAX_VALUE); //9223372036854775807
        */
        
        float numFloat = (float) 3.4028235E38F; //Por defoult java asigna los datos decimales al tipo double
        //se forza a float usando (float) o F al final del número.
        System.out.println("numFloat = " + numFloat);
        System.out.println("El valor mínimo de float:" + Float.MIN_VALUE); //1.4E-45
        System.out.println("El valor máximo de float:" + Float.MAX_VALUE); //3.4028235E38
        
        
        double numDouble = 1.7976931348623157E308D;
        System.out.println("numDouble = " + numDouble);
        System.out.println("El valor mínimo del double:" + Double.MIN_VALUE); //4.9E-324
        System.out.println("El valor máxmio del double:" + Double.MAX_VALUE); //1.7976931348623157E308
        
    }

}
