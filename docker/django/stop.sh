docker exec -d mysql mysql -uroot -p123456 -e "create database blog;"
docker build -t feiyu/django-app .
docker run --name django \
-v /usr/src/jianshu \
-v /usr/src/jianshu/static \                                                                 --link mysql:mysql \
--link redis:redis \
-p 12000:8000 \
-d feiyu/django-app /usr/local/bin/uwsgi --http :8000 --chdir /usr/src/jianshu -w jianshu.wsgi