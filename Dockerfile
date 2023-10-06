
FROM python:3.11


ENV PYTHONUNBUFFERED=1

RUN apt -y update && apt -y upgrade\
    && apt-get install -y software-properties-common \
    && add-apt-repository -y ppa:ubuntugis/ppa \
    && add-apt-repository -y ppa:deadsnakes/ppa \
    && apt -y update && apt -y upgrade\
    && apt-get -y install python3.8 python3.8-distutils python3.8-venv \
       gdal-bin libgdal-dev python3-gdal  \
    && apt-get autoremove -y \
    && apt-get autoclean -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /AgroChemicalService







COPY . /AgroChemicalService/



COPY requirements.txt .
COPY requirements.txt /tmp/requirements.txt

RUN pip install -r requirements.txt


COPY . .


CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]