segundos_totales = int(input("Ingrese la cantidad total de segundos: "))
minutos_completos = segundos_totales // 60
segundos_restantes = segundos_totales % 60
print("Equivale a:", minutos_completos, "minutos y", segundos_restantes, "segundos.")
