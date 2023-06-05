let x = 10; // variable de tipo primitiva
console.log(x.length); //undefined


//Objeto
let persona = {
    nombre: "Carlos",
    apellido: "Gil",
    email: "cgil@gmail.com",
    edad: 30,
    idioma: "ES",
    nombreCompleto: function(){
        return this.nombre+" "+this.apellido;
    },
    get nombreEdad(){ //metodo get
        return "El nombre es: "+this.nombre+", edad: "+this.edad;
    },
    get lang(){
        return this.idioma.toUpperCase();
    },
    set lang(lang){
        this.idioma = lang.toUpperCase();
    }
}

console.log(persona.nombre);
console.log(persona.apellido);
console.log(persona.email);
console.log(persona.edad);
console.log(persona);
console.log(persona.nombreCompleto());

let persona2 = new Object();
persona2.nombre = "Juan";
persona2.direccion = "Salada 14";
persona2.telefono = "5492618282821";
console.log(persona2.telefono);

console.log(persona["apellido"]); // Accedemos como si fuera un arreglo

//for in y accedemos al objeto como si fuera un arreglo
for(propiedad in persona){
    console.log(propiedad);
    console.log(persona[propiedad]);
}

persona.apellido = "Betancud"; //cambiamos dinamicamente un valor del objeto

//Distintas formas de imprimir un objeto
//1 - concatenar el valor de cada propiedad
console.log("Distintas formas de imprimir un objeto: forma 1");
console.log(persona.nombre+", "+persona.apellido);

//2 - a traves del ciclo for in
console.log("Distintas formas de imprimir un objeto: forma 2");
for(nombrePropiedad in persona){
    console.log(persona[nombrePropiedad]);
}

//3 - funcion Object.values()
console.log("Distintas formas de imprimir un objeto: forma 3");
let personaArray = Object.values(persona); //retorna un array con los valores de las propiedades del objeto pasado como argumento
console.log(personaArray);

//4 - metodo JSON.stringify
console.log("Distintas formas de imprimir un objeto: forma 4");
let personaString = JSON.stringify(persona);
console.log(personaString);

//
console.log("Comenzamos a utilizar el metodo get:")
console.log(persona.nombreEdad);


console.log("metodo get y set para idiomas: ");
persona.lang = "en";
console.log(persona.lang);
persona.lang = "es";
console.log(persona.lang);

//constructor de objetos
function Persona3(nombre, apellido, email){
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
    this.nombreCompleto = function(){
        return this.nombre+ " " + this.apellido;
    }
}
let padre = new Persona3("Leo", "Lopez", "lopezl@gmail.com");
padre.nombre = "Luis";
console.log(padre);
console.log(padre.nombreCompleto());

let madre = new Persona3("Laura", "Contrera", "contreral@gmail.com");
console.log(madre);
console.log(madre.nombreCompleto);

//diferentes formas de crear objetos
//caso 1
let miObjeto = new Object();
//caso 2
let miObjeto2 = {};

//caso string 1
let miCadena1 = new String("hola");
//caso string 2
let miCadena2 = "hola";

//caso con numeros 1
let miNumero = new Number(1);
//caso numeros 2
let miNumero2 = 1;

//caso boolean 1
let miBoolean = new Boolean(false);
//caso boolean 2
let miBoolean2 = false;

//caso arreglos 1
let miArreglo1 = new Array();
//caso arreglos 2
let miArreglo2 = [];

//caso function 1
let miFuncion1 = new function(){};
//caso function 2
let miFuncion2 = function(){};


//uso de prototype
Persona3.prototype.telefono = "26154846564";
console.log(padre.telefono);
console.log(madre.telefono);

//uso de call
let persona4 = {
    nombre: "Juan",
    apellido: "Perez",
    nombreCompleto2: function(titulo, telefono){
        return titulo+": "+this.nombre+" "+this.apellido+" "+telefono;
    }
}

let persona5 = {
    nombre: "Carlos",
    apellido: "Lara"
}

//metodo call
console.log(persona4.nombreCompleto2("Lic.", "2646721164"));
console.log(persona4.nombreCompleto2.call(persona5, "Ing.", "5464245465"));

//metodo apply
let arreglo = ["Ing.", "54875164"];
console.log(persona4.nombreCompleto2.apply(persona5, arreglo));