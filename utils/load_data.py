import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    df["fecha_envio"] = pd.to_datetime(df["fecha_envio"], errors="coerce")
    df["conversaciones"] = pd.to_numeric(df["conversaciones"], errors="coerce")
    df["costo"] = (df["costo"].astype(str).str.replace("$", "", regex=False).str.replace('"', "", regex=False).str.replace(",", ".", regex=False).astype(float))
    return df