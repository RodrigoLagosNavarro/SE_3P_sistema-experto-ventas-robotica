from inferencias.inference_engine import recomendar_producto


def procesar_solicitud(datos_cliente):

    resultado = recomendar_producto(datos_cliente)

    return resultado