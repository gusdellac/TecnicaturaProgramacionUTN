# Diseñar un programa que ingresando un año, nos devuelva por consola
# si es un año bisiesto o no, repetir la acción hasta que el usuario lo decida
opcion = 1
print("Comprobamos que año es Bisiesto")
while opcion == 1:
    num = int(input("Digite un año: "))
    if num % 4 == 0 and num % 100 != 0 or num % 400 == 0:
        print(f"¡El año {num} es Bisiesto!")
        opcion = int(input("Para seguir adelante digite la opción 1: "))
    else:
        print(f"¡El año {num} no es Bisiesto!")
        opcion = int(input("Para seguir adelante digite la opción 1: "))