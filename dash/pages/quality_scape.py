import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
import plotly.express as px

load_dotenv()

st.set_page_config(
    layout="wide",
)

@st.cache_data(ttl=300)
def load_data():
    return pd.read_sql("SELECT * FROM quality_scape", engine)

engine = create_engine(st.secrets["DB_URL"])

df = load_data()

st.subheader("Total de Incidências")
col1, col2, col3 = st.columns(3)

total = len(df)
col1.metric("Total", total)

reinc = df[df["Reincidência"] == "Sim"].shape[0]
perc_reinc = (reinc / total) * 100
col2.metric("Reincidência", f"{perc_reinc:.2f}%")

#df["Hora de início"] = pd.to_datetime(df["Hora de início"])
#df["Hora de conclusão"] = pd.to_datetime(df["Hora de conclusão"])
#df["tempo_resolucao"] = (
#    df["Hora de conclusão"] - df["Hora de início"]
#).dt.total_seconds() / 3600
#tempo_medio = df["tempo_resolucao"].mean()
#ol3.metric("Tempo médio", tempo_medio)


cliente_count = df["Cliente"].value_counts()

cols = st.columns(len(cliente_count))
for col, (cliente, quantidade) in zip (cols, cliente_count.items()):
    with col:
        df_cliente = df[df["Cliente"] == cliente]

        st.metric(
            label=cliente,
            value=quantidade,
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

df_group = (
    df.groupby(["Cliente", "Categoria"])
    .size()
    .reset_index(name="count")
)

order = (
    df.groupby("Cliente")
    .size()
    .sort_values()
    .index
)

fig = px.bar(
    df_group,
    x="count",
    y="Cliente",
    color="Categoria",
    orientation="h",
    category_orders={"Cliente": order}
)

st.subheader("Gráfico de Incidências por Cliente")
st.plotly_chart(fig, use_container_width=True)

st.divider();

df_reinc = (
    df.groupby("Cliente")["Reincidência"]
    .apply(lambda x: (x == "Sim").sum() / len(x) * 100)
    .reset_index(name="perc_reinc")
)

fig = px.bar(
    df_reinc,
    x="perc_reinc",
    y="Cliente",
    orientation="h",
    text="perc_reinc"
)

fig.update_traces(
    texttemplate="%{text:.1f}%",
    textposition="outside"
)

st.subheader("Gráfico de Reincidências por Cliente")
st.plotly_chart(fig, use_container_width=True)

st.divider();
st.subheader("Tabela geral quality Scape")
st.dataframe(df)