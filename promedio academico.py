promedio = float(input("Ingrese su promedio académico: "))
matricula_activa = input("¿Tiene matrícula activa? (si/no): ").lower() == "si"
if promedio >= 4.5 and matricula_activa:
    print("Cumple los requisitos preliminares para la beca.")
else:
    print("No cumple los requisitos para la beca.")
