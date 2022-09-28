
package Operaciones;

public class Aritmetica { // nomenclatura pascalcase
    //Atributos de la clase
    int a; // valor por default para un int es 0
    int b;
    
    //este método no retorna ningún valor, solo imprime un mensaje en consola.
    //public void (método publico vacío)
    public void sumarNumeros(){ //public void (modificador de acceso) . Nomenclatura camelcase
        int resultado = a + b;
        System.out.println("resultado = " + resultado);
    }
    
    //este método retorna un valor de tipo int
    //public int (método publico de tipo int)
    public int sumarConRetorno(){
        //int resultado = a + b;
        return this.a + this.b;
    } 
    
    public int sumarConArgumentos(int a, int b){
        this.a = a;
        this.b = b;
        //return a + b;
        return this.sumarConRetorno();
    }
}
