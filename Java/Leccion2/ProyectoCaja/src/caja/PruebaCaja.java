
package caja;

public class PruebaCaja {
    public static void main(String[] args) {
        Caja caja1 = new Caja();
        caja1.alto = 10.5;
        caja1.ancho = 20.5;
        caja1.profundidad = 5;
        double volumen = caja1.calculoVolumen();
        System.out.println("El volumen es: " + volumen);
        
        Caja caja2 = new Caja(6, 7.5, 3.5 );
        volumen = caja2.calculoVolumen();
        System.out.println("El volumen es: " + volumen);
        
    }
}
