class Persona:  # Creamos una clase
    def __init__(self, nombre, apellido, edad):  # Se lo llama método Init Dunder (constructor). Entre los paréntesis
        # debemos colocar la palabra reservada self que viene por defecto y luego los argumentos que recibirá el
        # constructor

        # Atributos de método
        self.nombre = nombre  # self hace referencia a una determinada instancia de la clase (this)
        self.apellido = apellido
        self.edad = edad

    def mostrar_detalle(self):  # método de clase, por defecto los métodos dentro de una clase generan la palabra self
        print(f"Persona: {self.nombre} {self.apellido} {self.edad}")  # utilizamos los atributos declarados en el
        # constructor

persona1 = Persona("Gustavo", "De Llac", 28)  # como indicamos argumentos al constructor debemos pasar los parámetros
print(persona1)
# al instanciar la clase
print(f"El objeto1 de la clase persona: Nombre: {persona1.nombre}, Apellido: {persona1.apellido}, "
      f"Edad: {persona1.edad}")

persona2 = Persona("Agustina", "De Llac", 17)
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
persona1.mostrar_detalle()
persona2.mostrar_detalle()

