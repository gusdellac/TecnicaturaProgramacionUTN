# Ejercicio 5: Convetidor de temperaturas
# Realizar dos funciones para convertir de grados celsius a fahrenheit y viceversa
# Investigar las formulas

def convertir_a_fahrenheit(grados):
    return grados * 9/5 + 32
def convertir_a_celsius(grados):
    return (grados - 32) * 5/9

gradosCelsius = float(input("Digite los grados Celsius que desea convertir a Fahrenheit: "))
resultadoCelsiusAFahrenheit = convertir_a_fahrenheit(gradosCelsius)
print(f"{gradosCelsius} °C = {resultadoCelsiusAFahrenheit:.2f} °F ")
gradosFahrenheit = float(input("Digite los grados Fahrenheit que desea convertir a Celsius: "))
resultadoFahrenheitACelsius = convertir_a_celsius(gradosFahrenheit)
print(f"{gradosFahrenheit} °F = {resultadoFahrenheitACelsius:.2f} °C")