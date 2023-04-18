archivo = open("prueba.txt", "r", encoding="utf8")
# print(archivo.read())
# print(archivo.read(16))  # lee la cantidad de caracteres que le indiquemos como parametro, desde el inicio del archivo
# print(archivo.readline())  # lee una linea del archivo, desde el inicio

# iteracion sobre un archivo
# for linea in archivo:
    # print(linea)  # iteramos todos los elementos del archivo

# print(archivo.readlines()[11])  # retorna una lista con todas las lineas del archivo


# Anexamos informacion, copiamos a otro
archivo2 = open("copia.txt", "a", encoding="utf8")
archivo2.write(archivo.read())
archivo.close()  # cerramos el primer archivo
archivo2.close()  # cerramos el segundo archivo

print("Se ha terminado el proceso de leer y copiar archivos")