while True:
    # 1. Validación de cantidad de estudiantes (no acepta 0 ni negativos)
    n = int(input("ingrese numero de estudiantes: "))
    if n <= 0:
        print("dato invalido no puedes tener 0 estudiantes ni negativos")
        continue

    option = ""  # Variable para controlar la salida en caso de presionar -1

    # 2. Ciclo de estudiantes
    for i in range(n):
        prom = 0  # Se reinicia en 0 para cada estudiante
        while True:
            try:
                numnotas = int(input(f"ingrese numero de notas que tiene el estudiante {i+1}: "))
                if numnotas > 0:
                    break
                else:
                    print("el numero de notas debe ser mayor que cero")
            except ValueError:
                print("ingrese un valor valido")
        
        for notas in range(numnotas):
            while True:
                nota = float(input(f"ingrese nota del estudiante {i + 1}, nota{notas + 1}: "))

                #valida si está fuera de rango (menor a 0 o mayor a 5) y diferente de -1
                if (nota < 0 or nota > 5) and nota != -1:
                    print("ingrese un numero de 0 a 5 o presione -1 para salir")

                elif nota == -1:
                    print("desea salir")
                    while True:
                        option = input("si/no : ")
                        match option:
                            case "si" | "SI" | "Si" | "sI" | "s" | "S":
                                break
                            case "NO" | "No" | "no" | "nO" | "n" | "N":
                                break
                            case _:
                                print("dato invalido")

                    # Evalúa la respuesta elegida
                    match option:
                        case "si" | "SI" | "Si" | "sI" | "s" | "S":
                            break  # Rompe el ciclo 'while True' de la nota actual
                        case "NO" | "No" | "no" | "nO" | "n" | "N":
                            continue  # Vuelve a pedir la nota actual

                else:
                    prom += nota
                    break  # Nota válida: rompe el 'while True' para pasar a la siguiente nota

            # Si se eligió "si", rompe el ciclo 'for notas'
            match option:
                case "si" | "SI" | "Si" | "sI" | "s" | "S":
                    break
        match option:
            case "si" | "SI" | "Si" | "sI" | "s" | "S":
                break

        # Si no se salió, calcula y muestra el promedio del estudiante
        prom = prom / numnotas
        if prom >= 3.5:
            print(f"el estudiante aprobo con {prom}")
        else:
            print(f"el estudiante no aprobo su nota fue de: {prom}")

    match option:
        case "si" | "SI" | "Si" | "sI" | "s" | "S":
            break
#si quiero salir de forma automatica una vez finalizado los n estudiantes
        case _:
            break