import streamlit as st
import plotly.express as px
import pandas as pd

def met_total(df: pd.DataFrame):
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total mensajes", f"{df['conversaciones'].sum():,}")
    col2.metric("Plantillas distintas", 11)
    col3.metric("Días de envío", df['fecha_envio'].nunique())
    col4.metric("Costo acumulado", f"${df['costo'].sum():,.1f}")

def met_insights(df: pd.DataFrame):
    col1, col2, col3 = st.columns(3)

    prom_mensajes_dia = df['conversaciones'].sum() / df['fecha_envio'].nunique()
    costo_mensaje = df['costo'].sum() / df['conversaciones'].sum()
    top_dia = df.groupby("fecha_envio")["conversaciones"].sum().idxmax()

    col1.metric("Promedio por día", f"{prom_mensajes_dia:,.1f}")
    col2.metric("Costo promedio por mensaje", f"${costo_mensaje:,.2f}")
    col3.metric("Día con más mensajes", top_dia.strftime("%d/%m/%Y"))

def graph_category(df: pd.DataFrame):
    graph = df.groupby("categoria")["conversaciones"].sum().reset_index()
    fig = px.pie(graph, names="categoria", values="conversaciones", hole=0.4)
    st.plotly_chart(fig, use_container_width=True)

def graph_messages_days(df: pd.DataFrame):
    resumen = df.groupby("fecha_envio")["conversaciones"].sum().reset_index()
    fig = px.line(resumen, x="fecha_envio", y="conversaciones")
    st.plotly_chart(fig, use_container_width=True)

def graph_cost_summary(df: pd.DataFrame):
    resumen = df.groupby("fecha_envio")["costo"].sum().cumsum().reset_index()
    fig = px.area(resumen, x="fecha_envio", y="costo")
    st.plotly_chart(fig, use_container_width=True)

def graph_cost_day(df: pd.DataFrame):
    resumen = df.groupby("fecha_envio")["costo"].sum().reset_index()
    fig = px.bar(resumen, x="fecha_envio", y="costo")
    st.plotly_chart(fig, use_container_width=True)