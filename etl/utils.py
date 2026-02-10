import pandas as pd


def format_date(df: pd.DataFrame, column: str) -> pd.DataFrame:
    df[column] = pd.to_datetime(
        df[column],
        format="%d%m%Y",
        errors="coerce"
    )
    df[column] = df[column].where(df[column].notna(), None)
    return df
