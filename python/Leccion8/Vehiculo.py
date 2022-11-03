class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f"Vehiculo : [ color: {self.color}, ruedas: {self.ruedas}]"

class Auto(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return f"Auto: [ velocidad: {self.velocidad}] {super().__str__()}"


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
    def __str__(self):
        return f" Bicicleta: [{self.tipo}] {super().__str__()}"


vehiculo1 = Vehiculo("Negro", 3)
print(f"Objeto vehiculo1: {vehiculo1}")

auto1 = Auto("Rojo", 4, "200km/h")
print(f"Objeto auto1: {auto1}")

# bicicleta1 = Bicicleta("Azul", 2, "Mountainbike")
# print(f"Objeto bicicleta1: {bicicleta1}")