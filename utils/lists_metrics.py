import streamlit as st
import pandas as pd
import plotly.express as px

def met_listas_totales(df: pd.DataFrame):
    total = len(df)
    validos_df = df[df["STATUS"] == "válido"]
    errores = total - len(validos_df)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total registros", f"{total:,}")
    col2.metric("Números válidos", f"{len(validos_df):,}")
    col3.metric("Errores (inválidos)", f"{errores:,}")
    col4.metric("Programas distintos", validos_df["PROGRAM"].nunique())

def met_listas_programas(df: pd.DataFrame):
    df = df[df["STATUS"] == "válido"]
    resumen = df["PROGRAM"].value_counts().reset_index()
    resumen.columns = ["PROGRAM", "Cantidad"]
    fig = px.bar(resumen, x="Cantidad", y="PROGRAM", orientation="h")
    st.plotly_chart(fig, use_container_width=True)

def met_listas_dias(df: pd.DataFrame):
    df = df[df["STATUS"] == "válido"]
    resumen = df.groupby("DATE").size().reset_index(name="envíos")
    fig = px.line(resumen, x="DATE", y="envíos")
    st.plotly_chart(fig, use_container_width=True)

def met_lists_insights(df: pd.DataFrame):
    df = df[df["STATUS"] == "válido"]

    col1, col2, col3, col4 = st.columns(4)

    promedio_dia = len(df) / df["DATE"].nunique()
    col1.metric("Promedio por día", f"{promedio_dia:,.1f}")

    programa_top = df["PROGRAM"].mode()[0] if not df["PROGRAM"].mode().empty else "—"
    col2.metric("Programa más enviado", programa_top)

    dia_top = df["DATE"].value_counts().idxmax()
    col3.metric("Día más activo", dia_top.strftime("%d %b %Y"))

    col4.metric("Contactos únicos", df["PHONE"].nunique())

def heatmap_programa_fecha(df: pd.DataFrame):
    df = df[df["STATUS"] == "válido"]
    resumen = df.groupby(["DATE", "PROGRAM"]).size().reset_index(name="envíos")
    fig = px.density_heatmap(resumen, x="DATE", y="PROGRAM", z="envíos", nbinsx=20)
    st.plotly_chart(fig, use_container_width=True)

def contactos_unicos_por_programa(df: pd.DataFrame):
    df = df[df["STATUS"] == "válido"]
    resumen = df.groupby("PROGRAM")["PHONE"].nunique().reset_index(name="Contactos únicos")
    fig = px.bar(resumen, x="PROGRAM", y="Contactos únicos")
    st.plotly_chart(fig, use_container_width=True)