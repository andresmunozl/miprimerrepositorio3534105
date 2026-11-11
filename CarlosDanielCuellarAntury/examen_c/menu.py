import time
sti = ""
contadorp = 0

while True:
    print("****menu****")
    print("1. Numeros pares")
    print("2. Adivina el numero")
    print("3. Salir")
    option = input("elija una opcion: ")
    match option:
        case "1":
            sti = ""
            contadorp = 0
            print("se piden dos numeros y se contaran cuantos numeros pares hay entre ellos")
            while True:
                try:
                    a = int(input("ingrese el primer valor: "))
                    break
                except ValueError:
                    print("ingrese un entero por favor")
            while True:
                try:
                    b = int(input("ingrese el segundo valor valor: "))
                    break
                except ValueError:
                    print("ingrese un entero por favor")
            b += 1
            if a < b:
                for i in range(a, b):
                    if i % 2 == 0:
                        contadorp += 1
                        stin = str(i)
                        sti += stin + " "
                print(f"en total hay {contadorp} pares, los cuales son {sti}")
                time.sleep(2)
            else:
                a += 1
                for i in range(b, a):
                    if i % 2 == 0:
                        contadorp += 1
                        stin = str(i)
                        sti += stin + " "
                print(f"en total hay {contadorp} pares, los cuales son {sti}")
                time.sleep(2)
        case "2":
            contador = 0
            print("adivina el numero secreto digita un valor se te ira dando pisas muy alto te pasaste muy bajo te falta")
            while True:
                try:
                    a = int(input("ingrese un valor: "))
                    break
                except ValueError:
                    print("ingrese un entero por favor")
            while a != 27:
                if a < 27:
                    contador += 1
                    print("muy bajo")
                    while True:
                        try:
                            a = int(input("ingrese un valor: "))
                            break
                        except ValueError:
                            print("ingrese un entero por favor")
                else:
                    contador += 1
                    print("muy alto")
                    while True:
                        try:
                            a = int(input("ingrese un valor: "))
                            break
                        except ValueError:
                            print("ingrese un entero por favor")
                    
            contador += 1  
            print(f"correcto el numero secreto es 27, te tomo un total de {contador} de intentos")
            time.sleep(2)
        case "3":
            break
        case _:
            print("dato invalido por favor elija una opcion")
            time.sleep(1)