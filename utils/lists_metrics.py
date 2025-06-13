import streamlit as st
import pandas as pd
import plotly.express as px

def met_lists_total(df: pd.DataFrame):
    total = len(df)
    validos_df = df[df["STATUS"] == "válido"]
    errores = total - len(validos_df)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total registros", f"{total:,}")
    col2.metric("Números válidos", f"{len(validos_df):,}")
    col3.metric("Errores (inválidos)", f"{errores:,}")
    col4.metric("Programas distintos", validos_df["PROGRAM"].nunique())

def met_lists_insights(df: pd.DataFrame):
    df = df[df["STATUS"] == "válido"]

    col1, col2, col3, col4 = st.columns(4)
    promedio_dia = len(df) / df["DATE"].nunique()
    programa_top = df["PROGRAM"].mode()[0]
    dia_top = pd.to_datetime(df["DATE"].value_counts().idxmax())
    plantilla_top = df["TEMPLATE"].mode()[0]

    col1.metric("Promedio por día", f"{promedio_dia:,.1f}")
    col2.metric("Programa más enviado", programa_top)
    col3.metric("Día más activo", dia_top.strftime("%d/%m/%Y"))
    col4.metric("Plantilla más usada", plantilla_top)

def graph_lists_programs(df: pd.DataFrame):
    df = df[df["STATUS"] == "válido"]
    graph = df["PROGRAM"].value_counts().reset_index()
    graph.columns = ["Programa", "Cantidad"]
    fig = px.bar(graph, x="Cantidad", y="Programa", orientation="h")
    st.plotly_chart(fig, use_container_width=True)

def graph_lists_days(df: pd.DataFrame):
    df = df[df["STATUS"] == "válido"]
    graph = df.groupby("DATE").size().reset_index(name="Mensajes")
    graph.columns = ["Fecha", "Mensajes"]
    fig = px.line(graph, x="Fecha", y="Mensajes")
    st.plotly_chart(fig, use_container_width=True)

def graph_lists_templates(df: pd.DataFrame):
    df = df[(df["STATUS"] == "válido") & (df["TEMPLATE"].notna())]
    graph = df["TEMPLATE"].value_counts().reset_index()
    graph.columns = ["TEMPLATE", "Cantidad"]
    fig = px.pie(graph, names="TEMPLATE", values="Cantidad", hole=0.4)
    fig.update_traces(textinfo='percent+value')
    st.plotly_chart(fig, use_container_width=True)

def graph_lists_program_date(df: pd.DataFrame):
    df = df[df["STATUS"] == "válido"]
    graph = df.groupby(["DATE", "PROGRAM"]).size().reset_index()
    graph.columns = ["Fecha", "Programa", "Mensajes"]
    fig = px.density_heatmap(graph, x="Fecha", y="Programa", z="Mensajes", nbinsx=20)
    st.plotly_chart(fig, use_container_width=True)

def graph_lists_only_users_messages(df: pd.DataFrame):
    df = df[df["STATUS"] == "válido"]
    graph = df.groupby("PROGRAM")["PHONE"].nunique().reset_index()
    graph.columns = ["Programa", "Números Únicos"]
    fig = px.bar(graph, x="Programa", y="Números Únicos")
    st.plotly_chart(fig, use_container_width=True)