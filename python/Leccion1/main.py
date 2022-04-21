# VARIABLES

variable = 1
miVariable = 2
print(variable + miVariable)

miVariable = "Holaaaaaaa"
print(miVariable)

x = 10
y = 2
z = x + y
# Usamos una funcion dentro de otra
print(id(x))
# las literales se escriben x936
print(id(z))
print(id(y))

# TIPOS DE DATOS
# integer, float, string, bool
x = 10
print(x)
print(type(x))

# Float
x = 10.5
print(x)
print(type(x))

# String
x = "Hola mundo"
print(x)
print(type(x))

# Boole
x = True
print(x)
print(type(x))
x = False
print(x)
print(type(x))

# Manejo de Strings
miGrupoFavorito = "Pink Floyd -"
caracteristicas = "The Best Rock Band"
print("Mi grupo favorito es:", miGrupoFavorito, caracteristicas)  # Concatenamos con coma, se crea un
# espacio automáticamente
print("Mi grupo favorito es:" + miGrupoFavorito + caracteristicas)  # Concatenamos con + no se crea un espacio
# es necesario agregar el espacio : " "

numero1 = "7"
numero2 = "8"
print(numero1 + numero2)  # Como son datos tipo string se concatena como un string
print(int(numero1) + int(numero2))  # Para sumar los valores es necesario convertir los números a tipo int,
# usamos la función int() . En python el int es una clase

# Tipos booleanos (bool)
miBooleano = 3 > 2  # Definimos variable miBooleano con un dato tipo booleano (True or False)
print(miBooleano)

if miBooleano:  # Condicional que utiliza el valor lógico de la variable miBooleano para operar
    print("El resultado es verdadero")
else:
    print("El resultado es falso")

# Procesar la entrada del usuario

resultado = input("Digite un número: ")  # función input () regresa un dato tipo string
print(resultado)

# Conversión de la entrada de datos

numero1 = int(input("Escribe el primer número: "))  # con int () convertimos el dato tipo string a int
numero2 = int(input("Escribe el segundo número: "))
resultado = numero1 + numero2
print("El resultado de la suma es: ", resultado)

# Ejercicio 1 califica tu día
calificacion = input("¿ Cómo estuvo tu día (del 1 al 10) ?")
print("Mi día estuvo de:", calificacion)

# Ejercicio 2 información libro

titulo = input("Ingrese el nombre del libro: ")
autor = input("Ingrese el autor del libro: ")
print(titulo, "fue escrito por:", autor)



