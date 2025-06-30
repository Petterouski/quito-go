FROM python:3.11-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el contenido del microservicio tourism
COPY . .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto del microservicio (8001 para tourism)
EXPOSE 8001

# Comando de arranque del servidor FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
