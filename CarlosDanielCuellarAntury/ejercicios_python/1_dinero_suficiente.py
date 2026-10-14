vc  =   float(input("ingrese el valor del producto"))
dc  =   float(input("ingrese cuanto tiene: "))
ldc =   float(vc*2.5)

if  dc  <=   10000 :
    print("no cumple el rango de presupuesto")
elif dc <   vc  :
    print("no tienes dinero suficiente para comprarlo")
elif dc >   vc  :
    print("te alcanza para el producto")
else:
    print("no cumple el rango de presupuesto")