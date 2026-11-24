nombre_persona = input("Nombre del trabajador: ")
horas_trabajadas = float(input("Ingrese las horas trabajadas: "))
pago_por_hora = float(input("Ingrese el valor del pago por hora: "))
pago_total = horas_trabajadas * pago_por_hora
print("El pago total para", nombre_persona, "es de: $", pago_total)
