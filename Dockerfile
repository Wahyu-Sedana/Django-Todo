FROM python:3.9

WORKDIR /todo
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.

RUN python manage.py makemigrations
RUN python manage.py migrate