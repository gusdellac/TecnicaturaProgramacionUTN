try:
    archivo = open("prueba.txt", "w", encoding="utf8")  # Parametros function open : 1- archivo con el que se trabajara
    # 2- accion que se ejecutara en el archivo (w = write) , 3 - codificacion caracteres
    # la function open retorna un objeto que lo almacenamos en la variable  archivo
    archivo.write("Programamos con diferentes tipos de archivos, ahora en txt.\n")  # metodo write para sobreescribir
    # el doc
    archivo.write("Los acentos son importantes para las palabras\n")
    archivo.write("como por ejemplo: acción, ejecución y producción\n")
    archivo.write("Acciones sobre un archivo: \nr - read leer, \na append anexar, \nw - write escribir, "
                  "\nx - create crear archivo, \nt - text, \nb - archivos binarios, \nw+ leer y escribir, \nr+ ver\n")
    archivo.write("Con esto terminamos")
except Exception as e:
    print(e)
finally:  # siempre se ejecuta
    archivo.close()  # metodo close para cerrar

