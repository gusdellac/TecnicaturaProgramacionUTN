# Ejercicio 1: Eliminar duplicados de una lista
# Escriba un programa donde tenga una lista y que a continuación
# elimine los elementos repetidos, por último mostrar la lista.

lista = [1, 2, 2, 3, 3, 3, 4, 5, 6, 7, 7, 8, 8]
# listaOrdenada = set(lista)  # convertimos la lista a un tipo set con el método set()
# print(type(listaOrdenada))
# lista = list(listaOrdenada)  # convertimos el tipo set a un tipo lista con el método list()
# print(lista)
# print(type(lista))
lista = list(set(lista))  # Realizamos los pasos anteriores en una sola línea
print(lista)