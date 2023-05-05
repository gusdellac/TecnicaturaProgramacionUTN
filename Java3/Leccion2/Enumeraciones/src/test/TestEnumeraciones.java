package test;

import enumeraciones.Continentes;
import enumeraciones.Dias;

public class TestEnumeraciones {
    public static void main(String[] args) {
        System.out.println("Dia 1: "+Dias.LUNES);
        indicarDiaSemana(Dias.MIERCOLES); // Las enumeraciones se tratan como cadenas
        //Ahora no se deben utilizar comillas, se accede a traves del operador de punto
        
        System.out.println("Continente N°4: "+Continentes.AMERICA);
        System.out.println("N° de paises en el 4to continente: "
                +Continentes.AMERICA.getPaises());
        System.out.println("N° de habitantes en el 4to continente: "
                +Continentes.AMERICA.getHabitantes());
    }
    
    private static void indicarDiaSemana(Dias dias){
        switch (dias){
            case LUNES:
                System.out.println("Primer dia de la semana");
                break;
            case MARTES:
                System.out.println("Segundo dia de la semana");
                break;
            case MIERCOLES:
                System.out.println("Tercer dia de la semana");
                break;
            case JUEVES:
                System.out.println("Cuarto dia de la semana");
                break;
            case VIERNES:
                System.out.println("Quinto dia de la semana");
                break;
            case SABADO:
                System.out.println("Sexto dia de la semana");
                break;
            case DOMINGO:
                System.out.println("Ultimo dia de la semana");
                break;
            default:
                System.out.println("Dato incorrecto");
        }
    }
}
