texto = input("ingrese un texto:\n")
stringinv = ""
contador = 0
for letra in texto:
    contador += 1 # usamos el contador para extraer el indice

indice = contador - 1
for _ in range(contador):
    if indice >= 0:
        stringinv   += texto[indice]
        indice -=   1
print(stringinv)

# for letra in texto:
#     stringinv = letra + stringinv
# print(stringinv)