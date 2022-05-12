# Sentencia if/else
"""
condicion = input("Digite True ó False:\n")

if condicion == 'True':
    condicion = True
elif condicion == 'False':
    condicion = False
else:
    print("Ingreso un dato incorrecto")

if condicion == True:
    print('Condición Verdadera')
elif condicion == False:
    print('Condición Falsa')
else:
    print('Condición sin especificar')
"""

num = int(input("Digite un número en el rango del 1 al 3:\n"))
numTexto = ""
if num == 1:
    numTexto = "Número uno"
elif num == 2:
    numTexto = "Número dos"
elif num == 3:
    numTexto = "Número tres"
else:
    numTexto = "Has ingresado un número fuera de rango"
print(f"El número ingresado es: {num} - {numTexto}")

