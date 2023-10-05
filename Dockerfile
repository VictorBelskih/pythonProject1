
FROM python:3.11


ENV PYTHONUNBUFFERED=1


WORKDIR /AgroChemicalService







COPY . /AgroChemicalService/



COPY requirements.txt .
COPY requirements.txt /tmp/requirements.txt

RUN pip install -r requirements.txt


COPY . .


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]