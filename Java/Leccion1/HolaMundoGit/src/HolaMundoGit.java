
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
        //8 bits
        System.out.println("numEnteroByte = " + numEnteroByte);
        System.out.println("valor mínimo del Byte:" + Byte.MIN_VALUE);//-128
        System.out.println("valor máximo del Byte:" + Byte.MAX_VALUE);//127
        //Byte.MIN_VALUE para poder evaluar los mínimos y maximos del tipo de dato
        //es necesario que utilicemos la clase Byte
        
        short numEnteroShort = 32767; //16 bits
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
        //la L al final del número. 64 bits
        System.out.println("numEnteroLong = " + numEnteroLong);
        System.out.println("Valor mínimo del long:" + Long.MIN_VALUE); //-9223372036854775808
        System.out.println("Valor mínimo del long:" + Long.MAX_VALUE); //9223372036854775807
        */
        
        /*
        float numFloat = (float) 3.4028235E38F; //Por defoult java asigna los datos decimales al tipo double
        //se forza a float usando (float) o F al final del número. 32 bits
        System.out.println("numFloat = " + numFloat);
        System.out.println("El valor mínimo de float:" + Float.MIN_VALUE); //1.4E-45
        System.out.println("El valor máximo de float:" + Float.MAX_VALUE); //3.4028235E38
        
        
        double numDouble = 1.7976931348623157E308D; //64 bits
        System.out.println("numDouble = " + numDouble);
        System.out.println("El valor mínimo del double:" + Double.MIN_VALUE); //4.9E-324
        System.out.println("El valor máxmio del double:" + Double.MAX_VALUE); //1.7976931348623157E308
        */
        
        //Inferencia de tipos var y tipos primitivos
        /*
        var numEntero = 20; //por default las literales enteras son de tipo int
        System.out.println("numEntero = " + numEntero);
        var numFloat = 10.0F; //por default las literales con decimales son de tipo double
        System.out.println("numFloat = " + numFloat);
        var numDouble = 10.0;
        System.out.println("numDouble = " + numDouble);
        
        /*breakpoint (punto de ruptura) se utiliza para realizar el paso a paso desde la línea seleccionada
        Usamos click derecho y opción debug file */
        
        //Tipos primitivos char
        
        /*
        char miVariableChar = 'a'; //notar que la asignación a char se realiza entre ('') 
        // tipo char 16 bits puede almacenar un caracter y valores decimales
        System.out.println("miVariableChar = " + miVariableChar);
        
        char varCaracter = '\u0024'; //Indicamos a Java la asignación con el código unicode
        System.out.println("varCaracter = " + varCaracter);
        char varCaracterDecimal = 36; //Valor decimal del juego de caracteres unicode
        System.out.println("varCaracterDecimal = " + varCaracterDecimal);
        char varCaracterSimbolo = '$'; //caracter especial, podemos copiar y pegar desde unicode
        System.out.println("varCaracterSimbolo = " + varCaracterSimbolo);
        
        //inferencia de tipo
        var varCaracter1 = '\u0024';
        System.out.println("varCaracter1 = " + varCaracter1);
        var varCaracterDecimal1 = (char)36; //olbigamos a que asigne el valor como tipo char
        System.out.println("varCaracterDecimal1 = " + varCaracterDecimal1);
        var varCaracterSimbolo1 = '$';
        System.out.println("varCaracterSimbolo1 = " + varCaracterSimbolo1);
        
        int varEnteroChar = '$'; //nos muestra el valor decimal asociado al símbolo
        System.out.println("varEnteroChar = " + varEnteroChar);
        int caracterChar = 'b'; //nos muestra el valor decimal asociado al símbolo
        System.out.println("caracterChar = " + caracterChar);
        */
        
        //Tipos primitivos tipos booleanos
        /*
        var varBool = false;  //los valores booleanos (verdadero/falso) se asigna true/ false. (en python True/False)
        System.out.println("varBool = " + varBool);
        
        if(varBool){
            System.out.println("La bandera es verde");  
        }
        else{
            System.out.println("La bandera es roja");
        }
        
        //Algoritmo: ¿Es mayor de edad?
        var edad = 28; //Java infiere que la literal es de tipo int
        //var adulto = edad >= 18; //Expresión booleana. Java infiere tipo de dato booelano
        if(edad >= 18){ //colocamos la expresión lógica en el condicional y nos ahorramos una línea de código
            //el if analizará la expresión y en caso de ser true ejecutará el código dentro del if,sino pasa al else
            System.out.println("Eres mayor de edad");
        }
        else{
            System.out.println("Eres menor de edad");
        }
        */
        
        //Conversión de tipos primitivos String a Int y Double
        /*
        var edad = Integer.parseInt("20"); //convertimos un dato tipo str a int
        System.out.println("edad = " +(edad + 1)); //a la variable edad tipo int le sumamos 1 y la imprimimos
        var valorPI = Double.parseDouble("3.1416"); //convertimos dato str a double
        System.out.println("valorPI = " + valorPI); //lo imprimimos en consola
        var strAfloat = Float.parseFloat("10.5");
        System.out.println("strAfloat = " + strAfloat);
        
        //Pedir un valor
        var entrada = new Scanner(System.in); // clase scanner (parámetro.atributo)
        // el dato a ingresar es de tipo str, java infiere el dato y lo asigna a var entrada
        System.out.println("Digite su edad:");
        edad = Integer.parseInt( entrada.nextLine()); // convertimos int(obejeto 'entrada'. método 'nextLine')
        System.out.println("edad = " + edad);
        */
        
        //Conversión de tipos primitivos 
        /*
        var edadTexto = String.valueOf(10); // Int a String. Clase String. método valueOf(int)
        System.out.println("edadTexto = " + edadTexto);
        
        var fraseChar = "programadores".charAt(10); //extraemos un carácter de la cadena
        //.charAt(índice) método para extraer el caracter
        System.out.println("fraseChar = " + fraseChar);
        
        var entrada = new Scanner(System.in);
        System.out.println("Digite un caracter: ");
        fraseChar = entrada.nextLine().charAt(0); //El caracter ingresado será de tipo string
        //con el método .charAt(indice) convertimos el str a char
        System.out.println("fraseChar = " + fraseChar);
        
        //string a boolean
        boolean varBoolean = Boolean.parseBoolean("true");
        System.out.println("varBoolean = " + varBoolean);
        */
        
        //la inferencia de tipos solo se puede hacer con una variable
        /*
        int num1 = 5, num2 = 4; // inicializamos mas de una variable en la misma línea
        //es necesario declarar el tipo de dato de las variables, no se puede inferir (en este caso int)
        
        var solucion = num1 + num2;
        System.out.println("solucion de la suma = " + solucion);
        
        solucion = num1 - num2;
        System.out.println("solucion de la resta = " + solucion);
        
        solucion = num1 * num2;
        System.out.println("solucion de la multiplicación = " + solucion);
        
        solucion = num1 / num2;
        System.out.println("solucion de la división = " + solucion);
        
        var solucion2 = 3.4 / num2; //infiere dato tipo double
        System.out.println("solucion2 = " + solucion2);
        
        solucion = num1 % num2; //guarda el residuo entero de la división
        System.out.println("solucion = " + solucion);
        
        //Cuando en una estructura if/else se utiliza solo una línea de código en cada bloque
        //no es necesario utilizar las llaves de apertura y cierre
        if (num1 % 2 == 0){
            System.out.println("El número es par");
        } else {
            System.out.println("El número es impar");
        }
        */
        
        //operadores asignación
        
        int varNum1 = 1, varNum2 = 4;
        int varNum3 = varNum1 + 6 - varNum2; 
        System.out.println("varNum3 = " + varNum3);
        
        varNum1 += 1; //Incrementa la variable en 1 (varNum1 = varNum1 + 1)
        System.out.println("varNum1 = " + varNum1);
        // +=     -=    *=     /=    %=
        varNum2 -=2;
        System.out.println("varNum2 = " + varNum2);
        varNum1 *=5;
        System.out.println("varNum1 = " + varNum1);
        varNum3 /=4;
        System.out.println("varNum3 = " + varNum3);
        varNum1 %= 6;
        System.out.println("varNum1 = " + varNum1);
    }

}
