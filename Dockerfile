# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /signtalk-flaskpython

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt --break-system

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
