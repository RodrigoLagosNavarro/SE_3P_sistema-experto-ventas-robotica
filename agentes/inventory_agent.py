from base_datos.database import obtener_stock
from inferencias.knowledge_base import productos


def sugerir_alternativa(producto_original):

    producto_base = None

    for producto in productos:

        if producto["nombre"] == producto_original:
            producto_base = producto
            break

    if not producto_base:
        return None

    for producto in productos:

        if producto["nombre"] == producto_original:
            continue

        mismo_proyecto = (
            producto["proyecto"]
            == producto_base["proyecto"]
        )

        misma_categoria = (
            producto["categoria"]
            == producto_base["categoria"]
        )

        if mismo_proyecto and misma_categoria:

            stock = obtener_stock(
                producto["nombre"]
            )

            if stock > 0:

                return {
                    "producto": producto["nombre"],
                    "motivo":
                    "Comparte categoría y proyecto similares."
                }

    return None