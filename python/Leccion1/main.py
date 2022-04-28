"""
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
"""

"""
# Operadores aritméticos
operandoA = 8
operandoB = 5
suma = operandoA + operandoB
print("Resultado de la suma:", suma)
print(f"El resultado de la suma es: {suma}")  # utilizamos la f (format) para interpolar la variable en un string

resta = operandoA - operandoB
print(f"El resultado de la resta es: {resta}")

multiplicacion = operandoA * operandoB
print(f"El resultado de la multiplicación: {multiplicacion}")

division = operandoA / operandoB
print(f"El resultado de la división es: {division}")  # resultado tipo float
division = operandoA // operandoB  # devuelve un resultado de tipo int
print(f"El resultado de la división (int) es: {division}")

modulo = operandoA % operandoB
print(f"El resultado de la división o residuo (modulo) es: {modulo}")

exponente = operandoA ** operandoB  # exponenciación
print(f"El resultado de la potencia es: {exponente}")



alto = int(input("Digite el alto del rectángulo: "))
ancho = int(input("Digite el ancho del rectángulo: "))
area = alto * ancho
perimetro = (alto + ancho)*2
print(f"El área del rectángulo es: {area}")
print(f"El perímetro del rectángulo es: {perimetro}")

miVariable3 = 10
print(miVariable3)
# Operadores de reasignación
miVariable3 = miVariable3 + 1
print(miVariable3)
miVariable3 += 1  # forma resumida de reasignación e incremento (miVar = miVar + 1)
print(miVariable3)
miVariable3 -= miVariable3 - 2  # forma resumida de reasignación y resta (miVar = miVar - 2)
print(miVariable3)
miVariable3 *= 3  # reasignación y producto (miVar = miVar * 3)
print(miVariable3)
miVariable3 /= 2  # reasignación y división (miVar = miVar / 2)
print(miVariable3)

# Operadores de Comparación
# Devuelven un tipo de dato booleano
d = 4
b = 2
resultado = d == b  # operador de igualdad
print(resultado)
resultado = d != b  # operador de desigualdad
print(resultado)
resultado = d > b  # operador de mayor que
print(resultado)
resultado = d < b  # operador de menor que
print(resultado)
resultado = d >= b  # operador mayor igual que
print(resultado)
resultado = d <= b  # operador menor igual que
print(resultado)
"""

# Par - impar

numero = int(input("Digite un número: "))
print(f"El residuo de la división es: {numero % 2}")
if numero % 2 == 0:  # en python en los if y else en lugar de utilizar {} para ingresar un bloque de código
    # afectado por el condicional se utilizan los (:)
    print(f"El valor de la variable es: {numero} , es un número par")
else:
    print(f"El valor de la variable es: {numero} , es un número impar")

edad = int(input("Digite su edad: "))
if edad >= 18:
    print(f"La edad digitada es: {edad} años, es mayor de edad")
else:
    print(f"La edad digitada es: {edad} años, es menor de edad")


