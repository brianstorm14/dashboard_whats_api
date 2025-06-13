import pandas as pd
from dateutil.parser import parse
import re

def load_all_lists() -> pd.DataFrame:
    csv1 = pd.read_csv("lists/beneficiarios_tarjetas 12 mar.csv")
    csv2 = pd.read_csv("lists/recoger_tarjeta 5 may.csv")
    csv3 = pd.read_csv("lists/dia_madres_2025 9 may.csv", nrows=1000)
    csv4 = pd.read_csv("lists/dia_madres_2025_2 10 may.csv", nrows=1000)
    csv5 = pd.read_csv("lists/renovacion_tarjeta_3 19 a 25 may.csv")
    csv6 = pd.read_csv("lists/Retarjeteo 3  jun.csv")
    csv7 = pd.read_csv("lists/Retarjeteo 4 jun.csv")
    csv8 = pd.read_csv("lists/Retarjeteo 5 jun.csv")
    csv9 = pd.read_csv("lists/Retarjeteo 39 jun.csv")
    csv10 = pd.read_csv("lists/Retarjeteo 9 jun.csv")
    csv11 = pd.read_csv("lists/Retarjeteo 10 jun.csv", nrows=1000)
    csv12 = pd.read_csv("lists/Retarjeteo 11 jun.csv")
    csv13 = pd.read_csv("lists/Retarjeteo 12 jun.csv")
    df_csvs = pd.concat([csv1, csv2, csv3, csv4, csv5, csv6, csv7, csv8, csv9, csv10, csv11, csv12, csv13], ignore_index=True)

    df_total = df_csvs

    df_total = df_total.iloc[:, :5]
    df_total = df_total.dropna(how="all")

    df_total["DATE"] = df_total["DATE"].apply(parse_fecha)
    df_total["DATE"] = df_total["DATE"].dt.date
    df_total["PHONE"] = df_total["PHONE"].apply(limpiar_telefono)
    df_total["STATUS"] = df_total["PHONE"].apply(telefono_valido)

    return df_total

def parse_fecha(valor):
    try:
        return pd.to_datetime(str(valor).strip(), format="%d/%m/%y", dayfirst=True, errors="coerce")
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