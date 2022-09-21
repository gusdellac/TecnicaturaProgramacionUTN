# Ejercicio 11: Agenda telefónica
# Hacer un programa que simule una agenda de contactos. Crear un
# diccionario donde la clave sea el nombre del usuario y el valor
# sea el teléfono, el programa tendrá el siguiente menú de opciones:
#       1. Nuevo contacto
#       2. Borrar contacto
#       3. Ver contactos existentes
#       4. Salir
agenda = {}
nombreAgenda = input("Ingrese su nombre: ")
while True:
    print(f"\n\t.:Agenda telefónica de {nombreAgenda}:.")
    print("1. Nuevo contacto")
    print("2. Borrar contacto")
    print("3. Ver contactos existentes")
    print("4. Salir")
    opcion = int(input("Digite una opción de menú: "))
    print()
    if opcion == 1:
        nombreContacto = input("Ingrese el nombre del contacto: ")
        telefonoContacto = input("Ingrese el número del contacto: ")
        if nombreContacto not in agenda:
            agenda[nombreContacto] = telefonoContacto
            print("Contacto agregado exitosamente!")
        else:
            print("El nombre de contacto ya existe")
    elif opcion == 2:
        nombreContacto = input("Ingrese un contacto a eliminar: ")
        if nombreContacto in agenda:
            agenda.pop(nombreContacto)
            print("Se ha eliminado el contacto requerido")
        else:
            print("El contacto que desea eliminar no existe en la agenda")
    elif opcion == 3:
        print("Agenda de contactos")
        for clave, valor in agenda.items():
            print(f"Nombre: {clave}, Teléfono: {valor}")
    elif opcion == 4:
        print("Gracias por utilizar su agenda de contactos")
        break
    else:
        print("Se equivocó de opción de menú")
        print()