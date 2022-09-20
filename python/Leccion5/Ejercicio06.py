# Ejercicio 6: Tabla de multiplicar
# Hacer un programa que pida un número por teclado y guarde en una
# lista su tabla de multiplicar hasta el 10. Por ejemplo:
# si digita el 5 la lista tendrá: 5,10,15,20,25,30,35,40,45,50
num = int(input("Digite un número: "))
lista = []
for i in range(1, 11):
    lista.append(num*i)
print(f"\nTabla de multiplicar de {num}: \n{lista}\n")

for indice, elemento in enumerate(lista):
    print(f"{num} * {indice+1} = {elemento}")