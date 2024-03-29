class Persona {

    //atributo static : solo se relaciona con la clase
    static contadorPersonas = 0;

    static get MAX_OBJ(){ //este metodo simula una constante
        return 5;
    }

    //atributo no static : solo se relaciona con las instancias de la clase
    //email = "valor default";

    constructor (nombre, apellido) {
        if(Persona.contadorPersonas < Persona.MAX_OBJ){
            this._nombre = nombre;
            this._apellido = apellido;
            this.idPersona == ++Persona.contadorPersonas;
        }
        else{
            console.log("Se ha superado el maximo de objetos permitidos");
        }
        //console.log("Se incrementa el contador: "+Persona.contadorObjetosPersona);
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
        return this.idPersona+" "+this._nombre + " " + this._apellido;
    }

    //sobreescribiendo el metodo de la clase padre Object
    toString(){
        // se aplica polimorfismo : multiples formas en tiempo de ejecucion
        // el metodo que se ejecuta depende de la referencia a la que el objeto apunta, es decir
        // a que clase pertenece el objeto instanciado
        return this.nombreCompleto();
    }

    //metodo static: solo se relaciona con la clase
    static saludar(){ 
        console.log("Saludo desde metodo static de la clase Persona");
    }

    static saludar2(persona){
        console.log(persona.nombre+ " "+persona.apellido);
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


// persona1.saludar(); // no se puede ejecutar un metodo static desde una instancia de la clase
Persona.saludar(); // un metodo static puede ser ejecutado solo desde la clase, este metodo esta relacionado a la clase y no a sus instancias 
Persona.saludar2(persona1);

// ejecucion metodos static desde clase hija Empleado
Empleado.saludar();
Empleado.saludar2(empleado1);

// console.log(persona1.contadorObjetosPersona);
//console.log(Persona.contadorObjetosPersona);
//console.log(Empleado.contadorObjetosPersona);

// console.log(Persona.email);
//console.log(persona1.email);
//console.log(empleado1.email);

console.log(persona1.toString());
console.log(persona2.toString());
console.log(empleado1.toString());
console.log(Persona.contadorPersonas);
let persona3 = new Persona("Carla", "Pertosi");
console.log(persona3.toString());
console.log(Persona.contadorPersonas);

console.log(Persona.MAX_OBJ);
//Persona.MAX_OBJ = 10; //no se puede modificar

let persona4 = new Persona("Franco", "Diaz");
console.log(persona4.toString());
let persona5 = new Persona("Liliana", "Paz");
console.log(persona5.toString());



