import streamlit as st
import pandas as pd
from db import get_engine

st.set_page_config(page_title="Dashboard Supabase", layout="wide")

engine = get_engine()

query = "SELECT * FROM document_control"

df = pd.read_sql(query, engine,index_col='id')

st.title("Dados do Supabase")
st.sidebar.success("Select something above")


st.metric(
    label = "Total de Oficios",
    value=len(df),
    border=True
)

st.dataframe(df)