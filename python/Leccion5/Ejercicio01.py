# Ejercicio 01: Crear una función para sumar los valores recibidos de tipo
# numéricos, utilizando argumentos variables *args como parámetro de la
# función y agregar como resultado la suma de todos los valores pasados como
# argumentos.

def sumar_valores(*args):  # cantidad de parámetros indefinidos
    # pass (se utiliza para no generar error si no se ingresa código dentro de la función)
    resultado = 0
    for numero in args:
        resultado += numero
    return resultado
resultadoSuma = sumar_valores(2, 6, 6)
print(f"El resultado  de la sumatoria es: {resultadoSuma}")