// import Cliente from "./Cliente.js"
const { Cliente } = require("./Cliente.js") // sintaxis modulos common js

let cliente1 = new Cliente("Gustavo", "De Llac", 29, new Date());
console.log(cliente1.toString());