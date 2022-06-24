# Ejercicio 5: Calcular el factorial de un número mayor o igual a 0
i = 1
factorial = 1
num = -1
while num < 0:
    num = int(input("Digite un número mayor o igual a 0 : "))
while i <= num:
    factorial *= i
    i += 1
print(f"El factorial es: {factorial}")

"""
numero = int (input("INGRESE NUMERO:"))
factorial = 1
if numero !=0:
    for i in range (1, numero+1):
        factorial = factorial * 2
print ("factorial:", factorial)
"""