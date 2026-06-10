import streamlit as st

from agentes.sales_agent import procesar_solicitud
from agentes.supervisor_agent import generar_reporte
from base_datos.database import crear_base_datos, guardar_consulta


crear_base_datos()

st.set_page_config(
    page_title="Sistema Experto de Robótica",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Sistema Experto de Ventas para Robótica")

st.write(
    "Obtenga recomendaciones de componentes y kits "
    "de robótica mediante reglas de conocimiento."
)

nivel = st.selectbox(
    "Nivel de experiencia",
    ["principiante", "intermedio", "avanzado"]
)

presupuesto = st.selectbox(
    "Presupuesto",
    ["bajo", "medio", "alto"]
)

proyecto = st.selectbox(
    "Tipo de proyecto",
    [
        "educacion",
        "iot",
        "automatizacion",
        "robotica_movil",
        "vision_artificial"
    ]
)

categoria = st.selectbox(
    "Categoría",
    [
        "controlador",
        "sensor",
        "actuador",
        "kit"
    ]
)

if st.button("Generar recomendación"):

    datos_cliente = {
        "nivel": nivel,
        "presupuesto": presupuesto,
        "proyecto": proyecto,
        "categoria": categoria
    }

    resultado = procesar_solicitud(datos_cliente)

    guardar_consulta(datos_cliente, resultado)

    st.success("Recomendación generada")

    st.subheader("Producto recomendado")
    st.write(resultado["producto"])

    st.subheader("Regla activada")
    st.write(resultado["regla"])

    st.subheader("Explicación")
    st.write(resultado["explicacion"])