
package excepciones;

//public class OperacionExcepcion extends Exception{
//    //Constructor
//    public OperacionExcepcion(String mensaje){
//        super(mensaje);
//    }
//}

public class OperacionExcepcion extends RuntimeException{
    //Constructor
    public OperacionExcepcion(String mensaje){
        super(mensaje);
    }
}
