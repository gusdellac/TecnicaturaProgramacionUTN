# MANEJO DE CONTEXTO WIDTH : sintaxis simplificada, abre y cierra el archivo
from ManejoArchivos import ManejoArchivos

with open("prueba.txt", "r", encoding="utf8") as archivo:
    print(archivo.read())
# No hace falta try , finally
# Utiliza los siguientes metodos: __enter__ este abre el archivo
# __exit__ este cierra el archivo

with ManejoArchivos("prueba.txt") as archivo:
    print(archivo.read())