productos = []
cantidades = []
while True:
    print(productos)
    print(cantidades)
    print("***menu***")
    print("1. Agregar producto")
    print("2. Buscar producto")
    print("3. Actualizar cantidad")
    print("4. Eliminar producto")
    print("5. salir")
    opcion = input("elija una opcion del 1 al 5: ")
    match opcion:
        case "1":
            producto = input("ingrese el producto: ")
            productos.append(producto)
            for index in range(len(productos)):
                if (productos[-1] == productos[index]) and len(productos)>1:
                    print("producto ya existe")
                    break
                elif productos[-1] == producto:
                    while True:
                        cantidad = int(input(f"ingrese stock de {producto}: "))
                        if cantidad < 0:
                            print ("un valor mayor o igual a 0 por favor")
                        else:    
                            cantidades.append(cantidad)
                            break
        case "2":
            buscar = input("escriba el nombre del producto: ")
            for index, producto in enumerate(productos):
                if producto == buscar:
                    print(f"producto encontrado es el producto {producto} con indice #{index} con stock de {cantidades[index]}")
                else:
                    print("producto no encontrado")
        case "3":
            actualizar = input("ingrese el producto a actualizar ")
            cantidad   =    int(input("ingrese la cantidad que desea sumar o restar"))
            print("1. sumar")
            print("2. restar")
            opcion2 = input("elija una opcion 1 o 2 o otra opcion para salir: ")
            match opcion2:
                case "1":
                    for index in range(len(productos)):
                        if actualizar == producto[index]:
                            cantidades[index] += cantidad
                        else:
                            print("producto no encontrado")
                case "2":
                    for index in range(len(productos)):
                        if actualizar == producto[index]:
                            while True:
                                cantidades[index] -= cantidad
                                if cantidades[index] < 0:
                                    print("cantidad no valida")
                                    cantidades[index] += cantidad
                                    cantidad = input("ingrese la cantidad que desea sumar o restar")
                                else:
                                    break
                        else:
                            print("producto no encontrado")
                case _ :  
                    print("saliendo")
        case "4":
            productodel=input("que producto desea eliminar")
            for index in range(len(productos)):
                if productos[index] == productodel:
                    print(f"se elimino el producto {productos[index]} y el stock de {cantidades[index]}")
                    cantidades.remove(cantidades[index])
                    productos.remove(productos[index])