import time
while True:
    for horas in range (24): 
        for minutos in range (60):
            for segundos in range(60):  
                time.sleep(1)                                           #tiempo entre lineas 1 segundo
                if horas < 10 and minutos < 10 and segundos < 10:       #3 variables 8 posibles salidas (condiciones)
                    print(f"0{horas}:0{minutos}:0{segundos}")
                elif horas < 10 and minutos < 10 and segundos >= 10:
                    print(f"0{horas}:0{minutos}:{segundos}")
                elif horas < 10 and minutos >= 10 and segundos < 10:
                    print(f"0{horas}:{minutos}:0{segundos}")
                elif horas < 10 and minutos >= 10 and segundos >= 10:
                    print(f"0{horas}:{minutos}:{segundos}")
                elif horas >= 10 and minutos < 10 and segundos < 10:
                    print(f"{horas}:0{minutos}:0{segundos}")
                elif horas >= 10 and minutos < 10 and segundos >= 10:
                    print(f"{horas}:0{minutos}:{segundos}")
                elif horas >= 10 and minutos >= 10 and segundos < 10:
                    print(f"{horas}:{minutos}:0{segundos}")
                else:
                    print(f"{horas}:{minutos}:{segundos}")