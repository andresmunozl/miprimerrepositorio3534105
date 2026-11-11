es_instructora = input("¿Es instructora? (si/no): ").lower() == "si"
tiene_autorizacion = input("¿Tiene autorización? (si/no): ").lower() == "si"
acceso = es_instructora or tiene_autorizacion
print("¿Puede acceder al recurso?", acceso)
