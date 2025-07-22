import polars as pl

def validar_df_polars(df: pl.DataFrame, columnas_fecha: list[str] = [], mostrar_sample: bool = True):
    print("📐 Dimensiones del DataFrame:")
    print(f"Filas: {df.height}, Columnas: {df.width}\n")

    print("🧱 Columnas y tipos:")
    print(df.dtypes)
    print()

    if mostrar_sample:
        print("🔎 Primeras filas:")
        print(df.head(5), "\n")

    print("❓ Valores nulos por columna:")
    print(df.null_count(), "\n")

    print("📊 Estadísticas básicas:")
    print(df.describe(), "\n")

    print("🔁 Duplicados (filas completas):")
    duplicados = df.is_duplicated().sum()
    print(f"{duplicados} duplicados encontrados\n")

    print("🔤 Valores únicos por columna de tipo string:")
    for col in df.columns:
        if df[col].dtype == pl.Utf8:
            print(f"- {col}: {df[col].n_unique()} únicos")
            print(f"  Ejemplo: {df[col].unique().sort().head(5)}\n")

    for col in columnas_fecha:
        try:
            df = df.with_columns([
                pl.col(col).str.strptime(pl.Date, "%Y-%m-%d", strict=False)
            ])
            print(f"📅 Columna '{col}' convertida a fecha. Rango:")
            print(f"{df[col].min()} → {df[col].max()}\n")
        except Exception as e:
            print(f"⚠️ No se pudo convertir '{col}' a fecha: {e}\n")
