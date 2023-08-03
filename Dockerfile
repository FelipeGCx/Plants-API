FROM python:3.10
WORKDIR /app
COPY requirements.txt /app/
COPY . /app/
RUN python -m venv venv
ENV PATH="/app/venv/bin:$PATH"
RUN pip install --no-cache-dir -r requirements.txt
RUN python manage.py makemigrations --noinput
RUN python manage.py migrate --noinput
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# EXPOSE 8000
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "plantscrud.wsgi:application"]
