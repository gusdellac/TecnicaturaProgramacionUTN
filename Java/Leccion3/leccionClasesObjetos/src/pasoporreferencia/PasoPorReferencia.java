//Paso por referencia
package pasoporreferencia;

import Clases.Persona;

public class PasoPorReferencia {
    public static void main(String[] args) {
        Persona persona1 = new Persona();
        persona1.nombre = "Ester";
        System.out.println("persona1 nombre = " + persona1.nombre);
        cambiarValor(persona1);
        System.out.println("El cambio que hicimos en el nombre es: " +persona1.nombre);
        persona1 = cambiarElValor(persona1);
        //Persona persona2 = null;
        Persona persona2 = new Persona();
        persona2 = cambiarElValor(persona2);
        System.out.println("El nuevo valor del objeto es: "+persona2.nombre);
    }
    
    // En éste método siempre se retorna algo. return automático
    public static void cambiarValor(Persona persona){ //parámetro por referencia
        persona.nombre = "María"; //modificamos el valor almacenado en la memoria heap
    }
    
    //retorna un dato de tipo object
    public static Persona cambiarElValor(Persona persona){
        if(persona == null){
            System.out.println("Valor de persona es inválido: Null");
            return null;
        }else{
            persona.nombre = "Mónica";
            return persona;
        }
       
    }
}
