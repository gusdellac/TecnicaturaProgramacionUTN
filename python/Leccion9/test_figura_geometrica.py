from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

cuadrado1 = Cuadrado(5, 5, "azul")
print(cuadrado1)
print(f"Cálculo del área del cuadrado: {cuadrado1.calcular_area()}")

# MRO = Method Resolution Order
print(Cuadrado.mro())  # este método nos devuelve el árbol de herencia de la clase

rectangulo1 = Rectangulo(8, 10, "negro")
print(rectangulo1)
print(f"Cálculo del área del cuadrado: {rectangulo1.calcular_area()}")
print(Rectangulo.mro())