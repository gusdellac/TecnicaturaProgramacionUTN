"""
Ejercicio 6: Etapas de vida
Haremos un programa que cuando el usuario ingrese su edad le diga
o imprima la etapa de su vida en una breve oración:
"""
etapa = None
edad = int(input("Digite su edad (0 - 29): "))
if (edad >= 0) and (edad <= 10):
    etapa = "La infancia es increíble y bella"
elif (edad >= 11) and (edad <= 19):
    etapa = "Tienes muchos cambios, mucho que estudiar"
elif (edad >= 20) and (edad <= 29):
    etapa = "Amor y comienza el trabajo"
else:
    etapa = "El valor ingresado no está dentro del rango indicado"
print(f"La etapa de vida para {edad} año/s es: {etapa}")