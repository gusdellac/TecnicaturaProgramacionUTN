
package test;

//import dominio.*; //importamos todas las clases que esten dentro del paquete
import dominio.Persona;

public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Osvaldo", 57000.00, false);
        System.out.println("persona1 su nombre es: "+persona1.getNombre());
        //modificamos atributos a través de los setters
        persona1.setNombre("Juan Ignacio");
        //accedemos a atributos a través de los getters
        System.out.println("persona1 su modificado es: "+persona1.getNombre());
        System.out.println("persona1 el resultado para el sueldo: "+persona1.getSueldo());
        System.out.println("persona1 para obtener el booleano: "+persona1.isEliminado());
        
        System.out.println("persona1 = " + persona1); /*
        no es necesario hacer explícita la llamada al método toString(),
        si sobreescribimos este método en la clase, al imprimir el objeto
        se ejecutará el método toString() que nos retornará una cadena
        */
        
        //System.out.println("persona1: "+persona1.toString());
        
    }
}
