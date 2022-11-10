
package domain;

public class Empleado extends Persona{
    private final int idEmpleado;
    private double sueldo;
    private static int contadorEmpleados;
    
    public Empleado(){ //constructor 1
        this.idEmpleado = ++Empleado.contadorEmpleados;
    }
    public Empleado(String nombre, double sueldo) { //constructor 2
//        super(nombre);
        this(); // Estamos llamando desde aquí al constructor vacío
        this.nombre = nombre; //podemos acceder directamente a los atributos
        //de la clase padre porque tienen el modificador de acceso protected
        this.sueldo = sueldo;
    }

    public int getIdEmpleado() {
        return idEmpleado;
    }

    public double getSueldo() {
        return sueldo;
    }

    public void setSueldo(double sueldo) {
        this.sueldo = sueldo;
    }

    @Override
    public String toString() { /*usamos clase StringBuilder*/
        StringBuilder sb = new StringBuilder();
        sb.append("Empleado{idEmpleado=").append(idEmpleado);
        sb.append(", sueldo=").append(sueldo);
        sb.append(", ").append(super.toString());
        sb.append('}');
        return sb.toString();
    }
    
    
    
    
    
    
    
}
