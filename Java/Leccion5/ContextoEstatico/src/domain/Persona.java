
package domain;

public class Persona {

    private int idPersona;
    private static int contadorPersona; //atributo asociado a la clase no a 
    //los objetos instanciados (static)
    
    private String nombre;
    
    //constructor
    public Persona(String nombre){
        this.nombre = nombre;
        
        //Incremantar el contador por cada objeto nuevo
        Persona.contadorPersona++; //no utilizar el operador this
        
        //asignar un nuevo valor a atributo idPersona
        this.idPersona = Persona.contadorPersona;
        
    }
    
    public static int getContadorPersona() {
        return contadorPersona;
    }

    public static void setContadorPersona(int aContadorPersona) {
        contadorPersona = aContadorPersona;
    }
    
    public int getIdPersona() {
        return this.idPersona;
    }

    public void setIdPersona(int idPersona) {
        this.idPersona = idPersona;
    }

    public String getNombre() {
        return this.nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

//    @Override
//    public String toString() {
//        return "Persona{" + "idPersona=" + idPersona + ", nombre=" + nombre + '}';
//    }
//    
    

    
    
    
}
