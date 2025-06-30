# Usa una imagen base de Python liviana
FROM python:3.11-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el contenido del microservicio de autenticación
COPY . .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que corre FastAPI para este servicio (ej. 8000)
EXPOSE 8000

# Comando para ejecutar la app con Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
