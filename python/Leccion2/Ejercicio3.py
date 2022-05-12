# Ejercicio 3: Intercambiar el valor de dos variables.
a = 10
b = 5
print(f"El valor de a es: {a}")
print(f"El valor de b es: {b}")
# Intercambiamos los valores de las variables utilizando un auxiliar
aux = a
a = b
b = aux
print(id(a))
print(id(b))
print(f"El nuevo valor de a es: {a}")
print(f"El nuevo valor de b es: {b}")
# Intercambiamos los valores de las variables en la misma línea sin tener que utilizar un auxiliar
a, b = b, a  # Notar que la reasignación se realiza al mismo tiempo
print(id(a))
print(id(b))
print(f"El nuevo valor de a es: {a}")
print(f"El nuevo valor de b es: {b}")
