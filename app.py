from agentes.customer_agent import obtener_datos_cliente
from agentes.sales_agent import procesar_solicitud
from agentes.supervisor_agent import generar_reporte


def main():

    datos_cliente = obtener_datos_cliente()

    resultado = procesar_solicitud(datos_cliente)

    generar_reporte(datos_cliente, resultado)


if __name__ == "__main__":
    main()