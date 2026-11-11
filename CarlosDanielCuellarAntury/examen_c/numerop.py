numero = int(input("Ingrese un numero mayot que 1: "))
es_primo = True
divisor = 2 # numero primo es divisible entre si y entre 1
divisores = 0
while divisor < numero:
    if numero % divisor == 0: # error = en lugar de == 
        es_primo = False # false no tiene la f minuscula es la palabra es False
        divisores = divisores + 1
    divisor = divisor + 1
if es_primo:
    print(numero, "es primo")
else:
    print(numero, "no es primo")
    print("Tiene", divisores, "divisores entre 2 y el numero anterior")
suma = 0
for i in range(1, numero+1): #error la el for debe estar en un ranfo de 1, numero + 1 rango toma el valor -1
    suma = suma + i
print("Suma de 1 hasta", numero, "es", suma)