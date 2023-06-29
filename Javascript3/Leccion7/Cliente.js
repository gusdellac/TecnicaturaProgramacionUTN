const { Persona } = require("./Persona.js"); // sintaxis modulos common js

class Cliente extends Persona {

    static contadorClientes = 0;

    constructor(nombre, apellido, edad, fecharegistro){
        super(nombre, apellido, edad);
        this._idCliente = ++Cliente.contadorClientes;
        this._fecharegistro = fecharegistro;
    }

    get idCliente(){
        return this._idCliente;
    }

    get fecharegistro(){
        return this._fecharegistro;
    }

    set fecharegistro(fecharegistro){
        this._fecharegistro = fecharegistro;
    }

    toString(){
        return super.toString()+" "+this._idCliente+" "+this._fecharegistro;
    }
}

// sintaxis modulos common js
module.exports = {
    Cliente : Cliente
}