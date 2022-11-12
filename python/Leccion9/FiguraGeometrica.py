from abc import ABC, abstractmethod
# ABC significa: Abstract Base Class, convierte una lase en abstracta

class FiguraGeometrica(ABC):  # nuestra clase debe extender de clase ABC para poder ser abstracta
    def __init__(self, alto, ancho):

        # validaciones en el constructor:
        if self._validar_valores(alto):  # validamos el parámetro recibido
            self._alto = alto
        else:
            self._alto = 0
            print(f"Valor erroneo para el alto: {alto}")

        if self._validar_valores(ancho):  # validamos el parámetro recibido
            self._ancho = ancho
        else:
            self._ancho = 0
            print(f"Valor erroneo para el ancho: {ancho}")

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        if self._validar_valores(alto):  # validamos el parámetro recibido
            self._ancho = alto
        else:
            print(f"Valor erroneo alto: {alto}")

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        if self._validar_valores(ancho):  # validamos el parámetro recibido
            self._ancho = ancho
        else:
            print(f"Valor errone ancho: {ancho}")

    @abstractmethod
    def calcular_area(self):  # método abstracto (sin implementación)
        pass

    def __str__(self):
        return f"FiguraGeometrica: [Alto: {self._alto} ; Ancho: {self._ancho}]"

    # método encapsulado
    # utilizamos este método para realizar validaciones tanto en el constructor como en los setters
    def _validar_valores(self, valor):
        return True if 0 < valor < 10 else False
