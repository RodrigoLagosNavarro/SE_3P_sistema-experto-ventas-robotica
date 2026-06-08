from inferencias.knowledge_base import reglas


def recomendar_producto(datos_usuario):
    """
    Busca una regla que coincida con las respuestas del usuario.
    """

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

    return {
        "regla": "SIN_REGLA",
        "producto": "No se encontró una recomendación.",
        "explicacion": "No existe una regla para esta combinación."
    }