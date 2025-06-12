import streamlit as st
from utils.load_data import load_data
from utils.lists import load_all_lists
from utils.metrics import met_categoria, met_mensajes_dias, met_totales, met_insights, costo_acumulado, costo_diario
from utils.lists_metrics import met_listas_dias, met_listas_programas, met_listas_totales, met_lists_insights, heatmap_programa_fecha, contactos_unicos_por_programa

st.set_page_config(
    layout="wide"
)

st.markdown("<h1 style='text-align: center;'>Dashboard de Mensajes por WhatsApp API</h1>", unsafe_allow_html=True)

modo = st.segmented_control(
    "Selecciona la fuente de datos:",
    ["Meta (API de WhatsApp)", "Listas de distribución"]
)

if modo == "Meta Dashboard (API de WhatsApp)":
    df = load_data("DataClean.csv")
    st.markdown("<h2 style='text-align: center;'>Resumen General</h2>", unsafe_allow_html=True)
    met_totales(df)
    met_insights(df)
    st.divider()

    st.markdown("<h3 style='text-align: center;'>Mensajes por plantilla</h3>", unsafe_allow_html=True)
    met_categoria(df)

    st.markdown("<h3 style='text-align: center;'>Mensajes por día</h3>", unsafe_allow_html=True)
    met_mensajes_dias(df)

    st.markdown("<h3 style='text-align: center;'>Costo Acumulado</h3>", unsafe_allow_html=True)
    costo_acumulado(df)

    st.markdown("<h3 style='text-align: center;'>Costo Diario</h3>", unsafe_allow_html=True)
    costo_diario(df)
elif modo == "Listas de distribución":
    df = load_all_lists()

    st.markdown("<h2 style='text-align: center;'>Resumen de Listas de Distribución</h2>", unsafe_allow_html=True)

    met_listas_totales(df)
    met_lists_insights(df)
    st.divider()

    st.markdown("<h3 style='text-align: center;'>Mensajes por Programas</h3>", unsafe_allow_html=True)
    met_listas_programas(df)
    st.markdown("<h3 style='text-align: center;'>Mensajes por Días</h3>", unsafe_allow_html=True)
    met_listas_dias(df)
    st.markdown("<h3 style='text-align: center;'>Mensajes por Programas y Días</h3>", unsafe_allow_html=True)
    heatmap_programa_fecha(df)
    st.markdown("<h3 style='text-align: center;'>Contactos Únicos por Programa</h3>", unsafe_allow_html=True)
    contactos_unicos_por_programa(df)


