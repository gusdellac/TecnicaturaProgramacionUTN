# Ejercicio 2: Modificar los elementos de una lista
# Llenar una lista con los números del 1 al 10, luego modificar los
# elementos de la lista multiplicándolos por un valor ingresado por el usuario

# 1 solución
lista = list(range(1, 11))
multiplo = int(input("Digite un número a multiplicar: "))
for elemento in lista:
    lista[elemento-1] *= multiplo
print(lista)

# 2 solución
lista2 = list(range(1, 11))
print("Lista original")
for i in lista2:
    print(i, end='-')
valor = int(input("\nDigite unvalor a multiplicar: "))
# Multiplicamos todos los elementos de la lista
for indice, i in enumerate(lista2):  # Método enumerate() sirve para modificar los índices de la lista
    lista2[indice] *= valor  # El iterador sólo recorre los índices, en ésta línea se multiplica
print(f"Lista final con los elementos multiplicados por {valor}")
for i in lista2:
    print(i, end='-')