FROM python:3.10-alpine

COPY requirements.txt /temp/requirements.txt

RUN apk add postgresql-client build-base postgresql-dev

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password testuser
COPY config /config
WORKDIR /config
EXPOSE 8000

USER testuser