# Utilizamos una imagen base de Python para Django
FROM python:3.10

# Establecemos el directorio de trabajo en /app
WORKDIR /app

# Copiamos los archivos requeridos al contenedor
COPY requirements.txt /app/
COPY . /app/

# Instalamos las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Ejecutamos la migración de la base de datos y colectamos los archivos estáticos
RUN python manage.py makemigrations --noinput
RUN python manage.py migrate --noinput

# Exponemos el puerto que va a ser utilizado por el servidor web de Django
EXPOSE 8000

# Comando para ejecutar el servidor web de Django (Gunicorn es una opción común para producción)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "plantscrud.wsgi:application"]
