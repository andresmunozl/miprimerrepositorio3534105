usuario_ingresado = input("Ingrese su nombre de usuario: ")

if usuario_ingresado == "admin" or usuario_ingresado == "aprendiz":
    autorizacion_vigente = input("¿Su autorización se encuentra vigente? (si/no): ").lower() == "si"
    if autorizacion_vigente:
        print("Acceso concedido exitosamente.")
    else:
        print("Acceso denegado: Su autorización ha expirado.")
else:
    print("Acceso denegado: Usuario no registrado o autorizado.")
