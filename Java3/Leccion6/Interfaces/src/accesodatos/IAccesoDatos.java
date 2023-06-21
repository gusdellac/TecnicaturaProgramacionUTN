package accesodatos;

public interface IAccesoDatos {
    int MAX_REGISTRO = 10; //atributo public static final **ver
    
    //metodo abstracto : sin implementacion
    void insertar();
    
    void listar();
    
    void actualizar();
    
    void eliminar();
}
