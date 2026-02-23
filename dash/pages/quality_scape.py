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
st.dataframe(df)

st.divider();

st.subheader("Clientes")

total = len(df)
st.metric("Total", total)

cliente_count = df["Cliente"].value_counts()

cols = st.columns(len(cliente_count))
for col, (cliente, quantidade) in zip (cols, cliente_count.items()):
    with col:
        st.metric(
            label=cliente,
            value=quantidade,
            border=True
        )

st.divider();
