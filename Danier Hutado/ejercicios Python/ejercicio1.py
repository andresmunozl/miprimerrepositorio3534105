precio_producto = float(input("introduce el precio del producto"))
presupuesto = precio_producto * 2.5 
if presupuesto > 10000 :
    print("¡presupuesto valido! si se puede comprar.")
else:
    print("no tienes dinero suficiente para comprarlo")
    