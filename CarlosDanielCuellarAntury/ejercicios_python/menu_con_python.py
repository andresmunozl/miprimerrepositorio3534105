import time
while True:
    print("****menu de opciones en python****")
    print("1. sumar 2 numeros")
    print("2. restar 2 numeros num1 - num2")
    print("3. Multiplicar 2 numeros")
    print("4. salir")
    print("5. division entre 2 numeros num1/num2")

    opcion  = input("seleccione entre 1 y 5: ")
    match opcion:
        case "1":
            while True:
                try:
                    num1 = float(input("ingrese primer numero por favor: "))
                    break  
                except ValueError:
                    print("ingrese un dato valido por favor")
            while True:    
                try:
                    num2 = float(input("ingrese primer numero por favor: "))
                    break  
                except ValueError:
                    print("ingrese un dato valido por favor")   
            suma = num1 + num2
            print(f"el resultado es {suma}")
            time.sleep(5)
        case "2":
            while True:
                try:
                    num1 = float(input("ingrese primer numero por favor: "))
                    break  
                except ValueError:
                    print("ingrese un dato valido por favor")
            while True:    
                try:
                    num2 = float(input("ingrese primer numero por favor: "))
                    break  
                except ValueError:
                    print("ingrese un dato valido por favor")   
            restar = num1 - num2   
            print(f"el resultado es {restar}")
            time.sleep(5)
        case "3":
            while True:
                try:
                    num1 = float(input("ingrese primer numero por favor: "))
                    break  
                except ValueError:
                    print("ingrese un dato valido por favor")
            while True:    
                try:
                    num2 = float(input("ingrese primer numero por favor: "))
                    break  
                except ValueError:
                    print("ingrese un dato valido por favor")   
                
            multiplicar = num1 * num2
            print(f"el resultado es {multiplicar}")
            time.sleep(5)
        case "4":
            break
        case "5":
            while True:
                try:
                    num1 = float(input("ingrese primer numero por favor: "))
                    break  
                except ValueError:
                    print("ingrese un dato valido por favor")
            while True:    
                try:
                    num2 = float(input("ingrese primer numero por favor: "))
                    if num2 == 0:
                        print("el numero debe ser distinto de 0")
                    else:
                        break
                except ValueError:
                    print("ingrese un dato valido por favor")   
            dividir = num1/num2
            print(f"el resultado es {dividir}")
            time.sleep(5)
            
        case _:
            print("valor invalido")
            time.sleep(1)