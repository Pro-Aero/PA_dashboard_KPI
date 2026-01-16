import pandas as pd

def formatDate(df, columnDate):
    # força datetime
    df[columnDate] = pd.to_datetime(
        df[columnDate],
        format="%d%m%Y",
        errors="coerce"
    )

    # converte NaT -> None
    df[columnDate] = df[columnDate].where(
        df[columnDate].notna(),
        None
    )

    return df
