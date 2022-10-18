
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
        
        //aritmetica1 = null; //no se debe realizar , es una mala práctica
        //System.gc(); //garbage collector , no utilizar (ver)
        Persona persona = new Persona("Ariel", "Betancud");
        System.out.println("persona = "+ persona);
        System.out.println("Persona nombre: "+ persona.nombre);
        System.out.println("Persona apellido: "+persona.apellido);
        
    }
    
    //Modularidad creamos un nuevo método
    public static void miMetodo(){
        var a = 10; //es necesario volver a inicializar la variable 
        System.out.println("Aquí hay otro método");
    }
    
    
    
}

//creamos otra clase dentro del mismo archivo.java. Dentro del mismo archivo
//solo una clase puede ser public

class Persona{ //por defecto el modificador de acceso es default o package
    String nombre;
    String apellido;
    
    //constructor 
    Persona(String nombre, String apellido){
        super(); //Llamada al constructor de la clase Padre Object
        new Imprimir().imprimir(this);
        this.nombre = nombre;
        this.apellido = apellido;
        System.out.println("Objeto persona usando this: "+this); // nos devuelve
        //la referencia en memoria del objeto instanciado de esta clase Persona
        
    }
    
}

class Imprimir{
    public Imprimir(){
        super(); //constructor de la clase padre
    }
    
    public void imprimir(Persona persona){
        System.out.println("Persona desde la clase imprimir: "+persona);
        System.out.println("Impresión del objeto actual (this): "+this);
    }
}
