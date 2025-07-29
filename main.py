## main.py
import sqlite3
from etl.sources.source_1.extract import read_excel
from etl.sources.source_1.transform import * #funciones
from etl.sources.source_1.load import save_to_sqlite
from etl.db import get_connection, init_schema


def main():
    conn = get_connection()

    init_schema(conn)
    # ... luego llamar a extract(), transform(), load()

    conn.close()

if __name__ == "__main__":
    main()