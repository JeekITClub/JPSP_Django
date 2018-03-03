FROM python:3.6

COPY . /app
WORKDIR /app

RUN apk add --update --no-cache supervisor && \
    pip install django && \
	pip install gunicorn && \
	pip install whitenoise


