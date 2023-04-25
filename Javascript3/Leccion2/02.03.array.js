//let autos = new Array("Ferrari", "Renault", "BMW"); sintaxis antigua
const autos = ["Ferrari", "Renault", "BMW"];
console.log(autos); 
console.log(autos[0]);
console.log(autos[2]);

for (let i = 0; i < autos.length; i++) {
    console.log(i + " : " + autos[i]);    
}

//Modificamos elementos del array
autos[1] = "Volvo";
console.log(autos[1]);

//Agregamos nuevos valores al array
autos.push("Audi"); // Agregamos el elemento al final del array
console.log(autos);

// Otras formas
autos[autos.length] = "Porsche";
console.log(autos);

//Tercer forma
autos[6] = "Renault"; // si el array no cuenta con elementos en las posiciones anteriores quedaran posiciones vacías
console.log(autos);

// Como saber si es un Array
console.log(Array.isArray(autos)); // Retorna un booleano

console.log(autos instanceof Array); // Retorna un booleano