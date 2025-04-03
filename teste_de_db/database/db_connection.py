import os
import psycopg2
from psycopg2 import pool
from dotenv import load_dotenv
from contextlib import contextmanager



dotenv_path = os.path.join(os.path.dirname(__file__), "..", "config", ".env")

load_dotenv(dotenv_path)

class DatabaseConnection:
    _pool = None

    @classmethod
    def initialize(cls):
        DB_CONFIG = {
            'host': os.getenv('DB_HOST'),
            'port': os.getenv('DB_PORT'),
            'database': os.getenv('DB_NAME'),
            'user': os.getenv('DB_USER'),
            'password': os.getenv('DB_PASS')
        }
        cls._pool = psycopg2.pool.SimpleConnectionPool(
            minconn=1,
            maxconn=10,
            **DB_CONFIG
        )

    @classmethod
    @contextmanager
    def get_connection(cls):
        if cls._pool is None:
            cls.initialize()
        
        conn = cls._pool.getconn()
        try:
            yield conn
        finally:
            cls._pool.putconn(conn)

    @classmethod
    def close_all_connections(cls):
        if cls._pool:
            cls._pool.closeall()

if __name__ == "__main__":
    try:
        DatabaseConnection.initialize()  
        with DatabaseConnection.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT 1;")
                result = cursor.fetchone()
                print("Conexão bem-sucedida!" if result == (1,) else "Falha na conexão.")
    except Exception as e:
        print(f"Erro ao conectar: {e}")
    finally:
        DatabaseConnection.close_all_connections()
