# Copyright 2013 Thatcher Peskens
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

FROM ubuntu:16.04

MAINTAINER Dockerfiles<qiushimao@hotmail.com>

# Install required packages and remove the apt packages cache when done.

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
	git \
	python3 \
	python3-dev \
	python3-setuptools \
	python3-pip \
	nginx \
	supervisor \
	sqlite3 && \
	pip3 install -U pip setuptools && \
   rm -rf /var/lib/apt/lists/*

# install uwsgi now because it takes a little while
RUN pip3 install uwsgi
RUN pip3 install django
RUN pip3 install django-cors-headers
# setup all the configfiles
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

COPY nginx-app.conf /etc/nginx/sites-available/default
COPY supervisor-app.conf /etc/supervisor/conf.d/
COPY . /home/docker/jpsp/
RUN sudo curl http://npmjs.org/install.sh | sudo sh
RUN sudo npm install -g cnpm --registry=https://registry.npm.taobao.org
RUN cd /home/docker/jpsp/jpsp/frontend
RUN sudo cnpm install
RUN sudo npm build
RUN python3 /home/docker/jpsp/jpsp/manage.py collectstatic
# COPY requirements.txt and RUN pip install BEFORE adding the rest of your code, this will cause Docker's caching mechanism
# to prevent re-installing (all your) dependencies when you made a change a line or two in your app.

# install django, normally you would remove this step because your project would already
# be installed in the code/app/ directory

EXPOSE 80
CMD ["supervisord", "-n"]