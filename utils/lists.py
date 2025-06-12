import pandas as pd
from dateutil.parser import parse
import re

def load_all_lists() -> pd.DataFrame:
    csv1 = pd.read_csv("lists/Beneficiarios 12 mar.csv")
    csv2 = pd.read_csv("lists/Madres 11 may 2.csv")
    csv3 = pd.read_csv("lists/Madres 11 may.csv")
    csv4 = pd.read_csv("lists/Planeación 23 may.csv")
    csv5 = pd.read_csv("lists/Retarjeteo 5 may.csv")
    csv6 = pd.read_csv("lists/Retarjeteo 6 may.csv")
    csv7 = pd.read_csv("lists/Retarjeteo 7 abr.csv")
    csv8 = pd.read_csv("lists/Retarjeteo 13 may.csv")
    df_csvs = pd.concat([csv1, csv2, csv3, csv4, csv5, csv6, csv7, csv8], ignore_index=True)

    excel1 = pd.read_excel("lists/Retarjeteo 3 a 6 jun.xlsx", sheet_name="02 junio")
    excel2 = pd.read_excel("lists/Retarjeteo 3 a 6 jun.xlsx", sheet_name="03 junio")
    excel3 = pd.read_excel("lists/Retarjeteo 3 a 6 jun.xlsx", sheet_name="04 junio")
    excel4 = pd.read_excel("lists/Retarjeteo 3 a 6 jun.xlsx", sheet_name="05 junio")
    excel5 = pd.read_excel("lists/Retarjeteo 9 a 12 jun.xlsx", sheet_name="08 junio")
    excel6 = pd.read_excel("lists/Retarjeteo 9 a 12 jun.xlsx", sheet_name="09 junio")
    excel7 = pd.read_excel("lists/Retarjeteo 9 a 12 jun.xlsx", sheet_name="10 junio")
    excel8 = pd.read_excel("lists/Retarjeteo 9 a 12 jun.xlsx", sheet_name="11 junio")
    df_excels = pd.concat([excel1, excel2, excel3, excel4, excel5, excel6, excel7, excel8], ignore_index=True)

    df_total = pd.concat([df_csvs, df_excels], ignore_index=True)

    df_total = df_total.iloc[:, :4]
    df_total = df_total.dropna(how="all")

    df_total["DATE"] = df_total["DATE"].apply(parse_fecha)
    df_total["DATE"] = df_total["DATE"].dt.date
    df_total["PHONE"] = df_total["PHONE"].apply(limpiar_telefono)
    df_total["STATUS"] = df_total["PHONE"].apply(telefono_valido)

    return df_total

def parse_fecha(valor):
    try:
        texto = str(valor).lower().strip().replace('"', '')

        dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
        for dia in dias_semana:
            texto = texto.replace(dia, '')

        return parse(texto, dayfirst=True, fuzzy=True)
    except:
        return pd.NaT

def limpiar_telefono(cel):
    cel = str(cel).strip()
    if cel.endswith(".0"):
        cel = cel[:-2]
    return cel

def telefono_valido(cel):
    cel = str(cel).strip()
    cel = re.sub(r"\D", "", cel)
    return "válido" if len(cel) == 10 else "inválido"