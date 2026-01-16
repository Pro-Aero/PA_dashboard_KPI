import streamlit as st
import pandas as pd
from db import get_engine

def login():
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if not st.session_state.authenticated:
        st.title("Acesso restrito")

        password = st.text_input("Senha", type="password")

        if st.button("Entrar"):
            if password == st.secrets["APP_PASSWORD"]:
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("Senha inválida")

        st.stop()

login()


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