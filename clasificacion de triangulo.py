lado1 = float(input("Ingrese la longitud del primer lado: "))
lado2 = float(input("Ingrese la longitud del segundo lado: "))
lado3 = float(input("Ingrese la longitud del tercer lado: "))

if lado1 > 0 and lado2 > 0 and lado3 > 0:
    # Comprobar si los lados cumplen la desigualdad triangular
    if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
        print("Los lados ingresados forman un triángulo válido.")
    else:
        print("Los lados ingresados NO pueden formar un triángulo.")
else:
    print("Error: Todas las longitudes deben ser valores positivos.")
