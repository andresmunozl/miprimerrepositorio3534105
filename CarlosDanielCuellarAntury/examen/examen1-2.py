fot = int(input("ingrese numero de fotos: \n"))                     #for = numero de fotos
mb  = int(input("ingrese tamaño promedio de cada foto en MB: \n"))  #mb  = megabytes
gb  = (fot * mb) / 1000 #gb  = gigabytes
pba = 8000*12           #pba = plan basico anual
ppa = 2000*12           #ppa = plan premiun anual
if gb < 0:
    print("datos invalidos")
elif gb <= 15:
    print(f"usted posee el plan Gratuito.\ntiene un costo de $0 al año \nha ocupado un total de {gb} GB")
elif gb > 15 and gb <= 100:
    print(f"usted posee el plan Basico. \ntiene un costo de ${pba} al año \nha ocupado un total de {gb} GB")
else:
    print(f"usted posee el plan Premiun. \ntiene un costo de ${ppa} al año \nha ocupado un total de {gb} GB")
