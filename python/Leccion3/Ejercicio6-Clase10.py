# Ejercicio 7: Ingresar "N" enteros, visualizar la suma de los
# números pares de la lista, cuántos números pares existen y
# cuál es el promedio de los números impares
i = 1
sumaPares = 0
conteoPares = 0
sumaImpares = 0
conteoImpares = 0
nElementos = int(input("Digite la cantidad de elementos a ingresar: "))
while i <= nElementos:
    num = int(input(f"{i}. Digite un número: "))
    if num % 2 == 0:
        sumaPares += num
        conteoPares += 1
        i += 1
    else:
        sumaImpares += num
        conteoImpares += 1
        i += 1
if conteoPares == 0:
    print("No se han digitado números pares.")
else:
    print(f"La suma de los números pares es: {sumaPares}")
    print(f"El conteo de los números pares es: {conteoPares}")
if conteoImpares == 0:
    print("No se han digitado números impares")
else:
    promedioImpares = sumaImpares/conteoImpares
    print(f"El promedio de números impares es: {promedioImpares}")