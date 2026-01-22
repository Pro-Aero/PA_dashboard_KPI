import pandas as pd
from dotenv import load_dotenv

def formatDate(df, columnDate):
    df[columnDate] = pd.to_datetime(
        df[columnDate],
        format="%d%m%Y",
        errors="coerce"
    )
    df[columnDate] = df[columnDate].where(
        df[columnDate].notna(),
        None
    )

    return df
