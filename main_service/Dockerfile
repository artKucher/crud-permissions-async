FROM python:3.10-slim
LABEL maintainer="info@smart-transport.ru"
ENV PYTHONUNBUFFERED 1
ENV LC_ALL C.UTF-8
ENV TZ Asia/Yekaterinburg

WORKDIR /code
ADD . /code

RUN pip install --no-cache-dir -r requirements.txt
