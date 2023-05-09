package test;

import domain.Empleado;
import domain.Gerente;

public class TestInstanceOf {
    public static void main(String[] args) {
        Empleado empleado1 = new Empleado("Juan", 10000);
        determinarTipo(empleado1);
        empleado1 = new Gerente("Jose", 10000, "Sistemas");
        determinarTipo(empleado1);
 
    }
    
    public static void determinarTipo(Empleado empleado){
        if(empleado instanceof Gerente){
            System.out.println("Es de tipo Gerente");
            
            //Casteo de la variable empleado - forma 1
//            ((Gerente) empleado).getDepartamento();
            
            //Casteo de la variable empleado - forma 2
            Gerente gerente = (Gerente) empleado;
            System.out.println("gerente = " + gerente.getDepartamento());
        }
        else if(empleado instanceof Empleado){
            System.out.println("Es de tipo Empleado");
            
            //Esto genera una exception de tipo cast debido a que se intenta
            //convertir la variable de un tipo de clase padre a un 
            //tipo de clase hija
            
//            Gerente gerente = (Gerente) empleado;
//            String departamento = gerente.getDepartamento();
//            System.out.println("departamento = " + departamento);
        }
        if(empleado instanceof Object){
            System.out.println("Es de tipo Object");
        }
    }
}
