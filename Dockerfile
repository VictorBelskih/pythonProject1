
FROM python:3.11.4


ENV PYTHONUNBUFFERED=1



WORKDIR /app

COPY . /app/



COPY requirements.txt .


RUN pip install -r requirements.txt


COPY . .


CMD ["gunicorn", "agrochemicalservice.wsgi:application", "--bind", "0.0.0.0:8000"]