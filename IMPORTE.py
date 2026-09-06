importe = float(input("¿cuánto es el importe de la cuenta?: "))
personas = int(input("¿cuántas personas van a pagar la cuenta?: "))
servicio = input("te gusto el servicio? (si/no):")

if servicio == "si":
    propina = importe * 0.15
else:
    propina = 0

total = importe + propina
pago_por_persona = total / personas
print(f"El total a pagar es: {round(total, 2)}")
print(f"El total por persona es: {round(pago_por_persona, 2)}")