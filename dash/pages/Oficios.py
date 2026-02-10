import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

@st.cache_data(ttl=300)
def load_data():
    return pd.read_sql("SELECT * FROM test_table", engine)

engine = create_engine(os.getenv("DB_URL"))


df = load_data()
st.dataframe(df)