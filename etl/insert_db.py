import pandas as pd
from sqlalchemy import create_engine, text

engine = create_engine("postgresql://etl_writer:EtluserwriterPA15243@db.dayonamzbfgrvmvebsqc.supabase.co:5432/postgres")

df = pd.read_excel("document_control.xlsx")

df_protocols = (
    df
    .groupby("TIPO")
    .size()
    .reset_index(name="quantidade")
)

df_protocols = df_protocols.rename(columns={
    "TIPO": "protocolo"
})

df_client = (
    df
    .groupby("CLIENTE")
    .size()
    .reset_index(name="documents")
)

df_client = df_client.rename(columns={
    "CLIENTE": "cliente"
})

df_situation = (
    df
    .groupby("SITUAÇÃO")
    .size()
    .reset_index(name="quantidade")
)

df_situation = df_situation.rename(columns={
    "SITUAÇÃO": "situation",
    "quantidade": "quantity"
})

df["int_1"] = df["1a ITERAÇÃO"].notna()
df["int_2"] = df["2a ITERAÇÃO"].notna()
df["int_3"] = df["SITUAÇÃO"].str.lower().eq("arquivado")

interacao = pd.DataFrame({
    "interacao": [1, 2, 3],
    "quantidade": [
        df["int_1"].sum(),
        df["int_2"].sum(),
        df["int_3"].sum()
    ]
})

upsert_protocolos = text("""
INSERT INTO dashboard_protocolos (protocolo, quantidade)
VALUES (:protocolo, :quantidade)
ON CONFLICT (protocolo)
DO UPDATE SET quantidade = EXCLUDED.quantidade;
""")

upsert_clients = text("""
INSERT INTO dashboard_clients (cliente, documents)
VALUES (:cliente, :documents)
ON CONFLICT (cliente)
DO UPDATE SET documents = EXCLUDED.documents;
""")

upsert_situation = text("""
INSERT INTO dashboard_situation (situation, quantity)
VALUES (:situation, :quantity)
ON CONFLICT (situation)
DO UPDATE SET quantity = EXCLUDED.quantity;
""")

upsert_interacts = text("""
INSERT INTO dashboard_interacts (interacao, quantidade)
VALUES (:interacao, :quantidade)
ON CONFLICT (interacao)
DO UPDATE SET quantidade = EXCLUDED.quantidade;
""")

with engine.begin() as conn:
    conn.execute(
        upsert_protocolos,
        df_protocols.to_dict(orient="records")
    )

    conn.execute(
        upsert_clients,
        df_client.to_dict(orient="records")
    )

    conn.execute(
        upsert_situation,
        df_situation.to_dict(orient="records")
    )

    conn.execute(
        upsert_interacts,
        interacao.to_dict(orient="records")
    )
