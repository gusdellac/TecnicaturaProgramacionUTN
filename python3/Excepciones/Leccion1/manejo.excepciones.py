from NumerosIgualesException import NumerosIgualesException

# try catch en python . Capturamos y procesamos una exception

# ZeroDivisionError
try:
    10/0
except Exception as e:
    print(f"Ocurrio un error: {e}")

# ZeroDivisionError
try:
    10/0
except ZeroDivisionError as e:
    print(f"Ocurrio un error: {e}")

# ZeroDivisionError
resultado = None
a = 10
b = 0
try:
    resultado = a / b
except Exception as e:
    print(f"Ocurrio un error: {e}")
print(f"El resultado es: {resultado}")
print("seguimos...")

# TypeError
resultado = None
a = "10"
b = 0
try:
    resultado = a / b
except Exception as e:
    print(f"Ocurrio un error: {e}")
print(f"El resultado es: {resultado}")
print("seguimos...")


# Realizamos el tratamiento de diferentes excepciones en el mismo bloque
resultado = None

try:
    a = int(input("Digite el primer número: "))
    b = int(input("Digite el segundo número: "))
    if a == b:
        raise NumerosIgualesException("Son numeros iguales")  # con raise lanzamos la excepcion
    resultado = a / b
except TypeError as e:
    print(f"TypeError - Ocurrio un error: {type(e)}")
except ZeroDivisionError as e:
    print(f"ZeroDivisionError - Ocurrio un error: {type(e)}")
except Exception as e:
    print(f"Exception - Ocurrio un error: {type(e)}")
else:
    print("No se arrojo ninguna excepcion")
finally:  # Se ejecuta exista o no excepcion
    print("Ejecucion de este bloque finally")

print(f"El resultado es: {resultado}")
print("seguimos...")

