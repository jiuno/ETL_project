FROM ubuntu:22.04

# Instalar dependencias
RUN apt-get update && apt-get install -y \
    python3 python3-pip openssh-server sudo postgresql-client && \
    mkdir -p /var/run/sshd && \
    apt-get clean

# Crear usuario SSH
RUN useradd -m -s /bin/bash etluser && echo "etluser:etlpassword" | chpasswd && adduser etluser sudo

# Configuración del directorio de trabajo
WORKDIR /app

# Copiar e instalar dependencias
COPY requirements.txt /app/
RUN pip3 install --no-cache-dir -r requirements.txt

# Exponer puerto SSH
EXPOSE 22

# Comando de inicio
CMD ["/usr/sbin/sshd", "-D"]
