nm  =   int(input("cuanto duro la llamada: "))   #numero de minutos

print("a que zona llamo")
print("1. America Del norte")
print("2. America central")
print("3. America del sur")
print("4 Europa")
print("5. Asia")
opcion  =   input("ingrese zona o numero de opcion: ")
match opcion:
    case "1" |  "America Del norte":
        if nm   >=  3:
            pllam   =   nm*200
            print(f"el costo de la llamada es {pllam}")
        else:
            pllam   =   nm*150
            print(f"el costo de la llamada es {pllam}")
    case "2" |  "America central":
        if nm   >=   3:
            pllam   =   nm*220
            print(f"el costo de la llamada es {pllam}")
        else:
            pllam   =   nm*200
            print(f"el costo de la llamada es {pllam}")
    case "3" |  "America del sur":
        if nm   >=   3:
            pllam   =   nm*300
            print(f"el costo de la llamada es {pllam}")
        else:
            pllam   =   nm*280
            print(f"el costo de la llamada es {pllam}")
    case "4" |  "Europa":
        if nm   >=   3:
            pllam   =   nm*550
            print(f"el costo de la llamada es {pllam}")
        else:
            pllam   =   nm*510
            print(f"el costo de la llamada es {pllam}")
    case "5" |  "Asia":
        if nm   >=   3:
            pllam   =   nm*600
            print(f"el costo de la llamada es {pllam}")
        else:
            pllam   =   nm*540
            print(f"el costo de la llamada es {pllam}")
    case _:
        print("invalido por favor lea las instrucciones")