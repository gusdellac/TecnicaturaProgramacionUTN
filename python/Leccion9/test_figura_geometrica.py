from Cuadrado import Cuadrado
from FiguraGeometrica import FiguraGeometrica
from Rectangulo import Rectangulo

print("Creación del objeto clase Cuadrado".center(50, "_"))
cuadrado1 = Cuadrado(5, 5, "azul")
print(cuadrado1)
print(f"Cálculo del área del cuadrado: {cuadrado1.calcular_area()}")

# MRO = Method Resolution Order
print(Cuadrado.mro())  # este método nos devuelve el árbol de herencia de la clase

print("Creación del objeto clase Rectangulo".center(50, "_"))
rectangulo1 = Rectangulo(8, 9, "negro")
print(rectangulo1)
print(f"Cálculo del área del rectángulo: {rectangulo1.calcular_area()}")
print(Rectangulo.mro())

# figura1 = FiguraGeometrica() No se puede instanciar, es una clase abstracta

