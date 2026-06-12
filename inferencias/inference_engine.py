from inferencias.knowledge_base import reglas


def recomendar_producto(datos_usuario):
    """
    Busca coincidencia exacta.
    Si no existe, intenta una recomendación parcial.
    """

    # =====================================
    # BUSQUEDA EXACTA
    # =====================================

    for regla in reglas:

        if (
            regla["nivel"] == datos_usuario["nivel"]
            and regla["presupuesto"] == datos_usuario["presupuesto"]
            and regla["proyecto"] == datos_usuario["proyecto"]
            and regla["categoria"] == datos_usuario["categoria"]
        ):

            return {
                "regla": regla["id"],
                "producto": regla["producto"],
                "explicacion": regla["explicacion"]
            }

    # =====================================
    # INFERENCIA PARCIAL
    # =====================================

    mejor_regla = None
    mayor_puntaje = 0

    for regla in reglas:

        puntaje = 0

        if regla["nivel"] == datos_usuario["nivel"]:
            puntaje += 1

        if regla["presupuesto"] == datos_usuario["presupuesto"]:
            puntaje += 1

        if regla["proyecto"] == datos_usuario["proyecto"]:
            puntaje += 1

        if regla["categoria"] == datos_usuario["categoria"]:
            puntaje += 1

        if puntaje > mayor_puntaje:
            mayor_puntaje = puntaje
            mejor_regla = regla

    # =====================================
    # RECOMENDACION APROXIMADA
    # =====================================

    if mejor_regla and mayor_puntaje >= 2:

        return {
            "regla": "INFERENCIA_PARCIAL",
            "producto": mejor_regla["producto"],
            "explicacion":
                f"No se encontró una coincidencia exacta. "
                f"Se recomienda {mejor_regla['producto']} "
                f"porque comparte varias características "
                f"con la solicitud del usuario."
        }

    # =====================================
    # SIN RECOMENDACION
    # =====================================

    return {
        "regla": "SIN_REGLA",
        "producto": "No se encontró una recomendación.",
        "explicacion": "No existe una regla suficientemente cercana."
    }