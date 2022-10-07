
package PasoPorValor;

public class PasoPorValor {
    public static void main(String[] args) {
        var valorX = 20;
        System.out.println("valorX = " + valorX);
        cambioValor(valorX); //solo le enviamos una copia, no envía la referencia
        //de la memoria stack en donde se almacena la variable local valorX
        //es decir , el método que la recibe como parámetro no puede modificar
        //el valor de la variable que recibe
        System.out.println("valorX = " + valorX);
    }
    
    public static void cambioValor(int arg1){
        System.out.println("arg1 = " + arg1);
        //arg1 = 25; aqui podemos modificar el valor pero de arg1 no de la variable
        //recibida valorX
    }
    
}
