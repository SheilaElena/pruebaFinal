#Exportamos la imagen estable mas reciente
FROM python:latest

# Copiamos los archivos de la aplicación (fijate en las rutas)
WORKDIR /app
COPY . /app

# Instala dependencias a partir del txt de antes
RUN pip install --no-cache-dir -r requirements.txt
# O bien puedes usar la siguiente sentencia que hace lo mismo:
# RUN pip install --no-cache-dir flask mysql-connector-python

# Exponemos el puerto de Flask
EXPOSE 5000

# Comando para iniciar la aplicación
CMD ["python", "app.py"]