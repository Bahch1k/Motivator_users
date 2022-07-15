FROM python:3.10.5-alpine3.15

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/Motivator_users

COPY ./requirements.txt usr/src/requirements.txt
RUN pip install -r usr/src/requirements.txt

COPY . /usr/src/Motivator_users

EXPOSE 8000


