from extract import extract_excel
from transform import transform_document_control
from load import load_dataframe

PATH = "document_control.xlsx"
TABLE = "document_control"
UNIQUE_KEY = "id"

def main():
    df = extract_excel(PATH)
    df = transform_document_control(df)
    load_dataframe(df, TABLE, UNIQUE_KEY)
    print("ETL finalizado com sucesso")

if __name__ == "__main__":
    main()
