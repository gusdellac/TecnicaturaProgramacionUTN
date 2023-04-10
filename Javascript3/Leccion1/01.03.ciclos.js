// while
let contador = 0;
while(contador < 3){
    console.log(contador);
    contador++;
}
console.log("Fin ciclo while");

//do while
let conteo = 0;
do {
    console.log(conteo);
    conteo++;
} while(conteo < 3);
console.log("Fin del ciclo do while");

// for
for (let contando = 0; contando < 3; contando++) {
    console.log(contando);
}
console.log("Fin del ciclo for");

// Palabra reservada break
for (let contando = 0; contando <= 10; contando++) {
    if (contando % 2 == 0) {
        console.log(contando);
        break;
    }
}
console.log("Termina el ciclo al encontrar el primer número par");

// Palabra reservada continue
for (let contando = 0; contando <= 10; contando++) {
    if (contando % 2 != 0) {
        continue; // pasa a la siguiente iteracion 
    }
    console.log(contando);
}
console.log("Termina el ciclo e imprime los numeros pares");


// Etiqueta labels
console.log("Etiquetas labels");

// Palabra reservada break + labels
inicio:
for (let contando = 0; contando <= 10; contando++) {
    if (contando % 2 == 0) {
        console.log(contando);
        break inicio;
    }
}
console.log("Termina el ciclo al encontrar el primer número par");

// Palabra reservada continue + labels

inicio:
for (let contando = 0; contando <= 10; contando++) {
    if (contando % 2 != 0) {
        continue inicio; // pasa a la siguiente iteracion 
    }
    console.log(contando);
}
console.log("Termina el ciclo e imprime los numeros pares");