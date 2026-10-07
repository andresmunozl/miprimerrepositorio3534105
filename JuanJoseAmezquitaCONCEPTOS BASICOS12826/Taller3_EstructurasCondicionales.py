# 1.
presupuesto = float(input('Ingrese el precio del presupuesto: '))

precio = float(input('Ingrse el precioo:'))

if presupuesto <= 10000:
    print('El presupuesto debe ser mayor a 10.000')
elif precio > presupuesto:
    print('no tiene sufiioente dinero: ')
else:
    print('puede comprar el producto: ')
    
# -----------------------------------------------------------    

# 2.

total = 0

valor_producto1 = float(input('Introduse el valor del producto1: '))
valor_producto2 = float(input('Introduse el valor del producto2: '))
valor_producto3 = float(input('Introduse el valor del producto3: '))
valor_producto4 = float(input('Introduse el valor del producto4: '))
valor_producto5 = float(input('Introduse el valor del producto5: '))

total = valor_producto1 + valor_producto2 + valor_producto3 + valor_producto4 + valor_producto5

print(f'Total de la compra: {total}')

if total > 100000:
    descuento = total * 0.20
else:
    descuento = total - valor_producto1

total_pagar = total - descuento

print('El total es:', total)
print('Descuento:', descuento)
print('Total a pagar:', total_pagar)


# ----------------------------------------

# 3.
indicativo = int(input('Ingree el indicativo: '))
minutos= int (input('Ingrese los minutos: '))

if indicativo == 12:
    precio_inicial = 200
    precio_adicional = 150
elif indicativo == 18:

#------------------------------------------------------

# 4
distancia_ida = float(input('ingrese la distancia de ida: '))
tiempEstancia  = float(input('ingese los dias de estancisa: '))

preciokm = 1230

distancia_total = distancia_ida * 2

precio4 = distancia_total * precio_km
