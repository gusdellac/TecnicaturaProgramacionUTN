class Persona:
    contadorPersonas = 0  # atributo de clase

    @classmethod
    def generar_siguiente_valor(cls):
        cls.contadorPersonas += 1
        return cls.contadorPersonas

    def __init__(self, nombre, edad):
        self.idPersona = Persona.generar_siguiente_valor()
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Persona [id: {self.idPersona} = {self.nombre} {self.edad}]"

persona1 = Persona("Gustavo", 28)
print(persona1)
persona2 = Persona("Agustina", 17)
print(persona2)
print(f"Valor contador personas: {Persona.contadorPersonas}")
