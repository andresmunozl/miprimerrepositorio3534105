cantidad_ahorrada = float(input("Ingrese la cantidad que lleva ahorrada: "))
meta_ahorro = float(input("Ingrese su meta de ahorro: "))
if cantidad_ahorrada >= meta_ahorro:
    print("¡Felicitaciones! Alcanzó su meta de ahorro.")
else:
    falta = meta_ahorro - cantidad_ahorrada
    print("Aún no alcanza la meta. Le falta ahorrar: $", falta)
