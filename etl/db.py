import sqlite3

def get_connection(db_path="db/negocio.db"):
    return sqlite3.connect(db_path)

def init_schema(conn):
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id_producto INTEGER PRIMARY KEY,
            nombre TEXT,
            categoria TEXT,
            precio REAL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ventas (
            id_venta INTEGER PRIMARY KEY,
            fecha TEXT,
            id_producto INTEGER,
            id_sucursal INTEGER,
            cantidad INTEGER,
            FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sucursales (
            id_sucursal INTEGER PRIMARY KEY,
            nombre TEXT,
            ciudad TEXT
        )
    """)

    conn.commit()
    print("📐 Esquema de base de datos creado.")



def drop_all(conn):
    """Elimina todas las tablas (uso con precaución)."""
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS ventas")
    cursor.execute("DROP TABLE IF EXISTS productos")
    cursor.execute("DROP TABLE IF EXISTS sucursales")
    conn.commit()
    print("⚠️ Todas las tablas fueron eliminadas.")