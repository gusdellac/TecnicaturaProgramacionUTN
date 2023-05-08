package paquete1;

/*modif acceso public permite que la clase, atributo, constructor o metodo,
pueda ser utilizado desde cualquier parte del proyecto, ya sea en el mismo 
paquete o en un paquete externo*/

public class Clase1 {
    public String atributoPublico = "Valor atributo publico";
    protected String atributoProtected = "valor atributo protected";
    
    public Clase1(){
        System.out.println("Constructor public");
    }
    
    protected Clase1(String atributoProtected){
        System.out.println("Constructor protected");
    }
    
    public void metodoPublico(){
        System.out.println("Metodo public");
    }
    
    protected void metodoProtected(){
        System.out.println("Metodo protected");
    }
}
