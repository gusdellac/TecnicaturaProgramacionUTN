
package CiclosJava;

public class EjercicioCiclos {
    public static void main(String[] args) {
        
        //loop while (mientras)
        System.out.println("LOOP WHILE: ");
        var conteo = 0; //inferencia de tipo
        while (conteo < 7){
            System.out.println("conteo = " + conteo);
            conteo++; //incremento variable
        }
        
        //loop do while (hasta que)
        System.out.println("LOOP DO WHILE: ");
        var contador = 0;
        do{
            System.out.println("contador = " + contador);
            contador++;
        }while(contador <7);
        
        //loop for (para)
        System.out.println("LOOP FOR: ");
        for(var iterador = 0;iterador < 7; iterador++){
            System.out.println("iterador = " + iterador);
        }
    }
    
}
