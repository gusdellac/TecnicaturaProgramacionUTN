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
}

console.log("*************************************")

let empleado1 = new Empleado("Gustavo", "De Llac", "Logistica");
console.log(`empleado1 = Nombre: ${empleado1.nombre} - Apellido: ${empleado1.apellido} - Departamento: ${empleado1.departamento}`);