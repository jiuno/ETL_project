## main.py
from etl.sources.excels_1.extract import read_excel
from etl.sources.excels_1.transform import * #funciones
from etl.sources.excels_1.load import save_to_sqlite
from etl.db import get_connection, init_schema


def main():
    conn = get_connection()

    init_schema(conn)
    # ... luego llamar a extract(), transform(), load()

    conn.close()

if __name__ == "__main__":
    main()