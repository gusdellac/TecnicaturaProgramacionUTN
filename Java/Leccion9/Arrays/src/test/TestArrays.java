
package test;

public class TestArrays {
    public static void main(String[] args) {
        int edades[] = new int [3]; /*del lado izquierdo declaramos la variable
        que será un array y del lado derecho instanciamos un objeto de tipo
        object*/
        System.out.println("edades posición en memoria del objeto = " + edades);
        
        edades[0] = 17;
        System.out.println("edades[0]= " + edades[0]);
        edades[1] = 5;
        edades[2] = 7;
        System.out.println("edades[1]= " + edades[1]);
        System.out.println("edades[2]=" + edades[2]);
          
        //edades[3] = 7; //Fuera de rango, error en tiempo de ejecución
        System.out.println(edades.length);
        
        for(int i = 0; i < edades.length; i++){
            System.out.println("edades["+i+"] = "+edades[i]);
        }
    }
}
