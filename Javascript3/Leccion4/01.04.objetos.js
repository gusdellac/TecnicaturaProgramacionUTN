let x = 10; // variable de tipo primitiva
console.log(x.length); //undefined


//Objeto
let persona = {
    nombre: "Carlos",
    apellido: "Gil",
    email: "cgil@gmail.com",
    edad: 30,
    nombreCompleto: function(){
        return this.nombre+" "+this.apellido;
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

