FROM python:3.9-slim-buster

WORKDIR /myapp

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc \
  && apt-get clean

# install python dependencies
RUN pip install --upgrade pip
COPY ./project/requirements.txt .
RUN pip install -r requirements.txt

COPY ./project .
