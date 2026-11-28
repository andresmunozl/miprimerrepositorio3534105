productos = []
cantidades = []

while True:
    print(productos)
    print(cantidades)
    print("***inventario***")
    print("1. Agregar producto")
    print("2. Buscar producto")
    print("3. Actualizar cantidad")
    print("4. Eliminar producto")
    print("5. salir")
    opcion = input("elija una opcion del 1 al 5: ")

    match opcion:
        case "1":
            producto = input("ingrese el producto: ")
            # Primero revisamos si ya existe, ANTES de agregarlo
            if producto in productos:
                print("producto ya existe")
            else:
                while True:
                    cantidad = int(input(f"ingrese stock de {producto}: "))
                    if cantidad < 0:
                        print("un valor mayor o igual a 0 por favor")
                    else:
                        productos.append(producto)
                        cantidades.append(cantidad)
                        print(f"producto {producto} agregado")
                        break

        case "2":
            buscar = input("escriba el nombre del producto: ")
            encontrado = False
            for index, producto in enumerate(productos):
                if producto == buscar:
                    print(f"producto encontrado es el producto {producto} con indice #{index} con stock de {cantidades[index]}")
                    encontrado = True
                    break
            if not encontrado:
                print("producto no encontrado")

        case "3":
            actualizar = input("ingrese el producto a actualizar: ")
            indice = -1
            for index in range(len(productos)):
                if productos[index] == actualizar:
                    indice = index
                    break

            if indice == -1:
                print("producto no encontrado")
            else:
                cantidad = int(input("ingrese la cantidad que desea sumar o restar: "))
                print("1. sumar")
                print("2. restar")
                opcion2 = input("elija una opcion 1 o 2 o otra opcion para salir: ")
                match opcion2:
                    case "1":
                        cantidades[indice] += cantidad
                        print(f"nuevo stock de {actualizar}: {cantidades[indice]}")
                    case "2":
                        while cantidades[indice] - cantidad < 0:
                            print(f"cantidad no valida, el stock actual es {cantidades[indice]}")
                            cantidad = int(input("ingrese la cantidad que desea restar: "))
                        cantidades[indice] -= cantidad
                        print(f"nuevo stock de {actualizar}: {cantidades[indice]}")
                    case _:
                        print("saliendo")

        case "4":
            productodel = input("que producto desea eliminar: ")
            encontrado = False
            for index in range(len(productos)):
                if productos[index] == productodel:
                    print(f"se elimino el producto {productos[index]} y el stock de {cantidades[index]}")
                    del cantidades[index]
                    del productos[index]
                    encontrado = True
                    break  # importante: la lista cambió, no seguimos recorriendo
            if not encontrado:
                print("producto no encontrado")

        case "5":
            print("saliendo del programa.")
            break

        case _:
            print("opcion no valida")