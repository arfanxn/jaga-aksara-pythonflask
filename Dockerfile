# syntax=docker/dockerfile:1

FROM alpine:latest

RUN apk update
RUN apk add gcc build-base mariadb-connector-c-dev python3-dev py3-pip

WORKDIR /jaga-aksara-flaskpython

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt --break-system-packages

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]