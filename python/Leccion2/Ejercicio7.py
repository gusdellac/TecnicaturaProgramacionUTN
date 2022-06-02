"""
Ejercicio 5: Sistema de calificaciones
El objetivo del programa será crear un sistema de calificaciones de la siguiente
manera: Le pedimos al usuario que ingres un valor de 0 al 10.
"""
qualification = None  # No es necesario inicializar la variable
numberScoreUser = float(input("Digite su calificación entre 0 y 10: \n"))
if 10 >= numberScoreUser >= 9:
    qualification = "A"
elif 9 > numberScoreUser >= 8:
    qualification = "B"
elif 8 > numberScoreUser >= 7:
    qualification = "C"
elif 7 > numberScoreUser >= 6:
    qualification = "D"
elif 6 > numberScoreUser >= 0:
    qualification = "F"
else:
    qualification = "¡¡El valor ingresado es incorrecto!!"
print(f"El número ingresado es {numberScoreUser}, su calificación es: {qualification}")