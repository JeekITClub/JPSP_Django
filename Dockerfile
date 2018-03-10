FROM python:3.6

COPY . /app
WORKDIR /app

RUN  apt-get update && \
    apt-get -y install supervisor && \
    pip install django && \
	pip install gunicorn && \
	pip install whitenoise
	
COPY ./supervisord.log /data/log/supervisord.log
COPY ./gunicorn.log /data/log/gunicorn.log
EXPOSE 80
WORKDIR /app/jpsp/
CMD gunicorn jpsp.wsgi -b 0.0.0.0:80 -w 2
