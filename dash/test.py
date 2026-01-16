import psycopg2

conn = psycopg2.connect(
    host="dayonamzbfgrvmvebsqc.supabase.co",
    port=5432,
    dbname="postgres",
    user="dashboard_read_only",
    password="Readonlysupadb",
    sslmode="require"
)

print("CONECTOU")
