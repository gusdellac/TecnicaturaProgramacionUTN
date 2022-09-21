
package Operaciones;

public class Aritmetica { // nomenclatura pascalcase
    //Atributos de la clase
    int a; // valor por default para un int es 0
    int b;
    
    //Método
    public void sumarNumeros(){ //public void (modificador de acceso) . Nomenclatura camelcase
        int resultado = a + b;
        System.out.println("resultado = " + resultado);
    }
}
