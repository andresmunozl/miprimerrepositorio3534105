contadorf = 0 #frio
contadort = 0 #templado
contadorc = 0 #caluroso
while True:
    while True:
        try:
            grados = float(input("ingrese la temperatura en celcius (c°): "))
            if grados < 15 and grados != -100:
                contadorf += 1
                print(f"Frio. \n dias frios: {contadorf}")
            elif grados >= 15 and grados <= 25:
                contadort += 1
                print(f"Templado. \n dias Templados: {contadort}")
            elif grados > 25 and grados != -100:
                contadorc += 1
                print(f"Caluroso. \n dias Calurosos: {contadorc}")
            else:
                break
        except ValueError:
            print("digite un dato valido o -100 para salir")
    break
totalday = contadorf + contadort + contadorc
print(f"dias frios: {contadorf}")
print(f"dias Templados: {contadort}")
print(f"dias Calurosos: {contadorc}")
print(f"dias transcurridos {totalday}")