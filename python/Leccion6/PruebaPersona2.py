# importamos módulo Persona2 y de ese módulo la clase Persona2

from Persona2 import Persona2  # Si quisieramos importar todas las clases y métodos del archivo:
# from <archivo> import *
print("Creación de objetos".center(50, "/"))  # método center posición el elemento al centro, 1er par: width, 2do par
# string
# Comprobación del método principal en ejecución (main)
if __name__ == "__main__":
    print("Objeto 4")
    persona5 = Persona2("Lionel", "Messi", 35)
    print(persona5.mostrar_detalles())
    persona5.nombre = "Gustavo"
    persona5.apellido = "De Llac"
    print(persona5.mostrar_detalles())
    print(__name__)  # nos indica que el archivo desde el que estamos ejecutando el código es el main (__main__)
print("Eliminación de objetos".center(50, "/"))
del persona5  # llamamos al método destructor
