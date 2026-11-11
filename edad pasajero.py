edad = int(input("Ingrese la edad del pasajero: "))
if edad < 12:
    print("Aplica tarifa infantil.")
elif edad < 18:
    print("Aplica tarifa juvenil.")
else:
    print("Aplica tarifa general.")
