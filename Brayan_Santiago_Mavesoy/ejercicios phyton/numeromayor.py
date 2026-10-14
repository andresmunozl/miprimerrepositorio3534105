num1 = int(input("ingrese el primer numero:\n")) 
num2 = int(input("ingrese el segundo numero:\n"))
num3 = int(input("ingrese el tercer numero:\n"))

if num1 > num2 and num1 > num3:
    print(input("ingrese el primer numero:\n")) 
elif num2 > num1 and num2 > num3:
    print(input("ingrese el primer numero:\n")) 
else:
    print("el numero mayor es el numero 3")



if num1 > num2:
    if num1 > num3:
        print("el numero mayor es el numero 1")
    else: 
        print("el numero mayor es el numero 3")
elif num2 > num3:
    print("el numero mayor es el numero 2")
else:
    print("el numero mayor es el numero 3")    



num1 = int(input("ingrese el primer número: \n"))
num2 = int(input("ingrese el segundo número: \n"))
num3 = int(input("ingrese el tercer número: \n"))
if num1 > num2 and num1 > num3:
    print(f"los número ingresados fueron: {num1}, {num2}, {num3}\ny el número mayor es: {num1}")
elif num2 > num1 and num2 > num3:
    print(f"los nimero ingresados fueron: {num1}, {num2}, {num3}\ny el número mayor es: {num2}")
else:
    print(f"los número ingresados fueron: {num1}, {num2}, {num3}\ny el número mayor es: {num3}")
