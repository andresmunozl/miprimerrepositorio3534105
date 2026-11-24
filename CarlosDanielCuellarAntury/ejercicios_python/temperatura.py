temperaturas =  []
for index in range(5):
    temperatura = float(input(f"ingrese la temperatura #{index + 1}: "))
    temperaturas.append(temperatura)

prom = sum(temperaturas)/len(temperaturas)
print(prom)
sums = 0
ind =   ""
for index, temperatura in enumerate(temperaturas):
    if temperatura > prom:
        print(f"la temperatura {temperatura} es mayor al promedio de {prom} en el indice {index + 1}")
        sums += 1
        ind  += str(index + 1) + " "
    elif temperatura < prom:
        print(f"la temperatura {temperatura} es menor al promedio de {prom} en el indice {index + 1}")
    else:
        print(f"la temperatura {temperatura} es igual al promedio de {prom} en el indice {index + 1}")
print(f"las temperaturas que soperan el promedio son {3} y son los de temperatura con indice: {ind}")