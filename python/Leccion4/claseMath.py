import math  # Importamos la clase math para hacer uso de la función sqrt(raíz cuadrada)

numero = int(input('Digite un número positivo: '))
while numero < 0:
    print('Error, debería ingresar un número positivo!!')
    numero = int(input('Digite un número positivo: '))
print(f'\nSu raíz cuadrada es: {math.sqrt(numero):.2f}')  # Calculamos la raíz cuadrada utilizando la clase math con el
# método sqrt()  . Despues de los dos puntos (:.2f) indicamos con .2f que limite los decimales a mostrar