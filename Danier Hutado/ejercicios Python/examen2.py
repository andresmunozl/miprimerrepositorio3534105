km = float(input("Ingrese los km recorridos al mes: "))
precio_galon = float(input("Precio del galón de gasolina: "))
precio_kwh = float(input("Precio del kWh: "))
costo_gasolina = (km / 40) * precio_galon
costo_electrico = (km * 0.15) * precio_kwh
print("Costo gasolina:", costo_gasolina)
print("Costo eléctrico:", costo_electrico)
if costo_gasolina < costo_electrico:
    diferencia = costo_electrico - costo_gasolina
    print("Gasolina, ahorra", diferencia)
elif costo_electrico < costo_gasolina:
    diferencia = costo_gasolina - costo_electrico
    print("Eléctrico, ahorra", diferencia)
else:
    print("Cuestan lo mismo")