porcentaje = float(input("Ingrese el porcentaje de cumplimiento: "))
if porcentaje < 60:
    print("Nivel: Bajo")
elif porcentaje < 80:
    print("Nivel: Medio")
elif porcentaje < 95:
    print("Nivel: Alto")
else:
    print("Nivel: Excelente")
