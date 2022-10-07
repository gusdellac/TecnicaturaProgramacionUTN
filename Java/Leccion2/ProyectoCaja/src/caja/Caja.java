/*
Proyecto caja:
Ejercicio 1: Crear un proyecto según las especificaciones mostradas
a continuación:
La fórmula es: volumen = ancho * alto * profundidad
*/

package caja;

public class Caja {
    public double ancho;
    public double alto;
    public double profundidad;
    
    public Caja(){
        System.out.println("Se está ejecutando el constructor número 1");
    }
    
    public Caja(double ancho, double alto, double profundidad){ 
        this.ancho = ancho;
        this.alto = alto;
        this.profundidad = profundidad;
        System.out.println("Se está ejecutando el constructor número 2");
    }
    
    public double calculoVolumen () {
        return ancho * alto * profundidad;
    }
}
