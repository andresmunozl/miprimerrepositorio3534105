num1 = int(input("ingrese el primer número:"))
num2 = int(input("ingrese el segundo número:"))
num3 = int(input("ingrese el tercer número:"))

if num1 > num2 and num1 > num3:
    print("El numero mayor es el numero 1")
elif num2 > num1 and num2 > num3:
    print("El numero mayor es el numero 2")
else:
    print("El numero mayor es el numero 3")
    












if num1 > num2:
    if num1 > num3:
        print("El numero mayor es el numero 1")
    else:
        print("El numero mayor es el numero 3")
elif num2 > num3:
    print("El numero mayor es el numero 2")
else:
    print("El numero mayor es el numero 3")