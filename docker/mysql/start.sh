#!/bin/bash
    #

echo "---------------start mysql image-------------------"
docker run --name mysql \
-v $(pwd)/conf.d:/etc/mysql/conf.d \
-v $(pwd)/data:/var/lib/mysql \
-e MYSQL_ROOT_PASSWORD=123456 \
-p 3307:3306 \
-d daocloud.io/mysql:5.6.30