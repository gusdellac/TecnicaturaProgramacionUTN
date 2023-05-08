package paquete1;

public class ClaseHija2 extends Clase2{
    public ClaseHija2(){
        super();
        this.atributoDefault = "Modificacion del atributo default 2";
        System.out.println("atributo default = " + this.atributoDefault);
        this.metodoDefault();
        
    }
}
