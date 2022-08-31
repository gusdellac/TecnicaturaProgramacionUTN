seleccionArgentina = {
    10: {'Nombre': 'Lionel Messi', 'Edad': 35, 'Altura': 1.70, 'Precio': '50 millones', 'Posicion': 'Extremo Derecho'},
    11: {'Nombre': 'Angel Di María', 'Edad': 34, 'Altura': 1.80, 'Precio': '12 millones', 'Posicion': 'Extremo Derecho'},
    5: {'Nombre': 'Leandro Paredes', 'Edad': 28, 'Altura': 1.80, 'Precio': '17 millones', 'Posicion': 'Medio Centro'},
    7: {'Nombre': 'Rodrigo De Paul', 'Edad': 28, 'Altura': 1.80, 'Precio': '40 millones', 'Posicion': 'Medio Campo'},
    20: {'Nombre': 'Giovani Lo Celso', 'Edad': 26, 'Altura': 1.77, 'Precio': '22 millones', 'Posicion': 'Medio Campo'},
    22: {'Nombre': 'Lautaro Martinez', 'Edad': 25, 'Altura': 1.74, 'Precio': '75 millones', 'Posicion': 'Delantero Centro'},
    24: {'Nombre': 'Alejandro Gomez', 'Edad': 34, 'Altura': 1.67, 'Precio': '6 millones', 'Posicion': 'Medio Campo'},
    13: {'Nombre': 'Cristian Romero', 'Edad': 24, 'Altura': 1.85, 'Precio': '48 millones', 'Posicion': 'Defensa Central'},
    19: {'Nombre': 'Nicolas Otamendi', 'Edad': 34, 'Altura': 1.83, 'Precio': '3.5 millones', 'Posicion': 'Defensa Central'},
    23: {'Nombre': 'Damian Emiliano Martinez', 'Edad': 29, 'Altura': 1.95, 'Precio': '28 millones', 'Posicion': 'Portero'}
}

for llave, valor in seleccionArgentina.items():
    print(llave, valor)

# Agregar por lo menos 4 jugadores más al diccionario
print('Tenemos cargado en el diccionario la cantidad de jugadores: ', end=' ')
print(len(seleccionArgentina))

