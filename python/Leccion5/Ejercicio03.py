# Ejercicio 3: Función Recursiva
# Imprimir números de N a 1 de manera descendente usando funciones recursivas.
# Puede ser cualquier valor positivo, por ej, si pasamos el valor de 5
# debe imprimir :
# 5 , 4 ,3 , 2 , 1
# En caso de ser el número 3 debe imprimir:
# 3 , 2 , 1
# Si se ingresan números negativos no imprime nada
def imprimirNumeros(number):
    if number >= 1:  # Caso base
        print(number)
        imprimirNumeros(number-1)  # Caso recursivo
numeroIngresado = int(input("Digite un número: "))
imprimirNumeros(numeroIngresado)
