class MiClase:
    # Variable de clase, este atributo dará a cada objeto el mismo valor
    variableClase = "Esta es una variable de clase"  # este atributo está relacionado con la clase (atributo static
    # en java)

    def __init__(self, variableInstancia):  # Variable de instancia, este atributo recibirá un valor para cada objeto
        # instanciado de esta clase
        self.variableInstancia = variableInstancia  # este atributo está relacionado con las instancias

    @staticmethod  # Método estático, se asocia a la clase
    def metodo_estatico():
        print("Método estático".center(50, "_"))
        print(MiClase.variableClase)

    @classmethod  # método de clase
    def metodo_clase(cls):  # python coloca cls como parámetro por defecto. Este parámetro es una referencia a la
        # clase
        print("Método de clase".center(50, "_"))
        print(cls.variableClase)  # llamamos a un atributo de clase utilizando cls
        print(MiClase.variableClase)  # llamamos a un atributo de clase utilizando el nombre de la clase

    def metodo_instancia(self):
        print("Método de instancia".center(50, "_"))
        self.metodo_clase()
        self.metodo_estatico()

miClase1 = MiClase("Esta es una variable de instancia")
print(miClase1.variableInstancia)
print(miClase1.variableClase)
miClase2 = MiClase("Esta es otra variable de instancia")
print(miClase2.variableInstancia)
print(miClase2.variableClase)
print(MiClase.variableClase)

# Podemos crear un atributo de clasea fuera de la clase
MiClase.variableClase2 = "Esta es otra variable de clase"
print(MiClase.variableClase2)

# Si intentamos acceder a este nuevo atributo desde los objetos vemos que el compilador nos recomienda que los atributos
# esten dentro de la clase, de todas maneras el código se puede ejecutar
print(miClase1.variableClase2)
print(miClase2.variableClase2)

MiClase.metodo_estatico()
miClase1.metodo_estatico()
miClase2.metodo_estatico()

MiClase.metodo_clase()
miClase1.metodo_clase()
miClase2.metodo_clase()

miClase1.metodo_instancia()