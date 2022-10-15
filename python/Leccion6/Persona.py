class Persona:  # Creamos una clase
    def __init__(self, nombre, apellido, dni, edad, *args, **kwargs):
        # Se lo llama método Init Dunder (constructor). Entre los paréntesis
        # debemos colocar la palabra reservada self que viene por defecto y luego los argumentos que
        # recibirá el constructor

        # Atributos de método
        self.nombre = nombre  # self hace referencia a una determinada instancia de la clase (this)
        self.apellido = apellido
        self._dni = dni  # atributo encapsulado (privado). Podemos accederlo sólo desde el constructor ***
        self.edad = edad
        self.args = args
        self.kwargs = kwargs

    def mostrar_detalle(self):  # método de clase, por defecto los métodos dentro de una clase generan la palabra self
        print(f"La clase Persona tiene los siguientes datos: {self.nombre} {self.apellido} {self._dni} {self.edad}, "
              f"la direccion es: {self.args}, "
              f"los datos importantes son: {self.kwargs}")
        # utilizamos los atributos declarados en el constructor

persona1 = Persona("Gustavo", "De Llac", 25612458, 28)  # como indicamos argumentos al constructor debemos
# pasar los parámetros

print(persona1)
# al instanciar la clase
print(f"El objeto1 de la clase persona: Nombre: {persona1.nombre}, Apellido: {persona1.apellido}, "
      f"Edad: {persona1.edad}")

persona2 = Persona("Agustina", "De Llac", 25612458, 17)
print(f"El objeto2 de la clase persona: Nombre: {persona2.nombre}, Apellido: {persona2.apellido}, "
      f"Edad: {persona2.edad}")

# Modificar atributos de un objeto
persona1.nombre = "Arduizur"
persona1.apellido = "Glickman"
persona1.edad = 19
print(f"El objeto1 de la clase persona modificado: Nombre: {persona1.nombre}, Apellido: {persona1.apellido}, "
      f"Edad: {persona1.edad}")

persona2.nombre = "Diego"
persona2.apellido = "De Llac"
persona2.edad = 31
print(f"El objeto2 de la clase persona modificado: Nombre: {persona2.nombre}, Apellido: {persona2.apellido}, "
      f"Edad: {persona2.edad}")

print("Utilizamos el método mostra_detalle() de la clase Persona:")
persona1.mostrar_detalle()  # La referencia en este caso se pasa de forma automática
persona2.mostrar_detalle()


# Persona.mostrar_detalle(persona1)  # Debemos pasarle una referencia para el self o dará error

# Creamos una atributo para objeto persona1
persona1.telefono = "456554816"
print(f"Este es el teléfono de {persona1.nombre}: {persona1.telefono}")  # Creamos un atributo de un objeto

# print(persona2.telefono) el objeto persona2 no tiene este atributo

persona3 = Persona("Rogelio", "Romero", 25612458, 22, "Teléfono", "261454684", "Calle Lopez", 823, "Manazana", 77,
                   "Casa", 18,
                   Altura=1.83, Peso=105, CFavorito="Azul", Auto="Citroen", Modelo=2021)
persona3.mostrar_detalle()

# *** _dni es un atributo encapsulado. La encapsulación en python es similar a javascript, ya que no existe una
# encapsulación real sino que se la trabaja como convención. Para esto utilizaremos el "_" antes del nombre de la
# variable.
# podremos setearle un valor al atributo encapsulado através del constructor y podremos obtener su valor dentro
# de la clase