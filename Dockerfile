# pull official base image

FROM python:3.9.6

RUN pip install --no-cache-dir numpy scipy pandas matplotlib django-resized sklearn

# set work directory
RUN mkdir /code
COPY ./code /code
WORKDIR /code 
# set environment variables

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

# install dependencies

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt


# COPY ./compose/local/django/celery/worker/start /start-celeryworker
# RUN sed -i 's/\r$//g' /start-celeryworker
# RUN chmod +x /start-celeryworker

# COPY ./compose/local/django/celery/beat/start /start-celerybeat
# RUN sed -i 's/\r$//g' /start-celerybeat
# RUN chmod +x /start-celerybeat
# copy project
COPY . .

