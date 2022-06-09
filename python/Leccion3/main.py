# Ciclo while (Mientras o durante)
"""
contador = 0
while contador < 78:
    print(f"Ejecutamos nuestro ciclo while {contador}")
    contador += 1
else:
    print("Fin del ciclo while")
"""

# Imprimir números del 0 al 5 con ciclo while
"""
maximo = 5
contador = 0
while contador <= maximo:
    print(f"Contador: {contador}")
    contador += 1
"""
# Imprimir números del 5 al 0 con ciclo while
"""
minimo = 0
contador = 5
while contador >= 0:
    print(f"Contador: {contador}")
    contador -= 1
"""
# Ciclo for
"""
cadena = "Hello"  # Inicializamos var cadena con un string "Hello"
for letra in cadena:  # sintaxis para recorrer una cadena con un ciclo for. Se realiza una iteración por cada posición
    # de los caracteres que componen a la cadena hasta que se recorre la longitud total de la misma. Cada caracter se
    # guarda en var letra.
    print(letra)
else:
    print("Fin ciclo for")
"""

# Palabra reservada break
for letra in "Alemania":  # se recorre el string "Alemania"
    if letra == "a":  # condicional : cuando el caracter guardado en var letra coincide con la letra "a" ingresa al if
        print(f"Letra encontrada: {letra}")
        break  # break finaliza el ciclo for
else:
    print("Fin del ciclo for")

# Palabra reservada continue
for i in range(6):  # recorremos un rango utilizando la función range(). Cada valor del rango se guardará en var i
    # el rango comenzará en 0 hasta 5
    if i % 2 == 0:  # condicional para determinar si el número es par
        print(f"Valor: {i}")  # si el número es par se imprimirá en consola

for i in range(8):
    if i % 2 != 0:  # condicional para determinar si el número es impar
        continue  # si se cumple el condicional se ejecutará la palabra reservada continue. Esto nos llevará nuevamente
        # al recorrido del índice del rango para buscar el siguiente valor. Si este valor es un número par la condicion
        # no se cumplirá por lo que se ejecutará el print posterior
    print(f"Valor: {i}")