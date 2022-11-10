
package domain;

//clase final
public final class Persona {
    
    //atributo final
    public final static int CONSTANTE_AQUI = 15; 
    
    private String nombre;

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    
    
            
    //método final
    public final void imprimir(){
        System.out.println("Método para imprimir");
    }
}
