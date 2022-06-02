"""
Ejercicio5: Calcular estación del anio
Pedir al usuario que ingrese un mes del año, el valor debe ser entre 1 y 12,
luego le decimos en que estación del año esta:
Verano 21/12 al 21/03 (1,2,3); Otonio 21/03 al 21/06 (4,5,6); Invierno 21/06 al 21/09 (7,8,9)
Primavera 21/09 al 21/12 (10,11,12)
"""
mes = int(input("Digite un mes del año (1 - 12): "))
estacion = None
if (mes > 0) and (mes < 4):
    estacion = "Verano"
elif (mes > 3) and (mes < 7):
    estacion = "Otoño"
elif (mes > 6) and (mes < 10):
    estacion = "Invierno"
elif (mes > 9) and (mes < 13):
    estacion = "Primavera"
else:
    estacion = "Error, el mes ingresado es incorrecto"
print(f"Para el mes {mes} la estación es: {estacion}")
