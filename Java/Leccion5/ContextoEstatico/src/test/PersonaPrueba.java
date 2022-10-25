
package test;

import domain.Persona;

public class PersonaPrueba {
    private int contador;
    
    public static void main(String[] args) {
        Persona persona1 = new Persona("Ariel");
        System.out.println("persona1 = " + persona1);
        Persona persona2 = new Persona("gustavo");
        System.out.println("persona2 = " + persona2);
        imprimir(persona1);
        imprimir(persona2);
        
        //Instanciamos dentro del método main un objeto de la misma clase
        //a la que pertenece. Debemos hacerlo para poder acceder a un atributo
        //de la clase que no utilice un contexto estático (static).
        
        PersonaPrueba personaP1 = new PersonaPrueba();
        System.out.println(personaP1.contador); //podemos acceder directamente
        //al atributo sin necesidad de un getter apesar de que el atributo sea
        //privado. Esto se logra porque el método desde el que lo llamamos
        //forma parte de la misma clase
        
        System.out.println(personaP1.getContador()); //accedemos al atributo
        //usando un getter
    }
    
    //contexto estático
    public static void imprimir(Persona persona){
        System.out.println("persona = " + persona);
    }
    
    public int getContador(){
        return this.contador;
    }

    
    
    
}
