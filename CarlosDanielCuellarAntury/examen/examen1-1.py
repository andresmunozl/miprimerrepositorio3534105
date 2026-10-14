while True:
    try:
        lon = int(input("ingrese la longitud de la contraseña \n"))
        if lon <= 0:
            print("dato invalido")
            continue
        break
    except ValueError:
        print("solo se aceptan números enteros")   

while True:
    print("¿la contraseña tiene mezcla?")
    print("1. con mezcla")
    print("2. sin mezcla")
    opcion = input("seleccione una opcion: \n")
    match opcion:
        case "1"|"con mezcla":
            if lon < 8:
                print("la contraseña tiene nivel Debil")
            elif lon >= 8 and lon <= 11:
                print("la contraseña tiene nivel Medio")
            elif lon >= 12 and lon <= 15:
                print("la contraseña tiene nivel Fuerte")
            else:
                print("la contraseña tiene nivel muy Fuerte")
            break
        case "2"|"sin mezcla":
                        if lon < 8:
                            print("la contraseña tiene nivel debil")
                        elif lon >= 8 and lon <= 11:
                            print("la contraseña tiene nivel debil")
                        elif lon >= 12 and lon <= 15:
                            print("la contraseña tiene nivel Media")
                        else:
                            print("la contraseña tiene nivel Fuerte")
                        break
        case _:
            print("respuesta invalida por favor responda: ")