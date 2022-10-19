
class Persona2:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre  # atributo encapsulado
        self._apellido = apellido  # atributo encapsulado
        self._edad = edad  # atributo encapsulado
    def mostrar_detalles(self):
        # print(f"Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}")
        return self.nombre, self.apellido, self.edad

    @property  # decorador     # (sintaxis correcta de getter)
    def nombre(self):  # método getter
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):  # método setter   # (sintaxis correcta de setter)
        self._nombre = nombre

    @property  # decorador
    def apellido(self):  # método getter
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):  # método setter
        self._apellido = apellido

    @property  # decorador
    def edad(self):  # método getter
        return self._edad

    # método destructor de objeto (si no se hace explícito se ejecuta implícitamente, recolector de basura)
    def __del__(self):
        print(f"Persona2: {self._nombre} {self._apellido} {self._edad}")

if __name__ == "__main__":  # si el archivo desde el que estamos ejecutando corresponde a la ubicación de la clase
    # utilizada, ejecutará el código, es decir, que corresponde al main
    persona1 = Persona2("Gustavo", "De Llac", 28)
    print(persona1.nombre)  # llamamos al método getter
    persona1.nombre = "Juan Pedro"  #Llamamos al método setter
    print(persona1.nombre)  # llamamos al método getter
    print(persona1.mostrar_detalles())  # método mostrar_detalles

    # atributo read-only sería la edad porque no tiene el método set
    print(persona1.edad)


    # Crear tres objetos más utilizando los métodos getter and setter
    # para modificar, y mostrar los cambios con el método mostrar_detalles()

    # objeto 1
    print("Objeto 1")
    persona2 = Persona2("Diego", "De Llac", 31)
    print(persona2.mostrar_detalles())
    persona2.nombre = "Alberto"
    persona2.apellido = "Guillen"
    print(persona2.mostrar_detalles())

    # objeto 2
    print("Objeto 2")
    persona3 = Persona2("Agustina", "De Llac", 17)
    print(persona3.mostrar_detalles())
    persona3.nombre = "Arduizur"
    persona3.apellido = "Glickman"
    print(persona3.mostrar_detalles())

    # objeto 3
    print("Objeto 3")
    persona4 = Persona2("Cristina", "Barro", 51)
    print(persona4.mostrar_detalles())
    persona4.nombre = "Maria"
    persona4.apellido = "Quiroga"
    print(persona4.mostrar_detalles())



    print(__name__)  # nos indica que el archivo desde el que estamos ejecutando el código es el main (__main__)

