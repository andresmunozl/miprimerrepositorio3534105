art1    =   float(input("ingrese el valor del producto 1: \n ")) # de articulo 1
art2    =   float(input("ingrese el valor del producto 2: \n ")) # de articulo 2
art3    =   float(input("ingrese el valor del producto 3: \n ")) # de articulo 3
art4    =   float(input("ingrese el valor del producto 4: \n ")) # de articulo 4
art5    =   float(input("ingrese el valor del producto 5: \n ")) #articulo 5
precio    =    art1    +   art2    +   art3    +   art4    +   art5
if precio > 100000  :
    preciof =   precio*0.8
    print(f"el precio final es {preciof} decuento aplicado de: {precio*0.2}")
else:
    preciof =   precio  -   (art1)
    print(f"el precio final es {preciof} descuento aplicado {art1}")