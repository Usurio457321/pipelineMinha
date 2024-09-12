import psycopg2
import os
from dotenv import load_dotenv
import traceback

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

# Verifica se as variáveis estão sendo carregadas corretamente
print(f"DB_HOST: {DB_HOST}")
print(f"DB_NAME: {DB_NAME}")
print(f"DB_USER: {DB_USER}")
print(f"DB_PASS: {DB_PASS}")

try:
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )
    print("Conexão bem-sucedida!")
    conn.close()
except Exception as e:
    print("Erro ao conectar:")
    traceback.print_exc()
