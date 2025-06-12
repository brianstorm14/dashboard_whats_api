import streamlit as st
from utils.load_data import load_data
from utils.lists import load_all_lists
from utils.metrics import met_categoria, met_mensajes_dias, met_totales, met_insights, costo_acumulado, costo_diario

st.set_page_config(
    layout="wide"
)

st.markdown("<h1 style='text-align: center;'>Dashboard de Mensajes por WhatsApp API</h1>", unsafe_allow_html=True)

modo = st.segmented_control(
    "Selecciona la fuente de datos:",
    ["Meta (API de WhatsApp)", "Listas de distribución"]
)

if modo == "Meta (API de WhatsApp)":
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
else:
    df = load_all_lists()
    st.dataframe(df)

