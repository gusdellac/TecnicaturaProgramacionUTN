class MiClase:
    # Variable de clase, este atributo dará a cada objeto el mismo valor
    variableClase = "Esta es una variable de clase"  # este atributo está relacionado con la clase

    def __init__(self, variableInstancia):  # Variable de instancia, este atributo recibirá un valor para cada objeto
        # instanciado de esta clase
        self.variableInstancia = variableInstancia  # este atributo está relacionado con las instancias

print(MiClase.variableClase)

miClase1 = MiClase("Esta es una variable de instancia")
print(miClase1.variableInstancia)
print(miClase1.variableClase)
miClase2 = MiClase("Esta es otra variable de instancia")
print(miClase2.variableInstancia)
print(miClase2.variableClase)