
public class HolaMundoGit {
    public static void main(String[] args) {
        System.out.println("Hola mundo desde Java");
        
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
           
    }
       
}
