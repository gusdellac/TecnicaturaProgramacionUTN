# Listas (arrays) . Las listas son mutables
nombres = ['Marcela', 'Roman', 'Fernanda', 'Leonardo']
print('Listas o arrays')
print(nombres[0])  # Mostramos el primer elemento
print(nombres[2])  # Mostramos el tercer elemento
print(nombres[-1])  # Mostramos el último elemento
print(nombres[-2])  # Mostramos el penúltimo elemento
print(nombres[ :2])  # Mostramos el elemento del índice 0 y 1
print(nombres[ :3])  # Mostramos el elemento del índice 0 y 1
print(nombres[1: ])  # Mostramos el elemento del índice 1 en adelante
nombres[2] = 'Ricardo'  # Modificamos un valor
print(nombres)
print('\n')
# Iteración sobre array
for nombre in nombres:
    print(nombre)
else:
    print('Finalizó el recorrido del array')

# Longitud array
print(f'La lista o array tiene: {len(nombres)} elementos')  # Método len()

# Agregar elemento a array
nombres.append('Marcelo')  # Método append()
print(nombres)

# Insertar un elemento en un índice específico
nombres.insert(1, 'Alberto')  # Método insert()
print(nombres)
nombres.insert(3, 'Debora')
print(nombres)

# Eliminamos un elemento
nombres.remove('Alberto')  # Método remove()
print(nombres)

# Eliminar el último elemento
nombres.pop()  # Método pop()
print(nombres)

# Eliminar un índice específico
del nombres[2]  # palabra reservada del significa delete (eliminar)
print(nombres)

# Eliminar, borrar o limpiar todos los elementos
nombres.clear()
print(nombres)

# Eliminar lista
del nombres

# Tupla . Son listas no mutables
print('\n')
print('Tuplas:')
cocina = ('cuchara', 'cuchillo', 'tenedor')
print(cocina)
print(len(cocina))

# Acceder a un elemento, par esto utilizamos corchetes
print(cocina[0])
# Mostrar de manera inversa
print(cocina[-1])

# Acceder a un rango
print(cocina[0:2])

# Ejemplo
verduras = ('papa',)  # Una tupla necesita aunque sea un elemento más una coma, de lo contrario sólo sería un string
print(verduras)

# Recorremos elementos de una tupla
for cocinar in cocina:
    print(cocinar, end=' ')  # Print está usando \n para salto de líneas. Utilizando palabra reservada end no se
    # realizan los saltos de línea del print. Ejemplo end=' ' , se verá en una sola línea con un espacio

# Modificar elementos de una tupla (es una mala práctica)
cocinaLista = list(cocina)
print(type(cocinaLista))
cocinaLista[0] = 'Plato'
cocina = tuple(cocinaLista)
print(type(cocina))

# Eliminar tupla
del cocina





