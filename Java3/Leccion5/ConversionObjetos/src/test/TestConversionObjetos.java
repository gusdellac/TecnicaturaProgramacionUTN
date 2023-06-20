package test;

import domain.*;


public class TestConversionObjetos {
    public static void main(String[] args) {
        Empleado empleado;
        empleado = new Escritor("Juan", 5000, TipoEscritura.CLASICO);
        System.out.println("empleado="+ empleado);
        System.out.println(empleado.obtenerDetalles()); //si queremos acceder a
        //metodos Escritor
        
        //Downcasting : convertimos un objeto de tipo clase padre a un objeto
        //de tipo clase hija
        
        //1ra forma
        //((Escritor)empleado).getTipoEscritura(); //casteamos la variable que 
        //almacena un objeto de tipo empleado y la convertimos a tipo escritor,
        //de esta forma podemos utilizar el metodo getTipoEscritura()
        
        //2da forma
        Escritor escritor = (Escritor)empleado;
        System.out.println(escritor.getTipoEscritura());
        
        //Upcasting : asignamos un objeto de tipo escritor a una variable de
        //tipo empleado, de esta forma la variable de tipo empleado almacena
        //un objeto de tipo escritor
        
        Empleado empleado2 = escritor;
        System.out.println(empleado2.obtenerDetalles());
    }
}
