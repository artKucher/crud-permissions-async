FROM python:3.10-slim
ENV PYTHONUNBUFFERED 1
ENV LC_ALL C.UTF-8

WORKDIR /code
ADD . /code

RUN pip install --no-cache-dir -r requirements.txt
