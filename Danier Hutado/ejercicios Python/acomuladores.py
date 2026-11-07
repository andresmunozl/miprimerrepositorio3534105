# contador = 1
# acumulador = 0
# while contador <= 5:
#     precio = int(input("ingrese producto"))
#     acumulador = acumulador + precio
#     contador += 1
# print(f"total a pagar es:{acumulador}")
can_estudiante = 0
promedio = 0
num_estudiante = int(input("ingrese el estudiante(-1 para salir): "))
while num_estudiante  -1:
    nota1 = float(input("indrese la primera nota"))
    nota2 = float(input("ingrese la segunda nota"))
    nota3 = float(input("ingrese la tercera nota"))
    promedio_notas = (nota1 + nota2 + nota3) / 3
    promedio = promedio + promedio_notas
    can_estudiante += 1
    print (f"promedio del estudiante es: {promedio_notas}")
    if promedio_notas >= 3.5:
        print("aprobado")
    else:
        print("no,aprobo")
    print(f"cantidad de estudiantes es: {can_estudiante}")
    print (f"numeros de estudiantes es: {num_estudiante}")
    num_estudiante = int(input("ingrese el estudiante(-1 para salir): "))
print ("programa terminado")      