import pandas as pd
import numpy as np
from functions import formatDate
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.dialects.postgresql import insert

path = "document_control.xlsx"
DB_URL = "postgresql://dashboard_read_only:Readonlysupadb@db.dayonamzbfgrvmvebsqc.supabase.co:5432/postgres"
table_name = "document_control"
unique_key = "id"

engine = create_engine(DB_URL)

df = pd.read_excel(path)

df.columns = df.columns.str.lower().str.strip()

date_columns = [
    "data limite",
    "1a iteração",
    "resposta 1a iteração",
    "2a iteração",
    "resposta 2a iteração",
    "aprovado/ arquivado"
]

for col in date_columns:
    if col in df.columns:
        df = formatDate(df, col)

df = df.replace({"NaT": None, "nan": None, "NaN": None})
df = df.where(pd.notnull(df), None)

metadata = MetaData()
table = Table(table_name, metadata, autoload_with=engine)

records = df.to_dict(orient="records")

stmt = insert(table).values(records)

update_cols = {
    c.name: stmt.excluded[c.name]
    for c in table.columns
    if c.name != unique_key
}

stmt = stmt.on_conflict_do_update(
    index_elements=[unique_key],
    set_=update_cols
)

with engine.begin() as conn:
    conn.execute(stmt)

print("finish insert")
