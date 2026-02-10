import os
from auth import get_graph_token
from extract_excel import extract_onedrive

def extract():
    token = get_graph_token(
        os.environ["TENANT_ID"],
        os.environ["CLIENT_ID"],
        os.environ["CLIENT_SECRET"],
    )

    df = extract_onedrive(
        token,
        os.environ["ONEDRIVE_FILE_ID"]
    )

    df.columns = df.columns.str.lower().str.strip()
    return df
