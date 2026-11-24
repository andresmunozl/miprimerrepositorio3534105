horas = int(input("Ingrese la cantidad de horas de estacionamiento: "))

# Rangos definidos: 1 a 2 horas = $2000/h, 3 a 5 horas = $1500/h, más de 5 horas = tarifa fija de $10000
if horas <= 2:
    total_parqueadero = horas * 2000
elif horas <= 5:
    total_parqueadero = horas * 1500
else:
    total_parqueadero = 10000

print("El costo total del parqueadero según las horas ingresadas es: $", total_parqueadero)
