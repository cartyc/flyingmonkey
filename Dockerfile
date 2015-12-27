FROM python:3.5
ENV PYTHONBUFFERED 1
run mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN apt-get -y update && apt-get -y install binutils libproj-dev gdal-bin
RUN pip install -r requirements.txt
ADD . /code/

RUN pip install -r requirements.txt
