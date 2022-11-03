from Color import Color
from FiguraGeometrica import FiguraGeometrica


class Cuadrado(FiguraGeometrica, Color):  # clase Cuadrado extiende de FiguraGeometrica y Color (herencia múltiple)
    def __init__(self, alto, ancho, color):
        # super().__init__(ancho, alto)  # no podemos referenciar la clase padre usando super porque en un caso de
        # herencia múltiple, el interprete no puede inferir a que clase padre estamos llamando.

        # super().__init__(color)


        FiguraGeometrica.__init__(self, alto, ancho)  # referenciamos a la clase padre con su nombre
        Color.__init__(self, color)

    def calcular_area(self):
        return self.alto * self.ancho

    def __str__(self):
        return f"Cuadrado =  {FiguraGeometrica.__str__(self)} {Color.__str__(self)}"