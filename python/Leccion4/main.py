# COLECCIONES DE DATOS EN PYTHON

# Listas (arrays) . Las listas son mutables
nombres = ['Marcela', 'Roman', 'Fernanda', 'Leonardo']
print('Listas o arrays')
print(nombres[0])  # Mostramos el primer elemento
print(nombres[2])  # Mostramos el tercer elemento
print(nombres[-1])  # Mostramos el último elemento
print(nombres[-2])  # Mostramos el penúltimo elemento
print(nombres[:2])  # Mostramos el elemento del índice 0 y 1
print(nombres[:3])  # Mostramos el elemento del índice 0 y 1
print(nombres[1:])  # Mostramos el elemento del índice 1 en adelante
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

# Agregar elemento. Se pueden agregar diferentes tipos de datos
nombres.append('Marcelo')  # Método append()
nombres.append([1, 2, 3])  # Agregamos una lista en una posición de la lista anterior
nombres.append(True)  # dato booleano
nombres.append(10.45)  # dato numérico flotante
nombres.append([4, 5])  # lista
nombres.append(7)  # entero
print(nombres)
print(nombres[5])  # print de la lista agregada en la posición 5 del array
print(nombres[5][2])  # print de la posición 2 de la lista guardada en la posición 5 del array

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

# Concatenamos listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = lista1 + lista2
print(lista3)

# Método extend(). Agregamos elementos a una lista
lista3.extend([7, 8, 9])
print(lista3)

print(lista3.index(5))  # método para ubicar en que índice esta el valor ingresado
# print(lista3.index(.))  # esto genera error porque el elemento no esta en la lista

# Como saber si un valor indicado esta repetido y cuantas veces lo está.
print(lista3.count(1))  # Método count()

# Para invertir una lista. Método reverse()
lista3.reverse()
print(lista3)

# Para que una lista se multiplique repitiendo sus elementos
lista = [1, 2, 3] * 2
print(lista)

# Métodos de ordenamiento
lista.sort()  # método sort() .Ordena los elementos ascendentemente
print(lista)
lista.sort(reverse=True)  # método sort() con parámetro reverse=True . Ordena los elementos descendentemente
print(lista)



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
cocinaLista = list(cocina)  # Convertimos la tupla a lista
print(type(cocinaLista))
cocinaLista[0] = 'Plato'  # Modificamos un valor de la lista
cocina = tuple(cocinaLista)  # Convertimos la lista a tupla
print(type(cocina))

# Tupla con elementos de distinto tipo de dato
tupla = (4, 'Hola', 6.78, [1, 2, 78], 4, 'Hola')

print(4 in tupla)  # Buscamos un elemento. Devuelve un dato booleano

# Eliminar tupla
del cocina

# Se puede usar con tuplas los métodos index() count() len()

# Tipo set : Se pueden almacenar datos de forma similar a las listas y tuplas.
# No se almacenan datos repetidos y los datos almacenados no tienen un orden (no tienen índice)
planetas = {'Marte', 'Júpiter', 'Venus'}
print(planetas)
# método len()
longitudPlanetas = len(planetas)
print(longitudPlanetas)

# Verificar si un elemento existe dentro del conjunto set
print('Marte' in planetas)
print('Marte' not in planetas)  # Forma negativa

# Agregar un elemento, método add()
planetas.add('Tierra')
print(planetas)

# Eliminar elementos
# Método remove() , arroja error si el elemento no existe
planetas.remove('Júpiter')
print(planetas)
# Método discard() , no arroja error si el elemento no existe
planetas.discard('Tierra')
print(planetas)

# Limpiar set o conjunto
planetas.clear()
print(planetas)

# Eliminar set o conjunto
del planetas

# Diccionarios. Está cumpuesto por dos elementos -(llave : valor)
# dict(key,value)
# Los diccionarios no tienen índice, se accede a los elementos mediante las llaves
diccionario = {
    'IDE': 'Integrated Development Environment',
    'POO': 'Programación Orientada a Objetos',
    'SABD': 'Sistema de Administración de Base de Datos'
}
# Verificar la cantidad de elementos de un diccionario
print(len(diccionario))
print(diccionario)
# Acceder a un diccionario con la llave(key)
print(diccionario['IDE'])

# Otra forma de recuperar un elemento. Método get()
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

# Modificamos elementos
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario)

# Como recorrer los elementos
for termino in diccionario:  # Recorremos el diccionario mostrando solo las llaves(key)
    print(termino)
# Necesitamos un método para recorrer el diccionario y poder acceder al valor de las llaves. Método items()
for termino, valor in diccionario.items():
    print(termino, valor)

# Otras maneras de acceder a un diccionario.

# Método keys(). Accedemos a key
for termino in diccionario.keys():
    print(termino)  # Muestra solo las llaves

# Método value() . Accedemos a value
for valor in diccionario.values():
    print(valor)

# Comprobar la existencia de algún elemento
print('IDE' in diccionario)  # devuelve dato booleano

# Agregar un elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)

# Eliminar un elemento. Método pop()
diccionario.pop('SABD')
print(diccionario)

# Vaciar un diccionario. Método clear()
diccionario.clear()
print(diccionario)

# Eliminar diccionario
del diccionario


# Pilas usando listas (forma de trabajo)
pila = [1, 2, 3]

# Agregar elementos a la pila por el final. Método append()
pila.append(4)
pila.append(5)
print(pila)

# Sacamos elementos desde el final. Método pop()
elementoBorrado = pila.pop()  # Quita el último elemento y lo guarda en la variable
print(f'Sacamos el elemento {elementoBorrado}')
print(f'La pila ahora quedo así: {pila}')

# Colas usando listas (forma de trabajo)
# Estructura de datos de tipo fifo(first input / first output)

cola = ['Ariel', 'Osvaldo', 'Liliana', 'Pilar']

# Agregamos elementos al final de la cola
cola.append('Natalia')
cola.append('José')
print(cola)

# Sacamos elementos de la cola
seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

