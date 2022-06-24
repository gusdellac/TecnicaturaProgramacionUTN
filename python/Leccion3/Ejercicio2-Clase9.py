# Calcular la suma de "N" primeros números
n = int(input("Digite la cantidad de números a sumarse: "))
suma = 0
for i in range(1, n+1):
    suma += i
print(f"La suma es: {suma}")