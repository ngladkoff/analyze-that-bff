FROM python:3.9
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1
RUN apt-get update \
  && apt-get -y install netcat gcc postgresql libpq-dev \
  && pip install psycopg2==2.8.5 \
  && apt-get clean
RUN pip install --upgrade pip
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .