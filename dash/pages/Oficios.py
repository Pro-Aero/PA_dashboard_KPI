from sqlalchemy import create_engine
import streamlit as st
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")
HOST = os.getenv("DB_HOST")
PORT = os.getenv("DB_PORT")
DBNAME = os.getenv("DB_NAME")

engine = create_engine(
    f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}",
    connect_args={
        "sslmode": "require"
    },
    pool_size=5,
    max_overflow=2,
    pool_timeout=30,
    pool_recycle=1800
)


@st.cache_data(ttl=300)
def load_data(query):
    return pd.read_sql(query, engine)

query = "SELECT * FROM document_control"
df = load_data(query)

st.dataframe(df)
