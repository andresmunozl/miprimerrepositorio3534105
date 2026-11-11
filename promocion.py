compra = float(input("Ingrese el valor de la compra: "))
fidelizado = input("¿Pertenece al programa de fidelización? (si/no): ").lower() == "si"
if compra > 150000 or fidelizado:
    print("Aplica a la promoción comercial.")
else:
    print("No aplica a la promoción.")
