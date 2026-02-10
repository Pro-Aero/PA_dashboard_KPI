import requests
import pandas as pd
from io import BytesIO

def extract_onedrive(access_token: str, file_id: str) -> pd.DataFrame:
    url = f"https://graph.microsoft.com/v1.0/me/drive/items/{file_id}/content"

    response = requests.get(
        url,
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )
    response.raise_for_status()

    return pd.read_excel(BytesIO(response.content))
