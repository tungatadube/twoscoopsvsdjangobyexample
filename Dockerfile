FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY . /code/
RUN apt-get update
RUN apt-get python3-dev default-libmysqlclient-dev -y
RUN pip install --proxy "192.168.100.22:80" -r dev.txt
