
FROM python:3.11.4


ENV PYTHONUNBUFFERED=1



WORKDIR /AgroChemicalService

GDAL_LIBRARY_PATH = '/usr/lib/libgdal.so'
GEOS_LIBRARY_PATH = '/usr/lib/libgeos_c.so'





COPY . /AgroChemicalService/



COPY requirements.txt .
COPY requirements.txt /tmp/requirements.txt

RUN pip install -r requirements.txt


COPY . .


CMD ["gunicorn", "agrochemicalservice.wsgi:application", "--bind", "0.0.0.0:8000"]