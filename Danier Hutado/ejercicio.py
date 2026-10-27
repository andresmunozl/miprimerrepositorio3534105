print("---sistema para calculo de nota de estudiante---")
cant_estudiantes = int(input("ingrese el numero de estudiantes: "))
cont_estudiantes = 1

while cont_estudiantes <= cant_estudiantes:
    acom_notas = 0
    cont_notas = 1
    cant_notas = int(input("ingrese la cantidad de notas: "))

    while cont_notas <= cant_notas:
         nota = float(input(f"ingrese la nota #{cont_notas} del estudiante #{cont_estudiantes}:"))
         acom_notas = acom_notas + nota
         cont_notas += 1
    promedio = acom_notas / cant_notas
    aprobo = False
    if aprobo >= 3.5:
         aprobo = True
    else:
         aprobo = False
    if aprobo:
         print("el estudian aprobo")
    else:
         print("el estudiante no aprobo")
cont_estudiantes += 1                   