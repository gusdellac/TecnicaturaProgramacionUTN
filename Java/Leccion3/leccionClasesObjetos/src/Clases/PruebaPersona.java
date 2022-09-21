
package Clases;

public class PruebaPersona {  //nomenclatura pascalcase
    public static void main(String[] args) {
        /*
        Persona persona1; //declaramos var persona1 de tipo Persona
        persona1 = new Persona(); /*Instanciamos un objeto de la clase Persona.
        Se realiza la llamada al constructor de la clase Persona
        */
        Persona persona1 = new Persona();
        persona1.nombre = "Gustavo"; //referencia en memoria en valor hexadecimal
        persona1.apellido = "De Llac";
        persona1.obtenerInformacion(); //Llamamos al método obtenerInformacion()
        System.out.println("persona1 = " + persona1);
        
        //Objeto persona2
        Persona persona2 = new Persona();
        persona2.obtenerInformacion(); //devuelve null 
        
        persona2.nombre = "Osvaldo";
        persona2.apellido = "Giordanini";
        persona2.obtenerInformacion();
        
    }
}
