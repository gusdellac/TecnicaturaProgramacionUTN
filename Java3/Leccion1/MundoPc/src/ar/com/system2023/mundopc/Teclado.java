
package ar.com.system2023.mundopc;

public class Teclado extends DispositivoEntrada {
    private final int idTeclado;
    private static int ocntadorTeclados;

    public Teclado(String tipoEntrada, String marca) {
        super(tipoEntrada, marca);
        this.idTeclado = ++Teclado.ocntadorTeclados;
    }

    @Override
    public String toString() {
        return "Teclado{" + "idTeclado=" + idTeclado + ", " + super.toString() + "}";
    }

} 
