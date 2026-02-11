import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

@st.cache_data(ttl=300)
def load_data():
    return pd.read_sql("SELECT * FROM document_control", engine)

engine = create_engine(st.secrets["DB_URL"])

df = load_data()

st.subheader("Resumo de Documentos")

total = len(df)
st.metric("Total", total)

st.divider();


status_count = df["Situação"].value_counts()

cols = st.columns(len(status_count))

for col, (status, quantidade) in zip (cols, status_count.items()):
    with col:
        st.metric(
            label=status,
            value=quantidade,
        )

st.dataframe(df)