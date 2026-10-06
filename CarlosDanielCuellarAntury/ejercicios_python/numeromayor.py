num1 = int(input("ingrese el primer numero: \n"))
num2 = int(input("ingrese el segundo numero: \n"))
num3 = int(input("ingrese el recer nuemero numero: \n"))
#regla numeros iguales con operadores logicos
if num1 == num2 and num3 == num2 :
    print("los tres numeros son iguales, el numero es", num1)
#regla numeros repetidos
elif num1 == num2 and num1 > num3:
    print(f"los numeros ingresados son {num1}, {num2}, {num3}, el primer y segundo numero son iguales y el numero mayor es: {num1}")
elif num2 == num3 and num2 > num1:
    print(f"los numeros ingresados son {num1}, {num2}, {num3}, el tercer y el segundo numero son iguales y el numero mayor es: {num2}")
elif num1 == num3 and num1 > num2:
    print(f"los numeros ingresados son {num1}, {num2}, {num3}, el primer y tercer numero son iguales y el numero mayor es: {num1}")
elif num1 > num2 and num1 > num3:
    print(f"los numeros ingresados son {num1}, {num2}, {num3}, y el numero mayor es: {num1}")
elif num2 > num1 and num2 > num3:
    print(f"los numeros ingresados son {num1}, {num2}, {num3}, y el numero mayor es: {num2}")
else:
    print(f"los numeros ingresados son {num1}, {num2}, {num3}, y el numero mayor es: {num3}")






















# #regla numeros iguales
# if num1 == num2 :
#     if num2 == num3 :
#         print("todos los numeros son iguales, el numero es:", num1)
# #regla numeros repetidos
# elif num1 == num2 :
#     if num2 > num3 :
#         print("el primer y segundo numero son igual y son los mayores, el numero es:", num1)
#     else:
#         print("el mayor es el tercero, el numero es:", num3)
# elif num2 == num3:
#     if num2 > num1 :
#         print("el segundo numero y el tercero son iguales y son los mayores, el numero es:", num2)
#     else:
#         print("el primer numero es el mayor, el numero es:", num1)
# elif num1 == num3:
#     if num1 > num2 :
#         print("el primer numero y el tercero son iguales y son los mayores, el numero es:", num1)
#     else:
#         print("el segundo numero es el mayor, el numero es:", num2)
# #regla numeros distintos
# elif num1 > num2 :
#     if num1 > num3 :
#         print("el mayor es el primer numero, el numero es:", num1)
#     else:
#         print("el mayor es el tercer numero, el numero es:", num3)
# else:
#     if num2 > num3 :
#         print("el mayor es el segundo numero, el numero es:", num2)
#     else:
#         print("el mayor es el tercer numero, el numero es:", num3)