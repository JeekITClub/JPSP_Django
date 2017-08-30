FROM daocloud.io/nginx
COPY /jpsp/frontend/dist /usr/share/nginx/html
EXPOSE 80
