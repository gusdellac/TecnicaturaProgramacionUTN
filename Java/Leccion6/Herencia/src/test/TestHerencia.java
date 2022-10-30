
package test;

import domain.Empleado;
import domain.Cliente;
import java.util.Date;

public class TestHerencia {
    public static void main(String[] args) {
        Empleado empleado1 = new Empleado("Gustavo De Llac", 250000);
        System.out.println("empleado1 = " + empleado1);
        
        Date fecha1 = new Date();
        Cliente cliente1 = new Cliente(fecha1, true, "Gustavo De Llac"
                , 'M', 28, "Necochea 312");
        System.out.println("cliente1 = " + cliente1);
        
    }
}
