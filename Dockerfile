
FROM python:3.11 AS init

WORKDIR /app
COPY . .    

ENV VIRTUAL_ENV=/app/.venv_docker
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN python3.11 -m venv $VIRTUAL_ENV
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Formato JSON para CMD
CMD ["reflex", "run", "--host", "0.0.0.0", "--env", "prod", "--backend-only"]

# docker run -d -p 8000:8000 --name app app_stock:latest
# comando para iniciar un contenedor con la imagen creada