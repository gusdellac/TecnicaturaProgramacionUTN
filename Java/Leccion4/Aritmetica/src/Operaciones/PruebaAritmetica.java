
package Operaciones;

public class PruebaAritmetica {
    public static void main(String[] args) {
        int a = 10; //variables locales. No tienen alcance fuera de este método main
        int b = 7; //memoria stack. Sólo almacena la referencia del objeto
        miMetodo(); //llamamos al método miMetodo()
        Aritmetica aritmetica1 = new Aritmetica(); /*cuando colocamos los paréntesis
        después del nombre de la clase "Aritmetica()" lo que hacemos es llamar al constructor
        de la clase y reservar espacio en memoria para instanciar el objeto*/
        aritmetica1.a = 3;
        aritmetica1.b = 7;
        aritmetica1.sumarNumeros();
        
        //Para almacenar un objeto o los atributos se utiliza la memoria heap
        int resultado = aritmetica1.sumarConRetorno();
        System.out.println("resultado = " + resultado);
        
        resultado = aritmetica1.sumarConArgumentos(12, 26);
        System.out.println("resultado usando argumentos = " + resultado);
        
        System.out.println("aritmetica1 a: "+aritmetica1.a);
        System.out.println("aritmetica1 a: "+aritmetica1.b);
        
        Aritmetica aritmetica2 = new Aritmetica(5, 8);
        System.out.println("aritmetica2 = " + aritmetica2.a);
        System.out.println("aritmetica2 = " + aritmetica2.b);
        
        //aritmetica1 = null;
        //System.gc();
    }
    
    public static void miMetodo(){
        var a = 10; //es necesario volver a inicializar la variable 
        System.out.println("Aquí hay otro método");
    }
}
