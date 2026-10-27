# numeros = []

# for i in range(5):
#     while True:
#         try:
#             numeros.append(int(input(f"{i+1}.ingrese un numero: ")))
#             break
#         except ValueError:
#             print("ingrese un entero por favor")

# for i, numero in enumerate(numeros):
#     residuo = numero % 2
#     if residuo == 0:
#         print(f"{i+1} el numero {numero} es par")
#     else:
#         print(f"{i+1} el numero {numero} es impar")


while True:
    while True:
        try:
            n = int(input("ingrese un numero:"))
            break
        except ValueError:
            print("ingrese un entero por favor")
    residuo = n % 3
    if residuo == 0 and n != 0:
        print(f"el numero {n} es multiplo de 3 ")
    elif n == 0:
        print("fin del codigo")
        break
    else:
        print(f"el numero {n} no es multiplo de 3 ")