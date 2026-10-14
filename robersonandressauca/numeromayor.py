print("hola mundo")
num1 = int (input("escriba el primer numero: ")) 
num2 = int (input("escriba el segundo numero: "))
num3 = int (input("escriba el tercer numero: "))
suma = num1 + num2 + num3
print (suma)

if num1 > num2:
    print("El numero mayor es el numero 1")
else:
    print("El numero mayor es el numero 2")
    
if num2 > num3:
    print("El numero mayor es el numero 2")
else:
    print("El numero mayor es el numero 3")
    
# operaodres logicos

if num1 > num2 and num1 > num3:
    print("El numero mayor es el numero 1")
elif num2 > num1 and num3:
    print("El numero mayor el tercero")
num1 = int(input("ingrese el primer número:\n"))
num2 = int(input("ingrese el segundo número:\n"))
num3 = int(input("ingrese el tercer número:\n"))


# menoslineas

if num1 > num2 and num1 > num3:
    print(f"los números ingresados fueron: {num1}, {num2}, {num3}\ny el número mayor es: {num1}")
elif num2 > num1 and num2 > num3:
    print(f"los números ingresados fueron: {num1}, {num2}, {num3}\ny el número mayor es: {num2}")
else:
    print(f"los números ingresados fueron: {num1}, {num2}, {num3}\ny el número mayor es: {num3}")