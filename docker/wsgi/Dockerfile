FROM python:latest
EXPOSE 3031
WORKDIR /app
RUN apt-get update && apt-get install nginx vim -y
RUN pip3 install --upgrade pip && pip3 install uwsgi
COPY myapp.py .
RUN useradd -m -s /usr/sbin/nologin uwsgi
RUN chown -R uwsgi:uwsgi /app

CMD [ "uwsgi", "--socket", "0.0.0.0:3031", "--protocol", "http", "--uid","uwsgi", "--wsgi", "myapp" ]
