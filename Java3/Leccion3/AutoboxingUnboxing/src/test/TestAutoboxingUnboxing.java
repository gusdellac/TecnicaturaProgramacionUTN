package test;

public class TestAutoboxingUnboxing {
    public static void main(String[] args) {
        //Clases envolventes o Wrapper
        /*
            Clases envolventes de tipos primitivos
            int = la clase envolvente es Integer
            **La clase envolvente de cada tipo de dato es el nombre del tipo
            pero comienza con mayuscula.
        */
        
        int enteroPrim = 10; //tipo primitivo
        System.out.println("enteroPrim = " + enteroPrim);
        Integer entero = 10; //tipo objecto con la clase Integer
        
        
        System.out.println("entero = " + entero.doubleValue()); //autoboxing,
        //convertimos de objeto a primitivo double
        
        int entero2 = entero; //unboxing, convertimos de objeto a primitivo int
        
        System.out.println("entero2 = " + entero2);
        
        
    }
}
