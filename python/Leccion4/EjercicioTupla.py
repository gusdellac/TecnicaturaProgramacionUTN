# Dada la siguiente tupla
tupla = (13, 1, 8, 3, 2, 5, 8)  # Definimos la tupla
# Crear una lista que solo incluya los números menores a 5 e imprima por consola [1, 3, 2]
lista = []
for numero in tupla:
    if numero < 5:
        lista.append(numero)
print(lista)