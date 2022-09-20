# Ejercicio 5: Factorial de un número positivo
# Hacer un programa para calcular el factorial de un número positivo

num = int(input("Digite un número positivo: "))
while num < 0:
    print("Error!! El número ingresado debe ser positivo")
    num = int(input("Digite un número positivo: "))
factorial = 1
for i in range(1, num+1):
    factorial *= i
print(f"El factorial de {num} es: {factorial}")