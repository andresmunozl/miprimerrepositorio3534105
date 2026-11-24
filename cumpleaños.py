edad = int(input("Ingrese su edad: "))
doc_vigente = input("¿Tiene documento vigente? (si/no): ").lower() == "si"
cumple = (edad >= 18) and doc_vigente
print("¿Cumple los requisitos de inscripción?", cumple)
