nota = float(input("Ingrese una nota académica: "))
nota_valida = (nota >= 0) and (nota <= 5)
print("¿La nota está en el rango válido de 0 a 5?", nota_valida)
