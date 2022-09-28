# Ejercicio 4: Calculadora de Impuestos
# Crear una función para calcular el total de un pago incluyendo un impuesto aplicado (IVA).
# Formula : pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
# Proporcione el pago sin impuesto: 1000
# Proporcione el monto del impuesto: 21%
# Pago con impuesto: xxxx

def calculo_pago_total(pago, impuesto):
    return pago + pago * (impuesto/100)

pagoSinImpuesto = float(input("Proporcione el pago sin impuesto: "))
impuestoParaAplicar = float(input("Proporcione el monto del impuesto: "))
pagoTotal = calculo_pago_total(pagoSinImpuesto, impuestoParaAplicar)
print(f"El pago total con impuesto incluido es: {pagoTotal}")

