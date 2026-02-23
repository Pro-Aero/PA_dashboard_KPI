import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    layout="wide",
)

@st.cache_data(ttl=300)
def load_data():
    return pd.read_sql("SELECT * FROM quality_scape", engine)

engine = create_engine(st.secrets["DB_URL"])

df = load_data()
st.dataframe(df, use_container_width=True)

st.divider();

st.subheader("Total de Incidências")

total = len(df)
st.metric("Total", total)

cliente_count = df["Cliente"].value_counts()

cols = st.columns(len(cliente_count))
for col, (cliente, quantidade) in zip (cols, cliente_count.items()):
    with col:
        df_cliente = df[df["Cliente"] == cliente]

        reinc = (df_cliente["Reincidência"] == "Sim").sum()

        perc_reinc = (reinc / quantidade) * 100 if quantidade > 0 else 0

        st.metric(
            label=cliente,
            value=quantidade,
            delta=f"{perc_reinc:.1f}% reinc.",
            border=True,
        )

st.divider();

st.subheader("Categoria")

categoria_count = df["Categoria"].value_counts()

cols = st.columns(len(categoria_count))
for col, (categoria, quantidade) in zip (cols, categoria_count.items()):
    with col:
        st.metric(
            label=categoria,
            value=quantidade,
            border=True
        )

st.divider();