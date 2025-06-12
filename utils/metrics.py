import streamlit as st
import plotly.express as px
import pandas as pd

def met_categoria(df: pd.DataFrame):
    resumen = df.groupby("categoria")["conversaciones"].sum().reset_index()
    fig = px.pie(resumen, names="categoria", values="conversaciones", hole=0.3)
    st.plotly_chart(fig, use_container_width=True)

def met_mensajes_dias(df: pd.DataFrame):
    resumen = df.groupby("fecha_envio")["conversaciones"].sum().reset_index()
    fig = px.line(resumen, x="fecha_envio", y="conversaciones")
    st.plotly_chart(fig, use_container_width=True)

def costo_acumulado(df: pd.DataFrame):
    resumen = df.groupby("fecha_envio")["costo"].sum().cumsum().reset_index()
    fig = px.area(resumen, x="fecha_envio", y="costo")
    st.plotly_chart(fig, use_container_width=True)

def costo_diario(df: pd.DataFrame):
    resumen = df.groupby("fecha_envio")["costo"].sum().reset_index()
    fig = px.bar(resumen, x="fecha_envio", y="costo")
    st.plotly_chart(fig, use_container_width=True)

def met_totales(df: pd.DataFrame):
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total mensajes", f"{df['conversaciones'].sum():,.0f}")
    col2.metric("Plantillas distintas", 11)
    col3.metric("Días de envío", df['fecha_envio'].nunique())
    col4.metric("Costo acumulado", f"${df['costo'].sum():,.2f}")

def met_insights(df: pd.DataFrame):
    col1, col2, col3 = st.columns(3)

    prom_mensajes_dia = df['conversaciones'].sum() / df['fecha_envio'].nunique()
    col1.metric("Promedio por día", f"{prom_mensajes_dia:,.1f}")

    costo_mensaje = df['costo'].sum() / df['conversaciones'].sum()
    col2.metric("Costo promedio por mensaje", f"${costo_mensaje:,.4f}")

    top_dia = df.groupby("fecha_envio")["conversaciones"].sum().idxmax()
    col3.metric("Día con más mensajes", top_dia.strftime("%d %b %Y"))


