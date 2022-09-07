# Ejercicio 1: Llenar una lista
# Llenar una lista con los números del 1 al 50, luego mostrar
# la lista con el bucle for, los elementos deben mostrarse
# de la siguiente forma:
# 1-2-3-4-5...50

# Solución 1
lista = []
for elementos in range(1, 51):
    lista.append(elementos)
for elementos in lista:
    print(elementos, end='-')
print('\n')

# Solución 2
lista2 = []
i = 1
while i <= 50:
    lista2.append(i)
    i += 1
for i in lista2:
    print(i, end='-')
print('\n')

# Solución 3
lista3 = list(range(1, 51))
for i in lista3:
    print(i, end='-')