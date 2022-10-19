class Encapsulamiento:
    def __init__(self, nombre, apellido, dni):
        self._nombre = nombre
        self.__apellido = apellido
        self.dni = dni

    def getApellido(self):  #getter __apellido (sintaxis incorrecta)
        return self.__apellido

    def setApellido(self, nombre):  # setter __apellido (sintaxis incorrecta)
        self._nombre = nombre

    def mostrarDetalle(self):
        print(self._nombre, self.__apellido, self.dni)

encapsulamiento1 = Encapsulamiento("Gustavo", "De Llac", 38208173)  # asignamos valores a los atributos privados
# desde el constructor
encapsulamiento1.mostrarDetalle()

encapsulamiento1._nombre = "Ariel"  # Si intentamos modificar desde fuera de la clase un atributo privado identificado
# con "_" python no nos mostrara la variable en cuestión. Si podremos escribirla manualmente como en el ejemplo, y
# lograr modificar su valor
encapsulamiento1.mostrarDetalle()

encapsulamiento1.__apellido = "Barro"  # Si intentamos modificar desde fuera de la clase un atributo privado
# identificado con "__" python no nos mostrara la variable en cuestión ni nos dejará modificarla manualmente.
# podemos decir que éste si es un modificador de acceso.
encapsulamiento1.mostrarDetalle()

# getter
apellido = encapsulamiento1.getApellido()
print(apellido)

# setter
encapsulamiento1.setApellido("Ricardo")
encapsulamiento1.mostrarDetalle()