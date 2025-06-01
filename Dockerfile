FROM python:3.9-slim

# Definir diretório de trabalho
WORKDIR /modelo

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    xvfb \
    libxi6 \
    libgconf-2-4 \
    default-jdk \
    && rm -rf /var/lib/apt/lists/*

# Baixar e instalar o Chrome (Chromium)
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google.list && \
    apt-get update && apt-get install -y google-chrome-stable

# Copiar os arquivos para o container
COPY . /modelo

# Criar e ativar o ambiente virtual dentro da pasta motor
RUN python -m venv /modelo/motor

# Ativar o ambiente virtual e instalar dependências do Python
RUN /app/motor/bin/pip install --no-cache-dir -r requirements.txt

# Definir o comando de execução ativando o ambiente virtual antes de rodar o código
CMD ["/modelo/motor/bin/python", "/modelo/app/main.py"]