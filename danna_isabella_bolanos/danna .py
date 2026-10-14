num1 = int(input("ingrese el primer número:\n"))
num2 = int(input("ingrese el segundo número:\n"))
num3 = int(input("ingrese el tercer número:\n"))

if num1 > num2 and num1 > num3:
    print(f"los número ingresados fueron: {num1}, {num2}, {num3}\ny el número mayor es: {num1}")
elif num2 > num1 and num2 > num3:
    print(f"los número ingresados fueron: {num1}, {num2}, {num3}\ny el número mayor es: {num2}")
else:
    print(f"los número ingresados fueron: {num1}, {num2}, {num3}\ny el número mayor es: {num3}")
  