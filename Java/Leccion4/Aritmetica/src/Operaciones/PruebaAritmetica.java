
package Operaciones;

public class PruebaAritmetica {
    public static void main(String[] args) {
        Aritmetica aritmetica1 = new Aritmetica(); /*cuando colocamos los paréntesis
        después del nombre de la clase "Aritmetica()" lo que hacemos es llamar al constructor
        de la clase y reservar espacio en memoria para instanciar el objeto*/
        aritmetica1.a = 3;
        aritmetica1.b = 7;
        aritmetica1.sumarNumeros();
        
        int resultado = aritmetica1.sumarConRetorno();
        System.out.println("resultado = " + resultado);
        
        resultado = aritmetica1.sumarConArgumentos(12, 26);
        System.out.println("resultado usando argumentos = " + resultado);
    }
}
