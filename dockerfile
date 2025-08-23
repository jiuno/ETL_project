# Imagen base
FROM python:3.11

# Crear carpeta de trabajo
WORKDIR /app

# Copiar scripts
COPY . /app

# Instalar librerías necesarias
RUN pip install --no-cache-dir pandas sqlalchemy psycopg2-binary openpyxl
