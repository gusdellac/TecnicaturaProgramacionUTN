package paquete1;

/*modif acceso default o package. Los elementos con este modif de acceso
solo son accesibles desde el mismo paquete*/
class Clase2{
    String atributoDefault = "Valor del atributo default";
    
    Clase2(){
        System.out.println("Constructor default");
        this.atributoDefault = "Modificacion del atributo default 1";
        System.out.println("atributo default = " + this.atributoDefault);
        this.metodoDefault();
    }
    
    void metodoDefault(){
        System.out.println("Metodo default");
    }
}
