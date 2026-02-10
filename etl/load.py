from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.dialects.postgresql import insert
import os

def load_dataframe(
    df,
    table_name: str,
    unique_key: str
):
    engine = create_engine(os.environ["DATABASE_URL"])

    metadata = MetaData()
    table = Table(table_name, metadata, autoload_with=engine)

    records = df.to_dict(orient="records")

    stmt = insert(table).values(records)

    update_cols = {
        c.name: stmt.excluded[c.name]
        for c in table.columns
        if c.name != unique_key
    }

    stmt = stmt.on_conflict_do_update(
        index_elements=[unique_key],
        set_=update_cols
    )

    with engine.begin() as conn:
        conn.execute(stmt)