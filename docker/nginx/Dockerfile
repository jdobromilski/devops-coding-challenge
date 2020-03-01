FROM nginx:latest
RUN apt-get update && apt-get install vim -y
EXPOSE 80
COPY default.conf /etc/nginx/conf.d/
CMD ["nginx"]
