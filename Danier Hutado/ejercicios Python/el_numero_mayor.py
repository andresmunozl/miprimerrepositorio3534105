num1 = int(input("ingrese el primer número:\n"))
num2 = int(input("ingrese el segundo número:\n"))
num3 = int(input("ingrese el tercer número:\n"))

if num1 > num2 and num1 > num3:
    print("El numero mayor es el numero 1")
elif num2 > num1 and num2 > num3:
    print("El numero mayor es el numero 2")
else:
    print("El numero mayor es el numero 3")