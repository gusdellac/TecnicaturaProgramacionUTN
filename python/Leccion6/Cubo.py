"""
Crear clase Cubo con los atributos: ancho, alto y profundidad.
Con un método calcular_volumen que tendrá la formula:
volumen = ancho * altura * profundidad.
El usuario debe ingresar los valores
"""
class Cubo:
    def __init__(self, ancho, altura, profundidad):
        self.ancho = ancho
        self.altura = altura
        self.profundidad = profundidad

    def calcular_volumen(self):
        return self.ancho * self.altura * self.profundidad

print(">>>>Cálculo volumen de un cubo<<<<")
ancho = float(input("Digite ancho del cubo: "))
altura = float(input("Digite altura del cubo: "))
profundidad = float(input("Digite profundidad del cubo: "))
cubo1 = Cubo(ancho, altura, profundidad)
print(f"El volumen del cubo es: {cubo1.calcular_volumen()}")