elementos = int(input("Cantidad total de elementos: "))
personas = int(input("Número de personas: "))
por_persona = elementos // personas
sobrantes = elementos % personas
print("Cada persona recibe:", por_persona, "y sobran:", sobrantes)
