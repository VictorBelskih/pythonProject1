
FROM python:3.11


ENV PYTHONUNBUFFERED=1



WORKDIR /AgroChemicalService







COPY . /AgroChemicalService/

RUN pip install GDAL-3.4.3-cp311-cp311-win_amd64.whl

COPY requirements.txt .
COPY requirements.txt /tmp/requirements.txt

RUN pip install -r requirements.txt


COPY . .


CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]