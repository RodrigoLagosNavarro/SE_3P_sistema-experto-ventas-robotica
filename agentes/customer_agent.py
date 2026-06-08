def obtener_datos_cliente():

    print("\n===== SISTEMA EXPERTO DE ROBÓTICA =====\n")

    nivel = input(
        "Nivel de experiencia (principiante/intermedio/avanzado): "
    ).lower()

    presupuesto = input(
        "Presupuesto (bajo/medio/alto): "
    ).lower()

    proyecto = input(
        "Proyecto (educacion/iot/automatizacion/robotica_movil/vision_artificial): "
    ).lower()

    categoria = input(
        "Categoría (controlador/sensor/actuador/kit): "
    ).lower()

    return {
        "nivel": nivel,
        "presupuesto": presupuesto,
        "proyecto": proyecto,
        "categoria": categoria
    }