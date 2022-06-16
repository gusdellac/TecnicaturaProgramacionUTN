# Leer 10 números e imprimir cuantos son positivos, cuantos negativos
# y cuantos neutros
conteoNeutros = 0
conteoPositivos = 0
conteoNegativos = 0
for i in range(10):
    num = int(input(f"{i+1}. Digite un número: "))
    if num == 0:
        conteoNeutros = conteoNeutros + 1
    elif num > 0:
        conteoPositivos = conteoPositivos + 1
    else:
        conteoNegativos = conteoNegativos + 1
print(f"La cantidad de números neutros es: {conteoNeutros}")
print(f"La cantidad de números positivos es: {conteoPositivos}")
print(f"La cantidad de números negativos es: {conteoNegativos}")