# profundizando en el tipo float
a = 3.0
print(f"a: {a:.2f}")

# constructor tipo flaot -> puede recibir int y str
a = float(10)  # le pasamos un tipo int
print(f"a: {a:.2f}")
a = float("10")  # le pasamos un tipo str
print(f"a: {a:.2f}")

# notacion exponencial (valores positivos o negativos)
a = 3e5
print(f"a: {a:.2f}")

a = 3e-5
print(f"a: {a:.5f}")

# cualquier calculo que incluya un float, cambia el resultado a float

a = 4.0 + 5
print(a)
print(type(a))




