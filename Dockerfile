FROM python:3.10-slim-buster

LABEL authors="Miguel Rojo"

WORKDIR /app

ENV PYTHONPATH "${PYTHONPATH}:/app"

RUN apt-get update \
    && apt-get install --yes --no-install-recommends \
        gcc g++ libffi-dev pkg-config libmariadbclient-dev


# install dependencies
RUN pip install --upgrade pip

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

WORKDIR /app/django_api

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000
