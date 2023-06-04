FROM python:3
ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONBUFFERED 1

RUN mkdir /teams
WORKDIR /hackernews
COPY requirements.txt /teams/
RUN pip install -r requirements.txt

COPY . /teams/
CMD python manage.py runserver 0.0.0.0:8080