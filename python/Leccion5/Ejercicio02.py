# Ejercicio 02 : Calcular el factorial de un número ingresado por el usuario

def factorial(numero):
    if numero == 0 or numero == 1:  # Caso Base
        return 1
    else:
        return numero * factorial(numero-1)  # Caso Recursivo

factorialACalcular = int(input("Digite el número del que desea calcular el factorial: "))
resultado = factorial(factorialACalcular)
print(f"El factorial de {factorialACalcular } es: {resultado}")