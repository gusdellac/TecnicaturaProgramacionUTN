miFuncion(8, 2); // llamamos a la funcion antes de declararla (hoisting**)

function miFuncion(a, b){
    //console.log("Sumamos: "+ (a + b)); 
    return a + b;
}

miFuncion(5, 4); // llamada a la funcion

let resultado = miFuncion(6, 7);
console.log(resultado);

// ** Hoisting es un término para describir que las declaraciones 
// ** de variables y funciones son desplazadas a la parte superior 
// **del scope más cercano, scope global o de función

//Declaramos una funcion de tipo expresion o anonima
let x = function(a, b){ return a +b};
resultado = x(5, 6);
console.log(resultado);

//Funciones de tipo self y invoking
(function(a, b){
    console.log("Ejecutando la funcion: "+ (a + b));
})(9, 6); // funcion autoejecutable

console.log(typeof miFuncionDos);

function miFuncionDos(a, b){
    console.log(arguments); //imprimimos los argumentos que recibe la funcion. arguments es una propiedad del objeto function, que a su vez
    //almacena un array
    console.log(typeof arguments);
    console.log(arguments.length); // imprimimos la longitud del array
}
miFuncionDos(5, 7);

//toString
var miFuncionTexto = miFuncionDos.toString(); //convertimos la funcion a text y la almacenamos en la var
console.log(miFuncionTexto);

//funciones flecha o arrow functions
const sumarFuncionFlecha = (a, b) => a + b;
resultado = sumarFuncionFlecha(3, 7); //asignamos el valor retornado a la variable resultado 
console.log(resultado);

//Funcion tipo expresion
let sumar = function(a, b){
    console.log(arguments[0]);
    console.log(arguments[1]);
    return a + b;
}
resultado = sumar(3, 5);
console.log(resultado);

//Sumar todos los argumentos 
let respuesta = sumarTodo(5, 4, 13, 10, 9); //llamada a la funcion antes de declararla **hoisting
console.log(respuesta);
function sumarTodo(){
    let suma = 0;
    for (let i = 0; i < arguments.length; i++) {
        suma += arguments[i];
    }
    return suma;
}


// paso por valor
let k = 10;
function cambiarValor(a){
    a = 20;
}
cambiarValor(k);
console.log(k);


//paso por referencia
const persona = {
    nombre: "Juan",
    apellido: "Lopez"
}

console.log(persona);
function cambiarValorObjeto(p1){ //recibimos como argumento la referencia en memoria del objeto persona
    p1.nombre = "Gustavo"; //modificamos valor propiedad nombre
    p1.apellido = "De Llac"; //modificamos valor propiedad apellido
}

cambiarValorObjeto(persona); //pasamos la referencia en memoria (valor hexadecimal) del objeto persona
console.log(persona);

