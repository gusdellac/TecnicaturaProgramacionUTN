class Persona:  # Esta clase hereda de la clase Object
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    @property  # getter _nombre
    def nombre(self):
        return self._nombre

    @nombre.setter  # setter _nombre
    def nombre(self, nombre):
        self._nombre = nombre

    @property  # getter _edad
    def edad(self):
        return self._edad

    @edad.setter  # setter _edad
    def edad(self, edad):
        self._edad = edad

    def __str__(self):  # Override (sobreescribe el método __str__de la clase Object)
        # este método es el toString() de Java
        return f"Persona: [nombre: {self.nombre}, edad: {self.edad}]"


class Empleado(Persona):  # Esta clase es hija de la clase persona
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)  # llamamos al constructor de la clase padre usando super()
        self._sueldo = sueldo

    @property  # getter _sueldo
    def sueldo(self):
        return self._sueldo

    @sueldo.setter  # setter _sueldo
    def sueldo(self, sueldo):
        self._sueldo = sueldo

    def __str__(self):  # override método __str__
        return f"Empleado: [ Sueldo: {self._sueldo}] {super().__str__()}"  # interpolamos el atributo _sueldo
        # y la llamada al método __str__ de la clase padre

empleado1 = Empleado("Gustavo", 28, 75000)
print(empleado1.nombre, empleado1.edad, empleado1.sueldo)

# Tarea: encapsular los atributos y agregar los métodos getters and setters
# Crear otro objeto, pasar los datos para nombre, edad y sueldo
# Mostrar estos datos, luego modificar y mostrar nuevamente

empleado2 = Empleado("Diego", 31, 80000)
print(empleado2.nombre, empleado2.edad, empleado2.sueldo)
empleado2.nombre = "Ricardo"
empleado2.edad = 25
empleado2.sueldo = 50000
print(empleado2.nombre, empleado2.edad, empleado2.sueldo)
