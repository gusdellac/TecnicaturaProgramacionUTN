package test;

import paquete1.Clase1;
import paquete2.Clase3;

public class TestModificadoresAcceso {
    public static void main(String[] args) {
        System.out.println("////MODIFICADOR ACCESO PUBLIC////");
        Clase1 clase1 = new Clase1();
        System.out.println("clase1 = " + clase1);  
        System.out.println("clase1 = " + clase1.atributoPublico);
        clase1.metodoPublico();
        System.out.println("////MODIFICADOR ACCESO PROTECTED////");
        Clase3 claseHija = new Clase3();
        System.out.println("claseHija = " + claseHija);
    }
}
