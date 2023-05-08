package paquete2;

/*modif acceso private. Los elementos con este modif de acceso solo pueden
ser accedidos desde la misma clase*/

public class Clase4 {
    private String atributoPrivate = "atributo private";
    
    //constructor private
    private Clase4(){
        System.out.println("Constructor private");
    }
    
    //Creamos un constructor public para poder crear objetos
    public Clase4(String argumento){
        this(); //llamamos constructor vacío de tipo private
        System.out.println("Constructor public");
    }
    
    //Metodo private
    private void metodoPrivate(){
        System.out.println("Metodo private");
    }
    
    //metodo public
    public void metodoPublic(){
        metodoPrivate(); //llamamos a metodo private
    }
    
    //getter and setter
    public String getAtributoPrivate() {
        return atributoPrivate;
    }

    public void setAtributoPrivate(String atributoPrivate) {
        this.atributoPrivate = atributoPrivate;
    }
    
    
}
