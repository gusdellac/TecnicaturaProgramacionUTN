
# Bool contiene los valores de True y False
# Los tipos numerico, es false para el 0(cero) y true para los demas valores

valor = 0
resultado = bool(valor)
print(f"valor: {valor}, resultado: {resultado}")

valor = 0.1
resultado = bool(valor)
print(f"valor: {valor}, resultado: {resultado}")

# Tipo string -> False "", True demas valores
valor = ""
resultado = bool(valor)
print(f"valor: {valor}, resultado: {resultado}")

valor = "hola"
resultado = bool(valor)
print(f"valor: {valor}, reusltado: {resultado}")

# Tipo colecciones -> False para colecciones vacias
# Tipo colecciones -> True para todas las demas
# Lista
valor = []
resultado = bool(valor)
print(f"valor lista vacia: {valor}, resultado: {resultado}")

valor = [2, 3, 4]
resultado = bool(valor)
print(f"valor lista con elementos: {valor}, resultado: {resultado}")

# Tupla
valor = ()
resultado = bool(valor)
print(f"valor tupla vacia: {valor}, resultado: {resultado}")

valor = (5,)
resultado = bool(valor)
print(f"valor tupla con elementos: {valor}, resultado: {resultado}")

# diccionario
valor = {}
resultado = bool(valor)
print(f"valor diccionario vacio: {valor}, resultado: {resultado}")

valor = {"nombre": "juan", "apellido": "perez"}
resultado = bool(valor)
print(f"valor diccionario con elementos: {valor}, resultado: {resultado}")

# sentencias de control con bool
valor = "algo"
if valor:
    print("Regresa verdadero")
else:
    print("Regresa falso")

# ciclos
variable = 0
while variable:
    print("regresa verdadero")
    break
else:
    print("Regresa falso")