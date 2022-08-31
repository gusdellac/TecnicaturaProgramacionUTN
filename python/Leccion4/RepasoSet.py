# Repaso de set o conjunto
conjunto = set()  # definimos un conjunto set
# conjunto1 = {}  # no se puede inicializar con {} vacías
conjunto1 = {'bye', }
conjunto.add(7)
conjunto.add('hola')
print(conjunto)
conjunto1.add('hola')
print(conjunto1)
print(3 not in conjunto1)  # Preguntamos si el número 3 NO esta en el conjunto

# Como hacer la igualdad de dos conjuntos
print(conjunto1 == conjunto)  # Nos devuelve un false como respuesta

# Operaciones con conjuntos
conjunto2 = conjunto | conjunto1  # La línea une los dos conjuntos
print(conjunto2)

conjunto2 = conjunto1 & conjunto2  # Que elemento tienen en comun
print(conjunto2)

conjunto2 = conjunto - conjunto1  # Asigna el valor que esta en el conjunto y no el en conjunto1
print(conjunto2)

conjunto2 = conjunto1 - conjunto
print(conjunto2)

conjunto2 = conjunto ^ conjunto1  # Elementos que no comparte o que son diferentes entre ambos
print(conjunto2)

conjunto2 = conjunto | conjunto1
print(conjunto.issubset(conjunto2))  # preguntamos si un conjunto es subconjunto dentro de otro
print(conjunto.issubset(conjunto1))

print(conjunto2.issuperset(conjunto))  # Preguntamos si los elementos del conjunto estan dentro del conjunto2
print(conjunto2.issuperset(conjunto1))  # Si es verdadero quiere decir que el conjunto2 es un superconjunto
print(conjunto1.issuperset(conjunto2))

# Como saber si ambos conjuntos son disconexos, esto es si no comparten elementos en comun
print(conjunto.isdisjoint(conjunto1))  # no hay cosas en común

# Convertir un conjunto totalmente en inmutable
conjunto = frozenset  # Esto hace que el conjunto sea totalmente inmutable
