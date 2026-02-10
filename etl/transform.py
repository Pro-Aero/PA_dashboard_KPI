import pandas as pd
from utils import format_date

DATE_COLUMNS = [
    "data limite",
    "1a iteração",
    "resposta 1a iteração",
    "2a iteração",
    "resposta 2a iteração",
    "aprovado/ arquivado"
]

def transform_document_control(df: pd.DataFrame) -> pd.DataFrame:
    for col in DATE_COLUMNS:
        if col in df.columns:
            df = format_date(df, col)

    df = df.replace({"NaT": None, "nan": None, "NaN": None})
    df = df.where(pd.notnull(df), None)

    return df