inscrito = input("¿Está inscrito? (si/no): ").lower() == "si"
identificacion = input("¿Presentó identificación? (si/no): ").lower() == "si"
if inscrito and identificacion:
    print("Cumple ambos requisitos de acceso.")
else:
    print("No cumple con los requisitos.")
