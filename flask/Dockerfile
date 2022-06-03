FROM python:3.9.13-alpine3.16

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD gunicorn --bind 0.0.0.0:5000 app:app 
