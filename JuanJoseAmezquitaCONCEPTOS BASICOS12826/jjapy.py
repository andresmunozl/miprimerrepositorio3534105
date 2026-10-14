num1 = int(input('ingrse el primer numero:'))
num2 = int(input('ingrse el segundo numero:'))
num3 = int(input('ingrse el tercer numero:'))

# print  (max())
print(f'Los numeros ingresado fureon: {num1}, {num2}, {num3}.')
if num1 > num2 and num1 > num3:
        print(f'El numero mayor es el primero: {num1}')      
elif num2 > num3 and num2 > num3:
    print(f'El numero mayor es eñ segundo: {num2}')
else:
    print(f'El numero mayor es el: {num3}')
