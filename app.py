import streamlit as st

from utils.load_data import load_data
from utils.lists import load_all_lists
from utils.metrics import graph_category, graph_messages_days, met_total, met_insights, graph_cost_summary, graph_cost_day
from utils.lists_metrics import graph_lists_days, graph_lists_programs, met_lists_total, met_lists_insights, graph_lists_program_date, graph_lists_only_users_messages, graph_lists_templates

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center;'>Dashboard de Mensajes por WhatsApp API</h1>", unsafe_allow_html=True)

modo = st.segmented_control("Selecciona la fuente de datos:", ["Meta Dashboard", "Listas de distribución"])

if modo == "Meta Dashboard":
    df = load_data("DataClean.csv")
    st.markdown("<h2 style='text-align: center;'>Resumen General</h2>", unsafe_allow_html=True)
    met_total(df)
    met_insights(df)
    st.divider()

    st.markdown("<h3 style='text-align: center;'>Mensajes por plantilla</h3>", unsafe_allow_html=True)
    graph_category(df)

    st.markdown("<h3 style='text-align: center;'>Mensajes por día</h3>", unsafe_allow_html=True)
    graph_messages_days(df)

    st.markdown("<h3 style='text-align: center;'>Costo Acumulado</h3>", unsafe_allow_html=True)
    graph_cost_summary(df)

    st.markdown("<h3 style='text-align: center;'>Costo Diario</h3>", unsafe_allow_html=True)
    graph_cost_day(df)

elif modo == "Listas de distribución":
    df = load_all_lists()

    st.markdown("<h2 style='text-align: center;'>Resumen de Listas de Distribución</h2>", unsafe_allow_html=True)

    met_lists_total(df)
    met_lists_insights(df)
    st.divider()

    st.markdown("<h3 style='text-align: center;'>Mensajes por Programas</h3>", unsafe_allow_html=True)
    graph_lists_programs(df)
    st.markdown("<h3 style='text-align: center;'>Mensajes por Días</h3>", unsafe_allow_html=True)
    graph_lists_days(df)
    st.markdown("<h3 style='text-align: center;'>Plantillas más usadas</h3>", unsafe_allow_html=True)
    graph_lists_templates(df)
    st.markdown("<h3 style='text-align: center;'>Mensajes por Programas y Días</h3>", unsafe_allow_html=True)
    graph_lists_program_date(df)
    st.markdown("<h3 style='text-align: center;'>Contactos Únicos por Programa</h3>", unsafe_allow_html=True)
    graph_lists_only_users_messages(df)


