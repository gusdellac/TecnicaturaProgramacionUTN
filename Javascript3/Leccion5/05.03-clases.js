class Persona {
    constructor (nombre, apellido) {
        this._nombre = nombre;
        this._apellido = apellido;
    }

    get nombre(){
        return this._nombre;
    }

    set nombre(nombre){
        this._nombre = nombre;
    }

    get apellido(){
        return this._apellido;
    }

    set apellido(apellido){
        this._apellido = apellido;
    }

    nombreCompleto(){
        return this._nombre + " " + this._apellido;
    }

    //sobreescribiendo el metodo de la clase padre Object
    toString(){
        // se aplica polimorfismo : multiples formas en tiempo de ejecucion
        // el metodo que se ejecuta depende de la referencia a la que el objeto apunta, es decir
        // a que clase pertenece el objeto instanciado
        return this.nombreCompleto();
    }
}

let persona1 = new Persona("Martin", "Perez");
console.log(`Persona1 = Nombre: ${persona1.nombre} - Apellido: ${persona1.apellido}`);
persona1.nombre = "Juan Carlos";
persona1.apellido = "Rios";
console.log(`Persona1 = Nombre: ${persona1.nombre} - Apellido: ${persona1.apellido}`);

console.log("*************************************")

let persona2 = new Persona("Carlos", "Lara");
console.log(`Persona2 = Nombre: ${persona2.nombre} - Apellido: ${persona2.apellido}`);
persona2.nombre = "Maria";
persona2.apellido = "Rodriguez";
console.log(`Persona2 = Nombre: ${persona2.nombre} - Apellido: ${persona2.apellido}`);

//* No se puede instanciar un objeto previo a la inicializacion de la clase. No aplica el concepto de hoisting */


//* Herencia */

class Empleado extends Persona {
    constructor (nombre, apellido, departamento){
        super(nombre, apellido);
        this._departamento = departamento;
    }

    get departamento(){
        return this._departamento;
    }

    set departamento(departamento){
        this._departamento = departamento;
    }

    //Sobreescritura
    nombreCompleto(){
        return super.nombreCompleto() + ", " + this._departamento;  
    }
}

console.log("*************************************")

let empleado1 = new Empleado("Gustavo", "De Llac", "Logistica");
console.log(`empleado1 = Nombre: ${empleado1.nombre} - Apellido: ${empleado1.apellido} - Departamento: ${empleado1.departamento}`);
console.log(empleado1.nombreCompleto());

// Object.prototype.toString //Esta es la manera de acceder a atributos y metodos de manera dinamica
console.log(empleado1.toString()); 
console.log(persona1.toString());

