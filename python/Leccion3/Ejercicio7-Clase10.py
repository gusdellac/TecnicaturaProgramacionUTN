# Ejercicio 8: Dadas las horas trabajadas de 5 personas
# y la tarifa de pago, calcular el salario y la sumatoria
# de todos los salarios.
i = 1
suma = 0
while i <= 5:
    print(f"Salario del empleado {i}: ")
    horas = int(input("Digite las horas trabajadas: "))
    tarifa = int(input("Digite la tarifa por hora: "))
    salario = horas*tarifa
    print(f"El salario es: $ {salario}")
    suma += salario
    i += 1
print(f"\nLa suma de todos los salarios es: $ {suma}")

