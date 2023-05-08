package paquete1;

import paquete2.Clase4;

public class TestPrivate {
    public static void main(String[] args) {
        Clase4 clase4 = new Clase4("Public");
        clase4.setAtributoPrivate("Cambio del atributo private");
        System.out.println("clase4 = " + clase4.getAtributoPrivate());
        
        System.out.println("Accedemos al metodo private desde un metodo public: ");
        clase4.metodoPublic();
    }
}
