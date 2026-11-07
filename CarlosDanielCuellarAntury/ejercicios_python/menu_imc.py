while True:
    print("****menu****")
    print("1. imc")
    print("2. saber si un numero es multiplo de otro")
    print("3. salir")
    opcion = input("elija un numero del 1 al 3: ")
    match opcion:
        case "1":
            while True:
                try:
                    kg = float(input("ingrese su peso en kg: "))
                    if kg>0:
                        break
                except ValueError:
                    print("ingrese un dato valido por favor")
            while True:
                try:
                    meters = float(input("ingrese su estatura en metros: "))
                    if meters>0:
                        break
                except ValueError:
                    print("ingrese un dato valido por favor")
            imc =  kg/(meters**2)
            print(round(imc))
            if imc < 18.5 :
                print("bajo peso")
            elif imc >= 18.5 or imc < 25:
                print("peso normal")
            elif imc >= 25 or imc < 30:
                print("Sobrepeso")
            elif imc >= 30 or imc < 35:
                print("Obesidad grado I")
            elif imc >= 35 or imc < 40:
                print("Obesidad grado II")
            else:
                print("Obesidad grado III")
        case "2":
            while True:
                try:
                    nummin = int(input("ingrese el primer numero: "))
                    if nummin>0:
                        break
                except ValueError:
                    print("ingrese un dato valido por favor")
            while True:
                try:
                    nummax = float(input("ingrese el segundo numero: "))
                    if nummax>0:
                        break
                except ValueError:
                    print("ingrese un dato valido por favor")
            if nummax > nummin :
                modulo = nummax % nummin
                if modulo == 0:
                    print(f"el {nummax} es multiplo de {nummin}")
                else:
                    print(f"el {nummin} y el {nummax} no son multiplos")
            else:
                nummin += nummax
                nummax = nummin - nummax
                nummin = nummin - nummax
                
                modulo = nummax % nummin
                if modulo == 0:
                    print(f"el {nummax} es multiplo de {nummin}")
                else:
                    print(f"el {nummin} y el {nummax} no son multiplos")
        case "3":
            break
        case _:
            print("dato invalido")