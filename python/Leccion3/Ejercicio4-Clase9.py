# Suponga que se tiene un conjunto de calificaciones de un grupo de 10 alumnos.
# Realizar un algoritmo para calcular la calificación promedio y la calificación
# más baja de todo el grupo

suma = 0
menorCalificacion = 99999
for i in range(10):
    calificacion = int(input(f"{i+1}. Digite una calificación: "))
    suma = suma + calificacion
    if calificacion < menorCalificacion:
        menorCalificacion = calificacion
calificacionPromedio = suma/10
print(f"La calificación promedio es: {calificacionPromedio}")
print(f"La calificación mas baja es: {menorCalificacion}")