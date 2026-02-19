import pandas as pd
import requests
import os
from dotenv import load_dotenv
from supabase import create_client


load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
TABLE = os.getenv("SUPABASE_TABLE")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

TENANT_ID = os.getenv("TENANT_ID")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
FILE_PATH = os.getenv("ONEDRIVE_FILE_PATH")


def get_acess_token():

    url = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"

    payload = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "scope": "https://graph.microsoft.com/.default",
        "grant_type": "client_credentials",
    }

    response = requests.post(url, data=payload)
    response.raise_for_status()

    return response.json()["access_token"]

def load_dataframe_to_supabase_upsert(df):
    data = df.to_dict("records")
    response = supabase.table(TABLE).upsert(data).execute()
    return response

def run_etl():
    # EXTRACT

    # TRANSFORM

    # LOAD
    load_dataframe_to_supabase_upsert(df)

    return df
