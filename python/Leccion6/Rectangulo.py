"""
Crear una clase llamada Rectangulo, debe tener 2 atributos: altura y base, el nombre del
método será calcular_area utilizando la formula:
area = base * altura. Pero la base y la altura deben ser ingresadas por el usuario
y los objetos deben ser tres.
"""
class Rectangulo:
    def __init__(self, altura, base):
        self.altura = altura
        self.base = base

    def calcular_area(self):
        return self.altura * self.base

print(">>>>Cálculo del área de un rectángulo<<<<")
altura = float(input("Digite altura del rectángulo: "))
base = float(input("Digite base del rectángulo: "))
rectangulo1 = Rectangulo(altura, base)
print(f"El área del rectángulo es: {rectangulo1.calcular_area()}")