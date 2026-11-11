producto = input("Nombre del producto: ")
precio = float(input("Precio unitario: "))
cantidad = int(input("Cantidad: "))
subtotal = precio * cantidad
print("--- FACTURA ---")
print("Producto:", producto, "x", cantidad)
print("Subtotal a pagar: $", subtotal)
