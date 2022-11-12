
package test;

import domain.Persona;

public class TestArraysObject {
    public static void main(String[] args) {
        Persona personas[] = new Persona[2];
        personas[0] = new Persona("Gustavo");
        personas[1] = new Persona("De Llac");
        
        System.out.println("Persona[0] = "+personas[0]);
        System.out.println("Persona[1] = "+personas[1]);
        
        //arrays sintaxis resumida
        String frutas[] = {"Banana", "Pera", "Durazno"};
        
        //array recorrido con forEach
        for(String fruta: frutas){
            System.out.println(fruta);
        }
    }
}
