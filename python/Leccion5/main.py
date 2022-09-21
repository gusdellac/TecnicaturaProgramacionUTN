# FUNCIONES EN PYTHON

# mi_funcion() no se puede llamar una función antes de definirla

# Definimos una función
def mi_funcion():
    print("Saludos!!")
mi_funcion()  # llamada a la función
mi_funcion()  # Se puede llamar a una función N cantidad de veces

# Desempaquetado de listas o list Unpacking
def show(name, lastName):
    print(name+" "+lastName)
person = ["Ariel", "Betancud"]  # desempaquetamos una lista
show(person[0], person[1])  # Pasamos uno por uno los datos de la lista a la función
show(*person)  # Muestra toda la lista
person2 = ("Osvaldo", "Giordanini")  # desempaquetamos a través de una tupla
show(*person2)
person3 = {"lastName": "Lucero", "name": "Natalia"}  # desempaquetamos un diccionario
show(**person3)

# Repaso ciclo for else
numbers = [1, 2, 3, 4, 5]
for n in numbers:
    print(n)
    if n == len(numbers):  # de esta forma podemos evitar la ejecución del else
        break
else:  # cuando finaliza toda la iteración del for se ejecuta el else
    print("Esto se termino")


# List comprehension, lista de comprensión
names = ["Paolo", "Rodrigo", "Lupe", "Pepe"]
alongP = [p for p in names if p[0] == "P"]  # Esto regresa una nueva lista
print(alongP)

bottleC = [{"name": "Quilmes", "country": "Arg"},
           {"name": "Corona", "country": "Mx"},
           {"name": "Stella Artois", "country": "Belgium"}]
Arg = [b for b in bottleC if b["country"] == "Arg"]
print(Arg)
print(bottleC)

# Paso de Argumentos (funciones)
def mi_funcion2(name, lastName):
    print("Saludos a todos!")
    print(f"Nombre: {name}, Apellido: {lastName}")
mi_funcion2("Jorge", "Lucero")
mi_funcion2("Gustavo", "De Llac")
mi_funcion2("Roberto", "Bolaños")

# Palabra reservada return en funciones
# Creamos una función para sumar
def sumar(a, b):
    return a + b
# resultado = sumar(78, 22)
# print(f"El resultado de la suma es: {resultado}")
print(f"El resultado de la suma es: {sumar(55, 45)}")

def sumar2(a:int = 0, b:int = 0):  # Le damos un valor por default
    return a + b
resultado = sumar2()
print(f"Resultado de la suma: {resultado}")
print(f"Resultado de la suma: {sumar2(22, 66)}")

# Argumentos, variables en funciones
def listarNombres(*nombres):  # *nombres se utiliza si desconocemos la cantidad de argumentos que se pasarán a la función
# Normalmente se utiliza: *args
    for nombre in nombres:  # nombres se convierte en una tupla
        print(nombre)
listarNombres("Gustavo", "Ariel", "Ricardo", "Pedro", "Matias")
listarNombres("Marcos", "Daniel", "Romina", "Pepe", "Marcela", "Carlos")
