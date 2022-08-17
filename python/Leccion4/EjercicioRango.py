"""
Sintaxis de range(inicio <opcional>, fin <requerido>, incremento <opcional>)
"""
# Ejercicio 1: Iterar un rango de 0 a 10 e imprimir números divisibles entre 3
# Ejemplo ejecución: 0,3,6,9

print('Ejercicio 1: ')
for iterador in range(0, 10, 3):
    print(iterador)

print('Ejercicio 1-b:  ')
for iterador in range(0, 10):
    if iterador % 3 == 0:
        print(iterador)

# Ejercicio 2: Crear un rango de números de 2 a 6 e imprimelos
# Ejemplo ejecución: 2,3,4,5,6
print('Ejercicio 2: ')
for iterador in range(2, 7):
    print(iterador)

# Ejercicio 3: Crear un rango de 3 a 10 pero con incremento de 2 en 2, en lugar de 1 en 1
# Ejemplo ejecución: 3,5,7,9
print('Ejercicio 3: ')
for iterador in range(3, 10, 2):
    print(iterador)



