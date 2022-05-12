# Sentencia if/else
condicion = input("Digite True ó False:\n")

if condicion == 'True':
    condicion = True
elif condicion == 'False':
    condicion = False
else:
    print("Ingreso un dato incorrecto")

if condicion == True:
    print('Condición Verdadera')
elif condicion == False:
    print('Condición Falsa')
else:
    print('Condición sin especificar')
