/*
Uso de la palabra Final.

Esta palabra reservada tiene diferentes significados dependiendo donde se 
utilice:
- variables: Evita cambiar el valor que almacena la variable (constante)
- métodos: Evita que se modifique la definición o el comportamiento de un 
método desde una subclase (hija)
-clases: Evita que se creen clases hijas
Otra característica es que normalmente cuando trabajamos ocn variables, se 
combina con el modificador de acceso estático para convertir una variable
en una constante, es decir, que no se puede modificar su valor, el ejemplo
de esto es la clase Math en la cuál todos sus atributos son de tipo static
y final, es por esto que la variable pi* se conoce como una constante.
*/
package test;

import domain.Persona;

public class TestFinal {
    public static void main(String[] args) {
        final int miDni = 38208173;
        System.out.println("miDni = " + miDni);
        
//        Persona.CONSTANTE_AQUI = 9; //no compila porque es una constante
        
        System.out.println("Mi atributo constante es: "+Persona.CONSTANTE_AQUI);
        
        final Persona persona1 = new Persona();
//        persona1 = new Persona(); //no se puede asignar una nueva referencia
        persona1.setNombre("Gustavo");
        System.out.println("persona1 = " + persona1.getNombre());
        persona1.setNombre("Ariel");
        System.out.println("persona1 = " + persona1);
    }
}
