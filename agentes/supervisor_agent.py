def generar_reporte(datos_cliente, resultado):

    print("\n========== REPORTE DEL SISTEMA ==========\n")

    print(f"Nivel: {datos_cliente['nivel']}")
    print(f"Presupuesto: {datos_cliente['presupuesto']}")
    print(f"Proyecto: {datos_cliente['proyecto']}")
    print(f"Categoría: {datos_cliente['categoria']}")

    print("\n---------- RESULTADO ----------\n")

    print(f"Regla activada: {resultado['regla']}")
    print(f"Producto recomendado: {resultado['producto']}")

    print("\n---------- EXPLICACIÓN ----------\n")

    print(resultado["explicacion"])

    print("\n========================================\n")