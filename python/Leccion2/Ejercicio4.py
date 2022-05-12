"""
Ejercicio 4: Área y longitud de un circulo
Hacer un programa para ingresar el radio de un circulo y
se reporte su área y la longitud de la circunferencia.
Area = pi * r**2
longitud = 2 * pi * r
debemos importar el modulo import math (contiene el valor de pi)
"""
import math  # al utilizar el math.pi se importa automáticamente el módulo math

radio = float(input("Ingrese el radio del círculo: \n"))
area = math.pi * radio ** 2  # utilizamos el módulo math para funciones matemáticas
longitud = 2 * math.pi * radio

print(f"El área del círculo es: {area}")
print(f"La longitud del círculo es: {longitud}")
