FROM python:3.11-slim


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DEBUG=0 

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY todo_app/ .

RUN python manage.py collectstatic --noinput

RUN adduser --disabled-password --gecos '' appuser
USER appuser

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "todo_app.wsgi:application"]


